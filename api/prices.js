export default async function handler(req, res) {
  async function swissSpot(sym) {
    const r = await fetch('https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/' + sym + '/USD', { headers: { 'User-Agent': 'Mozilla/5.0 (bcbullion)' } });
    if (!r.ok) throw new Error('sq ' + sym + ' ' + r.status);
    const data = await r.json();
    const bids = [];
    for (const p of data) for (const sp of (p.spreadProfilePrices || [])) if (typeof sp.bid === 'number') bids.push(sp.bid);
    if (!bids.length) return null;
    bids.sort(function (a, b) { return a - b; });
    return Math.round(bids[Math.floor(bids.length / 2)] * 100) / 100;
  }
  async function dayPct(yf) {
    try {
      const r = await fetch('https://query1.finance.yahoo.com/v8/finance/chart/' + yf + '?interval=1d&range=1d', { headers: { 'User-Agent': 'Mozilla/5.0' } });
      const m = (await r.json()).chart.result[0].meta;
      const p = m.regularMarketPrice, pc = m.chartPreviousClose || m.previousClose;
      return (p && pc) ? Math.round((p - pc) / pc * 10000) / 100 : null;
    } catch (e) { return null; }
  }
  try {
    const v = await Promise.all([swissSpot('XAU'), swissSpot('XAG'), swissSpot('XPT'), dayPct('GC=F'), dayPct('SI=F'), dayPct('PL=F')]);
    res.setHeader('Cache-Control', 's-maxage=60, stale-while-revalidate=120');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.status(200).json({ gold:{price:v[0],changePct:v[3]}, silver:{price:v[1],changePct:v[4]}, platinum:{price:v[2],changePct:v[5]}, updatedAt:new Date().toISOString(), source:'Swissquote' });
  } catch (e) {
    res.setHeader('Cache-Control', 'no-store');
    res.status(502).json({ error: String((e && e.message) || e) });
  }
}
