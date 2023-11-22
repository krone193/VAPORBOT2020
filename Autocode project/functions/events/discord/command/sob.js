const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/0EgQgZWi8WoAAAAC/sigh-yamadakun-and-the-seven-witches.gif',
  'https://c.tenor.com/z-tjiE68w40AAAAC/kiniromozaic-kinmozaic.gif',
  'https://c.tenor.com/LuFqQfvs36QAAAAC/sigh-anime.gif',
  'https://c.tenor.com/2f3Hik1lEm0AAAAC/sigh-tame-iki.gif',
  'https://c.tenor.com/PCcfYlHhNTEAAAAC/mashiro-shiina-sigh.gif',
  'https://c.tenor.com/-ugVcXNgn-IAAAAC/sakurasou-mashiro.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
