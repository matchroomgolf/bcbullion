export default async function handler(req, res) {
  async function spot(sym) {
    const r = await fetch('https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/' + sym + '/USD', { headers: { 'User-Agent': 'Mozilla/5.0 (bcbullion)' } });
    if (!r.ok) throw new Error('swissquote ' + sym + ' ' + r.status);
    const data = await r.json();
    const bids = [];
    for (const p of data) for (const sp of (p.spreadProfilePrices || [])) if (typeof sp.bid === 'number') bids.push(sp.bid);
    if (!bids.length) return null;
    bids.sort(function (a, b) { return a - b; });
    return Math.round(bids[Math.floor(bids.length / 2)] * 100) / 100;
  }
  try {
    const r = await Promise.all([spot('XAU'), spot('XAG'), spot('XPT')]);
    res.setHeader('Cache-Control', 's-maxage=60, stale-while-revalidate=120');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.status(200).json({ gold: r[0], silver: r[1], platinum: r[2], updatedAt: new Date().toISOString(), source: 'Swissquote' });
  } catch (e) {
    res.setHeader('Cache-Control', 'no-store');
    res.status(502).json({ error: String((e && e.message) || e) });
  }
}
