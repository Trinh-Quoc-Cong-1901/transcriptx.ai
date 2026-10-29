"""Soft background bed for walkthrough videos: slow piano arpeggios over a warm pad, 76 BPM, C major.

Pure-Python synthesis (no samples, no licensing questions). Writes a 16-bit stereo WAV.
Usage: python3 gen_soft_music.py out.wav [seconds]
"""
import array, math, random, sys, wave

SR = 44100
BPM = 76
BEAT = 60 / BPM
BAR = BEAT * 4
CHORDS = [[48, 55, 59, 64], [45, 52, 55, 60], [41, 48, 52, 57], [43, 50, 55, 59]]   # Cmaj7 Am7 Fmaj7 G6


def mtof(m):
    return 440 * 2 ** ((m - 69) / 12)


def render(dur):
    n = int(SR * dur)
    L, R = array.array('d', bytes(8 * n)), array.array('d', bytes(8 * n))
    rnd = random.Random(11)

    # pad: sine + soft 2nd harmonic, slow swell per bar, slightly detuned left/right
    for b in range(int(dur / BAR) + 1):
        t0 = b * BAR
        notes = [m + 12 for m in CHORDS[b % 4][1:]]
        i0, i1 = int(t0 * SR), min(n, int((t0 + BAR + 1.2) * SR))
        for m in notes:
            f = mtof(m)
            for i in range(i0, i1):
                t = i / SR - t0
                env = min(1, t / 0.9) * (1 if t < BAR else max(0.0, 1 - (t - BAR) / 1.2))
                a = 0.018 * env
                L[i] += a * (math.sin(2 * math.pi * f * 0.998 * t) + 0.25 * math.sin(4 * math.pi * f * t))
                R[i] += a * (math.sin(2 * math.pi * f * 1.002 * t) + 0.25 * math.sin(4 * math.pi * f * t))

    # piano-ish arpeggio: eighth notes, harmonics with exponential decay, gentle velocity changes
    step = BEAT / 2
    k = 0
    while k * step < dur - 0.5:
        t0 = k * step
        ch = CHORDS[int(t0 / BAR) % 4]
        pattern = [ch[0] + 12, ch[1] + 12, ch[2] + 12, ch[3] + 12, ch[2] + 24, ch[3] + 12, ch[1] + 12, ch[2] + 12]
        m = pattern[k % 8]
        f = mtof(m)
        vel = 0.055 * (1.0 if k % 8 == 0 else 0.72 + 0.12 * rnd.random())
        pan = 0.5 + 0.18 * math.sin(k * 0.9)
        i0, i1 = int(t0 * SR), min(n, int((t0 + 2.6) * SR))
        for i in range(i0, i1):
            t = i / SR - t0
            env = min(1, t / 0.006) * math.exp(-t * 1.9)
            s = (math.sin(2 * math.pi * f * t) + 0.35 * math.exp(-t * 3) * math.sin(4 * math.pi * f * t)
                 + 0.12 * math.exp(-t * 6) * math.sin(6 * math.pi * f * t)) * env * vel
            L[i] += s * (1 - pan) * 2
            R[i] += s * pan * 2
        k += 1

    # warm low-pass, fades, normalize to -6 dBFS
    a = 1 - math.exp(-2 * math.pi * 3200 / SR)
    yl = yr = 0.0
    for i in range(n):
        yl += a * (L[i] - yl)
        yr += a * (R[i] - yr)
        t = i / SR
        g = min(1, t / 1.2) * min(1, (dur - t) / 2.5)
        L[i], R[i] = yl * g, yr * g
    peak = max(max(abs(v) for v in L), max(abs(v) for v in R)) or 1
    k = 0.5 / peak
    out = array.array('h', bytes(4 * n))
    for i in range(n):
        out[2 * i] = int(L[i] * k * 32767)
        out[2 * i + 1] = int(R[i] * k * 32767)
    return out


def write(path, dur):
    with wave.open(path, 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(render(dur).tobytes())


if __name__ == '__main__':
    write(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 32)
