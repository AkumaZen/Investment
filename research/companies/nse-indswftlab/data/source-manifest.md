# Ind-Swift Laboratories - source manifest

Built 2026-11-09.
Company codes: NSE INDSWFTLAB, BSE 532305.
Raw files are in `docs/INDSWFTLAB/raw` and text extracts in `docs/INDSWFTLAB/text`, with "=== PAGE N ===" markers on physical PDF pages; docs/ is kept out of git.
Hashes are the first 12 hex digits of SHA-256 of the local file (also in `data/doc-index.json`).
Every document was read directly by Claude in this session; no worker models were used.

## Order of sources and what was checked

1. User upload: the Q2 FY27 call transcript (machine transcript; names garbled in places).
2. BSE filings via Screener `get_document_list`: decks, the Q1 FY27 transcript, annual reports, CARE monitoring agency reports.
3. NSE filings: the warrant allotment (17 Sep 2026) and conversion (8 Oct 2026) outcomes, found by web search and downloaded from nsearchives.nseindia.com.
4. CARE Ratings site: the Mar 2024 rating rationale (history only).
5. Screener.in: multi-year tables, shareholding and peers only (`data/screener-2026-11-09.md`), tagged [Screener].
6. Not available: Screener announcements returned nothing; Screener lists no earnings call transcripts other than those above, so the claims ledger covers Jan 2026 to Nov 2026 only.

## Documents

| Local file | What | Date | Pages | SHA-256 (12) | Tag | URL |
|---|---|---|---|---|---|---|
| uploads/Ind_Swift_Laboratories_Ltd_Sep_2026_Transcript.pdf | Q2 FY27 call transcript (user upload) | Call 4 Nov 2026 | n/a | n/a | [call pN], [tr-q2 pN] | User upload; BSE carries only the audio link: https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=3c6a2f5f-35f6-41c7-9c0f-7b7ea47c9ea3.pdf |
| raw/deck-q2fy27.pdf | Q2 FY27 investor deck | Filed 4 Nov 2026 | 32 | 5ef84216b5b8 | [deck pN], [D-Q2 pN] | https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=6385edbd-a83b-4fd6-9885-0743f7cb9a2e.pdf |
| raw/tr-q1fy27.pdf | Q1 FY27 call transcript | Filed Aug 2026 | 15 | c0d69839fe5d | [tr-q1 pN] | https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=20e51151-92d1-4584-b075-38946d071365.pdf |
| raw/deck-q1fy27.pdf | Q1 FY27 investor deck | Aug 2026 | 29 | 50378d082cf1 | [D-Q1 pN] | https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=53bc6695-3b3b-4d54-9e49-fd338cb7b144.pdf |
| raw/deck-q3fy26.pdf | Q3 FY26 investor deck | 4 Feb 2026 | 27 | ee5061355bc7 | [D-Q3 pN] | https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=b38c0cc9-6ef5-4074-a68b-0d45a9dfcee5.pdf |
| raw/deck-jan26.pdf | Corporate deck | 14 Jan 2026 | 25 | a81c1b4cfe6c | [D-Jan26 pN] | https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=1aea0d8d-53f1-4c67-9417-9110bc29ff21.pdf |
| raw/deck-q1fy21-old.pdf | Q1 FY21 deck, old API company (history only) | 2020 | 26 | bd7b969f89dc | [D-2020] | https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=715cd916-569d-434c-8c3c-f7d129dc5604.pdf |
| raw/deck-q2fy21-old.pdf | Q2 FY21 deck, old API company (history only) | 2020 | 28 | b70cfc8bb2a9 | [D-2020] | https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=43b9a794-56b9-4a7f-bb2e-c501cd49879f.pdf |
| raw/ar-fy26.pdf | Annual report FY26 | 5 Sep 2026 | 136 | 504f7d0078e4 | [AR26 pN] | https://www.bseindia.com/xml-data/corpfiling/AttachHis/1030038a-682c-455c-9ee3-7f2c273fa639.pdf |
| raw/ar-fy25.pdf | Annual report FY25 | 5 Sep 2025 | 109 | 9e0832abbb55 | [AR25 pN] | https://www.bseindia.com/xml-data/corpfiling/AttachHis/00dc7b70-03cb-4573-99ed-0b3e05ebf276.pdf |
| raw/ar-fy24.pdf | Annual report FY24 | 6 Sep 2024 | 100 | ca7eb0238c18 | [AR24 pN] | https://www.bseindia.com/xml-data/corpfiling/AttachHis/255c9918-ec21-425b-9dbb-88eaf0bd13a1.pdf |
| raw/care-ma-final.pdf | CARE monitoring agency final report, issue 1 (Rs 314.60 cr) | Filed 3 Nov 2026 | 13 | e407bc2a9024 | [CARE-F pN] | https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=e0af5fc1-e457-4aa2-abdd-655b65463742.pdf |
| raw/care-ma-q2fy27.pdf | CARE monitoring agency Q2 FY27 report, issue 2 (Rs 137.20 cr) | Filed 3 Nov 2026 | 13 | 8c4b619d9acb | [CARE-Q2 pN] | https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=e6ff1c5d-b9c5-4e88-a6a8-2662fb3398e5.pdf |
| raw/care-rating-mar24.pdf | CARE rating rationale (history) | Mar 2024 | 6 | cca1e31c8084 | [CARE-R24] | https://www.careratings.com/upload/CompanyFiles/PR/202403130346_Ind-Swift_Laboratories_Limited.pdf |
| raw/nse-warrant-allotment-17sep26.pdf | Allotment of 70,00,000 warrants at Rs 196 to Essix Biosciences | 17 Sep 2026 | 1 | 493b77456b84 | [NSE-A] | https://nsearchives.nseindia.com/corporate/INDSWFTLAB_17092026174502_Outcome_Allotment.pdf |
| raw/nse-warrant-conversion-08oct26.pdf | Conversion of 14,00,000 warrants into shares (Essix) | 8 Oct 2026 | 2+ | 77085c385e2d | [NSE-C] | https://nsearchives.nseindia.com/corporate/INDSWFTLAB_08102026183706_Committee_Meeting_Outcome_08102026.pdf |

## Data sources other than filings

| Source | Used for | Fetched |
|---|---|---|
| Screener.in consolidated pages for INDSWFTLAB and 8 peers | Multi-year P&L, cash flow, balance sheet, ratios, quarterly, shareholding, peer multiples | 2026-11-09T15:53-15:55Z |
| Web search (standard) | Locating the NSE warrant filings | 2026-11-09 |
| EGM summary, multibagg.ai (secondary) | Confirms the 5 Aug 2026 EGM approved 70 lakh warrants to a promoter entity; not used for any number | 2026-11-09 |

## Not found or not available

- Earlier earnings calls of the merged FDF business (FY25 to Q4 FY26): not listed on Screener or found on BSE in this session. Not Disclosed for the claims ledger before Jan 2026.
- NCLT merger scheme and swap ratio documents: not collected; the AR FY26 directors' report figures are used instead (45,15,495 shares to promoter-group holders of Ind-Swift Ltd [AR26 p40]).
- Slump-sale agreement terms (escrow, indemnities): not disclosed in the documents read.
- Regulator databases (MHRA, TGA, EU GMP): not queried; plant approvals come from the company's deck and are marked as company claims.
