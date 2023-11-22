const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/oUqKSJWeL8UAAAAC/cute-tired.gif',
  'https://c.tenor.com/NmzkpFEiNmwAAAAC/sleepy-nap.gif',
  'https://c.tenor.com/Izq6jHHDk20AAAAC/idolypride-anime.gif',
  'https://c.tenor.com/7Dzdo9JkSKwAAAAC/morning.gif',
  'https://c.tenor.com/GVVgz1vTXkcAAAAC/zero-two-yawn.gif',
  'https://c.tenor.com/re9a71mA5xwAAAAC/nogamenolife-shiro.gif',
  'https://c.tenor.com/jv-3NEyxpBwAAAAC/anime-yawning.gif',
  'https://c.tenor.com/jZOShuoKnm4AAAAC/sleepy-anime.gif',
  'https://c.tenor.com/_IBaj604zp8AAAAC/tired-kon.gif',
  'https://c.tenor.com/-2mSlbqgBlwAAAAC/sleepy-anime.gif',
  
  'https://c.tenor.com/s3g_66o9UDcAAAAC/anime-mornings.gif',
  'https://c.tenor.com/nRPVJFlw6GAAAAAC/anime-girl.gif',
  'https://c.tenor.com/Pu42qpMGiusAAAAC/anime-girl.gif',
  'https://c.tenor.com/AwkXTbTvvfUAAAAC/k-on-ui-hirasawa.gif',
  'https://c.tenor.com/a5gKYNKn6GIAAAAC/anime-k-on.gif',
  'https://c.tenor.com/PQt3WyEZZwQAAAAC/code-geass-good-morning.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
