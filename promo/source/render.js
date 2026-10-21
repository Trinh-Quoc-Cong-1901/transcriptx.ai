// node render.js            -> full video.mp4 (silent)
// node render.js 1.5,8.6    -> test_<t>.jpg stills
const puppeteer = require('puppeteer'); const { spawn } = require('child_process'); const ff = require('ffmpeg-static');
(async () => {
  const b = await puppeteer.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true, args: ['--allow-file-access-from-files', '--hide-scrollbars'] });
  const pg = await b.newPage(); await pg.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await pg.goto('file://' + __dirname + '/index.html', { waitUntil: 'load' });
  await pg.evaluate(async () => { await document.fonts.ready; fixGrad(); });
  const only = process.argv[2];
  if (only) {
    for (const s of only.split(',')) { await pg.evaluate(t => seek(t), +s); await pg.screenshot({ path: `${__dirname}/test_${s}.jpg`, type: 'jpeg', quality: 70 }); }
    await b.close(); return;
  }
  const FPS = 30;
  const proc = spawn(ff, ['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-pix_fmt', 'yuv420p', __dirname + '/video.mp4'], { stdio: ['pipe', 'ignore', 'inherit'] });
  for (let f = 0; f < FPS * 30; f++) {
    await pg.evaluate(t => seek(t), f / FPS);
    const buf = await pg.screenshot({ type: 'jpeg', quality: 95 });
    if (!proc.stdin.write(buf)) await new Promise(r => proc.stdin.once('drain', r));
    if (f % 150 === 0) console.log('frame', f);
  }
  proc.stdin.end(); await new Promise(r => proc.on('close', r)); await b.close();
})();
