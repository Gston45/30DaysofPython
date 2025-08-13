#Exercices
#1
import json
import requests
from bs4 import BeautifulSoup

URL = "http://www.bu.edu/president/boston-university-facts-stats/"

def extract_tables(soup):
    """Retourne une liste de tables.
       Chaque table est soit une liste de dictionnaires (si en-têtes),
       soit une liste de listes (si pas d’en-têtes)."""
    tables_data = []
    for table in soup.find_all("table"):
        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        rows = []
        for tr in table.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all("td")]
            if cells:
                rows.append(cells)

        if headers and rows and all(len(r) == len(headers) for r in rows):
            as_dicts = [dict(zip(headers, r)) for r in rows]
            tables_data.append({"type": "table_with_headers", "headers": headers, "rows": as_dicts})
        elif rows:
            tables_data.append({"type": "table_rows_only", "rows": rows})
    return tables_data

def extract_fact_lists(soup):
    """Beaucoup de pages 'facts' utilisent des listes <ul>/<ol> sous des titres <h2>/<h3>.
       On capture titre + items de liste pour les sauver proprement."""
    facts = []
    for heading in soup.find_all(["h2", "h3"]):
        title = heading.get_text(strip=True)
        nxt = heading.find_next_sibling()
        items = []
        jumps = 0
        while nxt and jumps < 2 and not nxt.name in ["ul", "ol"]:
            nxt = nxt.find_next_sibling()
            jumps += 1
        if nxt and nxt.name in ["ul", "ol"]:
            for li in nxt.find_all("li"):
                items.append(li.get_text(" ", strip=True))
        if items:
            facts.append({"section": title, "items": items})
    return facts

def scrape_bu_facts(url=URL, out_path="bu_facts.json"):
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    data = {
        "url": url,
        "title": (soup.title.get_text(strip=True) if soup.title else "Untitled"),
        "tables": extract_tables(soup),
        "fact_lists": extract_fact_lists(soup),
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Sauvegardé → {out_path}")
    print(f"Résumé: {len(data['tables'])} tables, {len(data['fact_lists'])} sections de listes.")

if __name__ == "__main__":
    scrape_bu_facts()
