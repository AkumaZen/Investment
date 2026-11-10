"""Cache full page-labelled PDF extracts, or run a company's ordered build manifest."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')


def extract(pdf, cache):
    import fitz
    pdf = pdf.resolve()
    source_hash = sha(pdf)
    extractor = 'page-text-v1/pymupdf-' + fitz.VersionBind
    key = hashlib.sha256((source_hash + extractor).encode()).hexdigest()
    meta_path, text_path = cache / (key + '.json'), cache / (key + '.txt')
    if meta_path.exists() and text_path.exists():
        meta = json.loads(meta_path.read_text(encoding='utf-8'))
        if (meta.get('source_sha256') == source_hash and meta.get('extractor') == extractor
                and meta.get('text_sha256') == sha(text_path)):
            print(json.dumps({'cache_hit': True, 'text': str(text_path.resolve()), 'metadata': str(meta_path.resolve())}))
            return
    with fitz.open(pdf) as doc:
        pages = [(i + 1, p.get_text()) for i, p in enumerate(doc)]
    cache.mkdir(parents=True, exist_ok=True)
    text_path.write_text('\n'.join(f'=== PHYSICAL PAGE {n} ===\n{text}' for n, text in pages), encoding='utf-8')
    save(meta_path, {'source_sha256': source_hash, 'first_source_path': str(pdf), 'extractor': extractor,
                     'pages': len(pages), 'low_text_pages': [n for n, t in pages if len(t.strip()) < 80],
                     'text_sha256': sha(text_path), 'coverage_status': 'extracted; not evidence of reading',
                     'visual_review': 'Reader must inspect scans, tables and charts, including text-rich pages.'})
    print(json.dumps({'cache_hit': False, 'text': str(text_path.resolve()), 'metadata': str(meta_path.resolve())}))


def run(config_path, check):
    config_path = config_path.resolve()
    config = json.loads(config_path.read_text(encoding='utf-8-sig'))
    cwd = (config_path.parent / config.get('working_directory', '.')).resolve()
    stages = config.get('stages')
    if not cwd.is_dir() or not isinstance(stages, list) or not stages:
        raise ValueError('Manifest needs an existing working_directory and nonempty stages.')
    names = set()
    for stage in stages:
        name, argv = stage.get('name'), stage.get('argv')
        if not isinstance(name, str) or not name or name in names:
            raise ValueError('Stage names must be nonempty and unique.')
        names.add(name)
        if not isinstance(argv, list) or not argv or not all(isinstance(a, str) and a for a in argv):
            raise ValueError(f'{name}: argv must be a nonempty list of strings.')
        if not shutil.which(argv[0]):
            raise ValueError(f'{name}: executable unavailable: {argv[0]}')
        if len(argv) > 1 and argv[1].endswith(('.py', '.mjs', '.js')) and not (cwd / argv[1]).is_file():
            raise ValueError(f'{name}: script missing: {cwd / argv[1]}')
    outputs = config.get('outputs', [])
    if not isinstance(outputs, list) or not all(isinstance(p, str) and p for p in outputs):
        raise ValueError('outputs must be a list of paths.')
    if check:
        print(f'Valid command manifest: {len(stages)} stages. No commands executed; QA not certified.')
        return 0
    log_path = cwd / config.get('log', 'qa/build-run.json')
    log = {'started_utc': datetime.now(timezone.utc).isoformat(), 'manifest_sha256': sha(config_path),
           'status': 'running', 'stages': [], 'token_usage': None,
           'manual_visual_review': 'required separately', 'outputs': []}
    save(log_path, log)
    for stage in stages:
        start = time.monotonic()
        print(f'Running {stage["name"]}', flush=True)
        try:
            result = subprocess.run(stage['argv'], cwd=cwd, check=False)
            code = result.returncode
        except OSError as error:
            code = 1
            print(str(error), file=sys.stderr)
        log['stages'].append({'name': stage['name'], 'argv': stage['argv'], 'exit_code': code,
                              'elapsed_seconds': round(time.monotonic() - start, 3)})
        if code:
            log['status'] = 'failed'
            save(log_path, log)
            return code
        save(log_path, log)
    for name in outputs:
        path = cwd / name
        if not path.is_file():
            log.update(status='failed', missing_output=str(path.resolve()))
            save(log_path, log)
            return 1
        log['outputs'].append({'path': str(path.resolve()), 'sha256': sha(path), 'bytes': path.stat().st_size})
    log['status'] = 'commands-passed; manual review required'
    save(log_path, log)
    print(f'Command stages passed; run log: {log_path.resolve()}. Complete manual PDF review before delivery.')
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    ex = sub.add_parser('extract')
    ex.add_argument('pdf', type=Path)
    ex.add_argument('--cache', type=Path, required=True)
    build = sub.add_parser('run')
    build.add_argument('manifest', type=Path)
    build.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.command == 'extract':
        extract(args.pdf, args.cache)
        return 0
    return run(args.manifest, args.check)


if __name__ == '__main__':
    sys.exit(main())
