const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/pYzpQgkAQJkAAAAC/violet-evergarden-hug.gif',
  'https://c.tenor.com/FJaQ1MKAtowAAAAd/idk-what-anime-this-is-from-but-its-anime-girls-hugging.gif',
  'https://c.tenor.com/3ergzHiRIBwAAAAC/hug-cuddle.gif',
  'https://c.tenor.com/2tStVop0CowAAAAC/lindo-adorable.gif',
  'https://c.tenor.com/xoZfAA2Rz1oAAAAC/anime-manga.gif',
  'https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif',
  'https://c.tenor.com/Pd2sMiVr09YAAAAC/hug-anime-hug.gif',
  'https://c.tenor.com/UhcyGsGpLNIAAAAC/hug-anime.gif',
  'https://c.tenor.com/zEz00ZxujqMAAAAC/blush-hug.gif',
  'https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif',
  
  'https://c.tenor.com/0vl21YIsGvgAAAAC/hug-anime.gif',
  'https://c.tenor.com/keasv-Cnh4kAAAAd/hug-cuddle.gif',
  'https://acegif.com/wp-content/gif/anime-hug-91.gif',
  'https://c.tenor.com/fjyH7Yd7yG8AAAAC/k-on-hug.gif',
  'https://c.tenor.com/mBmkxNFl5acAAAAC/anime-happy.gif',
  'https://c.tenor.com/Lmc7jvRbcvAAAAAC/darling-in-the-franxx-zero-two.gif',
  'https://c.tenor.com/TULvK6iT9O4AAAAC/anime-group-hug.gif',
  'https://c.tenor.com/XKJwFX9B_DUAAAAC/hug.gif',
  'https://c.tenor.com/CUwv8tibOZoAAAAC/aikatsu-stars.gif',
  'https://c.tenor.com/1YBiXY9SFq0AAAAC/bangdream-bandori.gif',
  
  'https://c.tenor.com/aG0pA87t0dMAAAAC/anime-chino.gif',
  'https://c.tenor.com/bWvPyYDBpdcAAAAC/anime-couple-anime-head-rub.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
