# Augmont research status

Security: NSE **AUGMONT**, BSE **544888**, India, INR. Research cutoff: **7 November 2026**.

**Status: readable interim report available; full all-document research remains incomplete.**

Open [the HTML report](report.html) locally or download [the 23-page PDF draft](report-draft.pdf). The report contains all twenty sections, with 55.6% of section text devoted to understanding the business. It explicitly marks unfinished source reviews and does not give an actionable price target.

The [calculation model](model.py), [model output](data/model-output.json) and [QA results](qa-results.json) accompany the draft. Rebuild with `python model.py`, then `python build_report.py` from this folder. Local browser checks use installed Microsoft Edge via `python check_report.py`.

Start with [STATUS.md](STATUS.md) for the latest checkpoint and [HANDOFF.md](HANDOFF.md) to resume work.

The [finished research prompt](prompts/Augmont%20Enterprises%20Research%20Prompt.md) governs the report. Prompt preparation used only the uploaded Q2 FY27 transcript. The report must use all available documents, including the DRHP, RHP, prospectus, annual reports, results, decks and material announcements.

The repository preserves the prompt, extracted evidence, financial tool snapshots, source inventory, scripts, report renderer and validation records. The approximately 1 GB of re-downloadable public filings and duplicate downloads remains in the local cache. Their source URLs and paths are recorded in [source-inventory.json](source-inventory.json); cached does not mean read or verified. The user-supplied transcript and staged report-design references are preserved.

No trade or external communication has been made. Git pushes are authorised by the user for progress checkpoints.
