// Serverless contact-form handler. Emails B.C. Bullion (Boone) on submit.
// Setup (one-time, in Vercel project env): set RESEND_API_KEY (free at resend.com).
// Optional env: CONTACT_TO (default hello@bcbullion.com), CONTACT_FROM (a verified sender).
export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'method' });

  try {
    const body = typeof req.body === 'string' ? JSON.parse(req.body || '{}') : (req.body || {});
    const name = String(body.name || '').trim().slice(0, 200);
    const email = String(body.email || '').trim().slice(0, 200);
    const message = String(body.message || '').trim().slice(0, 5000);

    if (!name || !email || !message) return res.status(400).json({ ok: false, error: 'Please fill in your name, email, and message.' });
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return res.status(400).json({ ok: false, error: 'Please enter a valid email address.' });

    const KEY = process.env.RESEND_API_KEY;
    const TO = process.env.CONTACT_TO || 'hello@bcbullion.com';
    const FROM = process.env.CONTACT_FROM || 'B.C. Bullion Website <onboarding@resend.dev>';
    // Not configured yet -> tell the client to show the call/email fallback (don't pretend it sent).
    if (!KEY) return res.status(503).json({ ok: false, error: 'unconfigured' });

    const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    const html =
      `<h2 style="font-family:Georgia,serif;color:#0E1B2C">New message from the B.C. Bullion website</h2>` +
      `<p><strong>Name:</strong> ${esc(name)}<br><strong>Email:</strong> ${esc(email)}</p>` +
      `<p style="white-space:pre-wrap">${esc(message)}</p>`;

    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: FROM,
        to: [TO],
        reply_to: email,
        subject: `Website inquiry from ${name}`,
        html,
        text: `New message from the B.C. Bullion website\n\nName: ${name}\nEmail: ${email}\n\n${message}`
      })
    });

    if (!r.ok) {
      const detail = await r.text().catch(() => '');
      return res.status(502).json({ ok: false, error: 'send_failed', detail: detail.slice(0, 300) });
    }
    return res.status(200).json({ ok: true });
  } catch (e) {
    return res.status(500).json({ ok: false, error: String((e && e.message) || e) });
  }
}
