const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://64.media.tumblr.com/c75a7492ed6153828ccfea76ab659cae/tumblr_pwnqrr3v2M1yqkoyvo1_500.gif',
  'https://c.tenor.com/ESe9mqJlywkAAAAC/anime-girl.gif',
  'https://c.tenor.com/EizBjV8lOFUAAAAd/sad-girl.gif',
  'https://c.tenor.com/PHBzhcOds5oAAAAC/lonely-windy.gif',
  'https://c.tenor.com/AY7ipPod8eQAAAAC/anime-alone.gif',
  'https://c.tenor.com/zAlabxg7g3UAAAAd/anime-sad.gif',
  'https://c.tenor.com/dznqHVbWPlUAAAAC/in-the-rain-sad-story.gif',
  'https://cdn40.picsart.com/174293536000202.gif?to=crop&type=webp&r=-1x-1&q=95',
  'https://c.tenor.com/VTqa0X2W6LUAAAAC/80s-running.gif',
  'https://c.tenor.com/Mlgi6bkVkG8AAAAC/emotional-cry.gif',
  
  'https://c.tenor.com/Foyauwn9foIAAAAC/crying-anime.gif',
  'https://c.tenor.com/Jphp6FfLOXoAAAAC/anime-sad.gif',
  'https://c.tenor.com/cKJS_DQCP08AAAAC/sad-black.gif',
  'https://c.tenor.com/Um4n_9H39FUAAAAd/anime-sad.gif',
  'https://c.tenor.com/J_W8S5Y1GSsAAAAC/triste-sad.gif',
  'https://c.tenor.com/ynltIl-WTboAAAAC/anime-sad.gif',
  'https://c.tenor.com/thw0X00MurYAAAAC/anime-crying.gif',
  'https://64.media.tumblr.com/b3a2d708f6ee36a5dbbb56d49b9e41e4/tumblr_nz3y5ckZPM1tb7stoo2_500.gif',
  'https://c.tenor.com/wobdcikOtM0AAAAC/darling-in-the-franxx.gif',
  'https://c.tenor.com/lZPEIcCXehkAAAAC/anime-cry.gif',
  
  'https://c.tenor.com/uuqQq_-vw_YAAAAC/zero-two-cartoon.gif',
  'https://i.pinimg.com/originals/62/1d/80/621d80330c06c1bd1a11de2eb8cf5abf.gif',
  'https://c.tenor.com/15_OSXV_GZoAAAAC/zero-two-crying.gif',
  'https://c.tenor.com/E1y1Afk6mmYAAAAC/crying-cry.gif',
  'https://c.tenor.com/3lDNGJnzSt0AAAAC/anime-hug.gif',
  'https://c.tenor.com/D2FVIXyTMpsAAAAC/shoko-nishimiya-nishimiya.gif',
  'https://c.tenor.com/Nv4dk-B-BVsAAAAC/cry-sad.gif',
  'https://c.tenor.com/cpDRqZxQvYQAAAAC/sorry-anime.gif',
  'https://c.tenor.com/lcUIc0XdCHQAAAAC/triste-anime.gif',
  'https://c.tenor.com/FPvXCv0GzRgAAAAC/no-sad.gif',
  
  'https://c.tenor.com/bC8PzqKp4ngAAAAC/secre-swallowtail-black-clover.gif',
  'https://c.tenor.com/HUewq2uQi30AAAAC/anime-crying.gif',
  'https://c.tenor.com/-se3g87dEXIAAAAC/anime-sad.gif',
  'https://c.tenor.com/72RCIUZt5QcAAAAC/anime-sad.gif',
  'https://c.tenor.com/c40yj8LchX4AAAAC/anime-anime-girl-sad.gif',
  'https://c.tenor.com/VDwrKFrSyHsAAAAC/anime-running.gif',
  'https://c.tenor.com/9NQ6gwp930oAAAAC/violet-evergarden-anime.gif'
]

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
