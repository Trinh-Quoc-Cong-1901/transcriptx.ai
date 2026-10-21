// Synthesized 30s launch track, 120 BPM, A minor. Writes music.wav
const fs = require('fs');
const SR = 44100, DUR = 30, N = SR * DUR;
const L = new Float32Array(N), R = new Float32Array(N);
const BEAT = 0.5;
let seed = 7; const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647) * 2 - 1;
const mtof = m => 440 * Math.pow(2, (m - 69) / 12);
const put = (i, l, r = l) => { if (i >= 0 && i < N) { L[i] += l; R[i] += r; } };

// Chords: Am F C G, 4s each
const CH = [[45, 57, 60, 64], [41, 57, 60, 65], [48, 55, 60, 64], [43, 55, 59, 62]];
const chordAt = t => CH[Math.floor(t / 4) % 4];

// ---- Pad (detuned saws, lowpass opening over time)
{
  let lpL = 0, lpR = 0; const ph = new Float64Array(32);
  for (let i = 0; i < N; i++) {
    const t = i / SR, ch = chordAt(t), ct = t % 4;
    const env = Math.min(1, ct / 0.25) * (ct > 3.7 ? Math.max(0, (4 - ct) / 0.3) : 1);
    let sl = 0, sr = 0;
    ch.forEach((m, k) => {
      for (let d = 0; d < 3; d++) {
        const j = k * 3 + d, f = mtof(m + 12) * (1 + (d - 1) * 0.006);
        ph[j] = (ph[j] + f / SR) % 1; const s = 2 * ph[j] - 1;
        if (d === 0) sl += s; else if (d === 2) sr += s; else { sl += s * .5; sr += s * .5; }
      }
    });
    const cut = t < 5 ? 300 + t * 120 : t < 22.5 ? 1400 + (t - 5) * 40 : 2400;
    const a = 1 - Math.exp(-2 * Math.PI * cut / SR);
    lpL += a * (sl - lpL); lpR += a * (sr - lpR);
    const g = 0.035 * env * (t > 28 ? Math.max(0, (30 - t) / 2) : 1);
    put(i, lpL * g, lpR * g);
  }
}

// ---- Kick
const kick = (t0, amp = 1) => {
  let ph = 0;
  for (let i = 0; i < SR * 0.45; i++) {
    const t = i / SR, f = 45 + 110 * Math.exp(-t * 30);
    ph += f / SR; const s = Math.sin(2 * Math.PI * ph) * Math.exp(-t * 7) * amp * 0.55;
    put(Math.floor(t0 * SR) + i, s);
  }
};
// ---- Noise hit (hat / clap / crash)
const noise = (t0, dur, decay, hp, amp, pan = 0) => {
  let lp = 0;
  for (let i = 0; i < SR * dur; i++) {
    const t = i / SR, n = rnd(); lp += hp * (n - lp);
    const s = (n - lp) * Math.exp(-t * decay) * amp;
    put(Math.floor(t0 * SR) + i, s * (1 - pan), s * (1 + pan));
  }
};
// ---- Pluck arp with ping-pong echo
const pluck = (t0, m, amp) => {
  let ph = 0;
  for (let i = 0; i < SR * 0.35; i++) {
    const t = i / SR; ph = (ph + mtof(m) / SR) % 1;
    const tri = 4 * Math.abs(ph - 0.5) - 1, sq = ph < .5 ? 1 : -1;
    const s = (tri * 0.7 + sq * 0.15 * Math.exp(-t * 30)) * Math.exp(-t * 14) * amp;
    for (let e = 0; e < 4; e++) {
      const k = Math.floor((t0 + e * 0.375) * SR) + i, g = Math.pow(0.42, e);
      put(k, s * g * (e % 2 ? 0.4 : 1), s * g * (e % 2 ? 1 : 0.4));
    }
  }
};
// ---- Sub bass
const bass = (t0, m, len, amp) => {
  let ph = 0;
  for (let i = 0; i < SR * len; i++) {
    const t = i / SR; ph = (ph + mtof(m) / SR) % 1;
    const s = Math.tanh(Math.sin(2 * Math.PI * ph) * 2.2) * Math.min(1, t / .01) * Math.exp(-t * 4) * amp;
    put(Math.floor(t0 * SR) + i, s);
  }
};
// ---- Riser / whoosh: filtered noise swelling up to tEnd
const riser = (t0, tEnd, amp) => {
  let lp = 0, bp = 0;
  for (let i = Math.floor(t0 * SR); i < tEnd * SR; i++) {
    const p = (i / SR - t0) / (tEnd - t0), n = rnd();
    const a = 1 - Math.exp(-2 * Math.PI * (200 + 6000 * p * p) / SR);
    lp += a * (n - lp); bp += 0.05 * (lp - bp);
    const s = (lp - bp) * p * p * amp;
    put(i, s * (1 - .3 * Math.sin(p * 9)), s * (1 + .3 * Math.sin(p * 9)));
  }
};
// ---- Impact: boom + crash
const impact = t0 => { kick(t0, 1.4); bass(t0, 33, 1.6, 0.35); noise(t0, 2.2, 2.2, 0.35, 0.16); };
// ---- UI click
const click = t0 => { for (let i = 0; i < SR * .04; i++) { const t = i / SR; put(Math.floor(t0 * SR) + i, Math.sin(2 * Math.PI * 2400 * t) * Math.exp(-t * 160) * 0.18); } };

// Arrangement
riser(0.3, 5.0, 0.5);
impact(5.0);
for (const [a, b] of [[9.6, 10.5], [14.4, 15.4], [21.6, 22.5]]) riser(a, b, 0.35);
click(8.4); click(11.75); click(12.75);
for (let b = 0; b < 60; b++) {
  const t = b * BEAT;
  if (t >= 5 && t < 28) kick(t, b % 2 ? 0.8 : 1);
  if (t >= 10.5 && t < 28) noise(t + BEAT / 2, 0.08, 60, 0.6, 0.07, (b % 2) * .4 - .2);
  if (t >= 15.5 && t < 28 && b % 2 === 1) noise(t, 0.25, 18, 0.3, 0.11);
  if (t >= 5 && t < 28) for (let e = 0; e < 2; e++) bass(t + e * .25, chordAt(t)[0] - 12, 0.24, 0.17);
}
for (let s = 0; s * 0.125 < 30; s++) {
  const t = s * 0.125; if (t < 10.5 || t >= 28) continue;
  const ch = chordAt(t), pat = [0, 1, 2, 3, 2, 1, 3, 2];
  pluck(t, ch[pat[s % 8]] + 24, t > 22.5 ? 0.09 : 0.065);
}
impact(22.5);
noise(28, 2.0, 2, 0.3, 0.1); kick(28, 1.2); bass(28, 33, 2, 0.3);

// Normalize + write WAV
let peak = 0; for (let i = 0; i < N; i++) peak = Math.max(peak, Math.abs(L[i]), Math.abs(R[i]));
const buf = Buffer.alloc(44 + N * 4);
buf.write('RIFF', 0); buf.writeUInt32LE(36 + N * 4, 4); buf.write('WAVEfmt ', 8);
buf.writeUInt32LE(16, 16); buf.writeUInt16LE(1, 20); buf.writeUInt16LE(2, 22);
buf.writeUInt32LE(SR, 24); buf.writeUInt32LE(SR * 4, 28); buf.writeUInt16LE(4, 32); buf.writeUInt16LE(16, 34);
buf.write('data', 36); buf.writeUInt32LE(N * 4, 40);
const fade = i => Math.min(1, i / (SR * .02), (N - i) / (SR * .05));
for (let i = 0; i < N; i++) {
  buf.writeInt16LE(Math.round(Math.tanh(L[i] / peak * 1.1) * 0.89 * fade(i) * 32767), 44 + i * 4);
  buf.writeInt16LE(Math.round(Math.tanh(R[i] / peak * 1.1) * 0.89 * fade(i) * 32767), 46 + i * 4);
}
fs.writeFileSync(__dirname + '/music.wav', buf);
console.log('music.wav written, peak', peak.toFixed(2));
