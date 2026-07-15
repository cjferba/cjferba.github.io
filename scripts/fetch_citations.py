#!/usr/bin/env python3
"""Refresh citation stats from OpenAlex (by ORCID) for the Publications page chart.

No API key needed. Run manually whenever you want fresher citation counts:

    python3 scripts/fetch_citations.py

Writes data/en/citations.json, which assets/scripts/citations-chart.js reads
client-side on the Publications page.
"""
import json
import urllib.request
from collections import defaultdict
from pathlib import Path

ORCID = "0000-0002-8809-8676"
USER_AGENT = "cjferba-personal-site/1.0 (mailto:cjferba@decsai.ugr.es)"
ROOT = Path(__file__).resolve().parent.parent


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def main():
    author = fetch(f"https://api.openalex.org/authors?filter=orcid:{ORCID}")["results"][0]
    author_id = author["id"].rsplit("/", 1)[-1]
    stats = author["summary_stats"]

    works = fetch(
        f"https://api.openalex.org/works?filter=author.id:{author_id}"
        "&per_page=100&select=id,doi,title,publication_year,cited_by_count"
    )["results"]

    by_year = defaultdict(int)
    for w in works:
        by_year[w["publication_year"]] += w["cited_by_count"]

    out = {
        "total_citations": author["cited_by_count"],
        "h_index": stats["h_index"],
        "i10_index": stats["i10_index"],
        "works_count": author["works_count"],
        "citations_by_year": dict(sorted(by_year.items())),
    }

    out_path = ROOT / "data" / "en" / "citations.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {out_path}")
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
