#!/usr/bin/env python3
"""Fetch live gold/silver/platinum spot (USD/oz) from Swissquote's public feed -> prices.json"""
import json, urllib.request, statistics, datetime

def spot(sym):
    url = f"https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/{sym}/USD"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (bcbullion price bot)"})
    data = json.load(urllib.request.urlopen(req, timeout=25))
    bids = [sp["bid"] for p in data for sp in p.get("spreadProfilePrices", []) if sp.get("bid")]
    if not bids:
        raise SystemExit(f"No bids returned for {sym}")
    return round(statistics.median(bids), 2)

out = {
    "gold": spot("XAU"), "silver": spot("XAG"), "platinum": spot("XPT"),
    "updatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "source": "Swissquote",
}
with open("prices.json", "w") as f:
    json.dump(out, f, indent=2)
print(out)
