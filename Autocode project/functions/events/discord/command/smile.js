const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/U1p83COiAPYAAAAC/anime-happy-anime-smile.gif',
  'https://c.tenor.com/6x5NsgRFxFUAAAAC/animegirl-anime.gif',
  'https://c.tenor.com/nuKmYDgaDpAAAAAC/anime-smile.gif',
  'https://c.tenor.com/Vtjibw10S4AAAAAC/cute-smiling.gif',
  'https://c.tenor.com/IyKy95tPdNgAAAAC/smiling-thinking.gif',
  'https://c.tenor.com/BL5odrhdEKIAAAAC/eru-cute.gif',
  'https://images6.fanpop.com/image/photos/38400000/Cute-anime-girl-blushing-anime-38465673-500-275.gif',
  'https://data.whicdn.com/images/327605476/original.gif',
  'https://c.tenor.com/xHbq3PpKgiEAAAAC/phone-cellphone.gif',
  'https://c.tenor.com/DbRVEHMsm-YAAAAC/yoruka-smile-yoruka.gif',
  
  'https://c.tenor.com/P6Cih-37NKAAAAAC/anime-girl.gif',
  'https://c.tenor.com/rGhny9QnU5EAAAAC/anime-girl.gif',
  'https://c.tenor.com/rUxuwcDGJr8AAAAC/anime-girl.gif',
  'https://c.tenor.com/Giv4A22u3KUAAAAd/zero-two-smile.gif',
  'https://c.tenor.com/SYdxYyZyQJkAAAAC/zero-two-smile.gif',
  'https://c.tenor.com/jDzuJe3ss3wAAAAd/zero-two-darling-in-the-franxx.gif',
  'https://c.tenor.com/YGuLegQWubwAAAAC/miku-nakano-gotoubun-no-hanayome.gif',
  'https://c.tenor.com/5bEVbZkSVigAAAAC/erio-touwa-erio-towa.gif',
  'https://c.tenor.com/ujrhrLQlskIAAAAC/anime-zero-two.gif',
  'https://c.tenor.com/s83QlJ7AMvUAAAAC/shikimori.gif',
  
  'https://c.tenor.com/eMsHZ2dl79AAAAAC/kawaii-dake-janai.gif',
  'https://c.tenor.com/FoYi0sJGkvcAAAAC/shikimori.gif',
  'https://c.tenor.com/92OMpo8hascAAAAC/smile-stare.gif',
  'https://c.tenor.com/fF1yz0HOUAoAAAAC/shikimoris-not-just-a-cutie-kawaii-dake-ja-nai-shikimorisan.gif',
  'https://c.tenor.com/z95FBoVL7zUAAAAC/shugo-chara.gif',
  'https://c.tenor.com/ZglUG-3bnOAAAAAC/anime-shikimoris-not-just-cute.gif',
  'https://c.tenor.com/G3k9xdBSjM4AAAAC/reina-kousaka-hibike-euphonium.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
