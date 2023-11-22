const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/sjUvV_MMDksAAAAC/anime-girl.gif',
  'https://c.tenor.com/q6vmV7JzZaAAAAAd/anime-oops-my-fault.gif',
  'https://c.tenor.com/HOQ5bxzACaUAAAAC/dandidave-cute.gif',
  'https://c.tenor.com/2cDkLXJpYPAAAAAC/anime-tohru-honda.gif',
  'https://c.tenor.com/3SMAyDkjv6MAAAAC/akane-shinjō-shinjou-akane.gif'
]

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
