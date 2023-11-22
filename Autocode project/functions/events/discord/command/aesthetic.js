const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'http://68.media.tumblr.com/9c482ecfcda309f629ac69168f2c22c2/tumblr_oh44bi2bp91vj2gx4o1_500.gif',
  'http://68.media.tumblr.com/c7bbbfbfd679a3fe7b8036fff709e937/tumblr_oievzj6Xng1sf9678o1_400.gif',
  'https://66.media.tumblr.com/28c8017277686e5e1340420e1cca1be3/tumblr_pwr9qxlpJE1ynwbv0o1_500.gif',
  'http://33.media.tumblr.com/d2d145c8d69a59658f75d2ec2728a243/tumblr_nirkf9POgY1tlm0p2o1_1280.gif',
  'http://38.media.tumblr.com/47a6c4d1c227a20bb4fde22c9fd2d0f4/tumblr_nn17vmeS531tlm0p2o1_1280.gif',
  'http://68.media.tumblr.com/917e28a27d13ffea0a032516149d8dec/tumblr_oiogv7bPJw1w0ii2ho1_500.gif',
  'http://31.media.tumblr.com/5e2be2951c2504779065607305b15d42/tumblr_np90omeRF31ripbvlo1_500.gif',
  'http://78.media.tumblr.com/a2998706b5d2bab367abdeb57f58e689/tumblr_p0z72hXshe1tlkklno1_500.gif',
  'http://68.media.tumblr.com/9e9c3f70954ac563e568e0f4001e481a/tumblr_odo23fF5Lz1snkq37o1_500.gif',
  'https://c.tenor.com/hwjqo-O16cUAAAAC/vaporwave.gif',
  
  'https://c.tenor.com/0TiBV8KRJ-YAAAAd/vaporwave-lord-desktop.gif',
  'https://c.tenor.com/QRnlS5Lxvg8AAAAC/vaporwave-aesthetic.gif',
  'https://c.tenor.com/-sazR0Z_pB8AAAAC/horusultra-vaporwave.gif',
  'https://c.tenor.com/h6nfPchxScUAAAAC/vaporwave-neon.gif',
  'https://c.tenor.com/I3hnQ9yerWkAAAAC/vaper-wave.gif',
  'https://c.tenor.com/KDWou_IneW4AAAAd/dangiuz-cyberpunk.gif',
  'https://c.tenor.com/NpMkKBtHaKkAAAAC/vaporwave-chillwave.gif',
  'https://c.tenor.com/81YAPg8gyBAAAAAd/aesthetic-vaporwave.gif',
  'https://c.tenor.com/kbAXHrIp5agAAAAC/vaporwave-aesthetic.gif',
  'https://c.tenor.com/KfUVTnbtS0oAAAAC/paradise-holiday.gif',
  
  'https://c.tenor.com/zwhit72ZM08AAAAC/vaporwave-seapunk.gif',
  'https://c.tenor.com/fJQffXDzjqUAAAAC/anime-hibike-euphonium.gif',
  'https://pa1.narvii.com/7694/496f14b417db4c0bd2f540e75b588104a1a3ab99r1-500-260_hq.gif',
  'https://64.media.tumblr.com/dda2b45229b5bb77b38f0c18f2cf13cb/tumblr_inline_p79hw9w1CH1seuc55_540.gifv',
  'https://c.tenor.com/b9Rqi7jQNdAAAAAC/red.gif'
]

await vapor.sendgif(
  context.params.event,
  CommandContent,
  false,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
