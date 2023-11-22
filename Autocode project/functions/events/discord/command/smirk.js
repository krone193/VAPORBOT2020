const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/beBYN2X06NwAAAAC/flirty-anime.gif',
  'https://c.tenor.com/gq3hI9ts-fkAAAAC/anime-zero-two.gif',
  'https://c.tenor.com/Er0KtYDvy_cAAAAC/accion-reface.gif',
  'https://c.tenor.com/P1LldG69iPYAAAAC/chika-lenny-face.gif',
  'https://c.tenor.com/XPSM3wbqWXMAAAAC/nagatoro.gif',
  'https://c.tenor.com/EqmQKDJghk4AAAAC/anime-pink-lips.gif',
  'https://c.tenor.com/rDqn-ZL82C0AAAAd/nakano-ichika.gif',
  'https://c.tenor.com/ZglUG-3bnOAAAAAd/anime-shikimoris-not-just-cute.gif',
  'https://media.tenor.com/3D__CbAhTl8AAAAC/girl-cute.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
