const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/qvvKGZhH0ysAAAAC/anime-girl.gif',
  'https://c.tenor.com/Jm8JkCG3NRsAAAAC/anime-ban.gif',
  'https://c.tenor.com/8sPNImjK4KsAAAAC/hologra-hololive.gif',
  'https://c.tenor.com/G8GSrgFFRSsAAAAC/anime-dark.gif',
  'https://c.tenor.com/IPkZqclH7vgAAAAC/anime-hammer.gif',
  'https://c.tenor.com/JKeoUTnu-G0AAAAC/chika-ban-gif-chika.gif',
  'https://i.imgur.com/466l0cw.gif',
  'https://reallifeanime.files.wordpress.com/2014/06/akari-hammer-attack.gif',
  'https://data.whicdn.com/images/232487491/original.gif',
  'https://c.tenor.com/50Yz9iy_MDcAAAAC/jujutsu-kaisen.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
