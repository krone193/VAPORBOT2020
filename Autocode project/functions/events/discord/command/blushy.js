const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/eT_HnoX8eKoAAAAC/happy-anime.gif',
  'https://c.tenor.com/voCLgP3672MAAAAC/anime-manga.gif',
  'https://c.tenor.com/vjgGw6IEFuUAAAAC/brilho-anime.gif',
  'https://c.tenor.com/-E4Y8d-JxL4AAAAC/soft-neko.gif',
  'https://c.tenor.com/uT9BWeRBJwYAAAAC/blushing-anime-girl.gif',
  'https://c.tenor.com/2cWyWrf4ucAAAAAC/cyan-hijirikawa-show-by-rock.gif',
  'https://c.tenor.com/hCqcNUuWCf0AAAAC/blush-anime.gif',
  'https://c.tenor.com/6NbEUdgkBq4AAAAC/smile-happy.gif',
  'https://c.tenor.com/Vu533jLjgw0AAAAC/shy-ughm.gif',
  'https://c.tenor.com/kEKQYGO0riUAAAAC/red-anime.gif',
  
  'https://c.tenor.com/4JBrfqDM83UAAAAC/smile-cute.gif',
  'https://c.tenor.com/e5GIh587OssAAAAC/anime-blushing.gif',
  'https://c.tenor.com/fapsneQ0NTkAAAAd/embarrassed-embarrasment.gif',
  'https://c.tenor.com/l-ItaKTK6hgAAAAC/miku-anime.gif',
  'https://i.pinimg.com/originals/e4/3b/87/e43b871792e070252eaf22bd3e9dc8f6.gif',
  'https://c.tenor.com/W_Ks8z4l6fkAAAAC/girl-redhead.gif',
  'https://c.tenor.com/_uXObgxomDYAAAAC/blush-blushing.gif',
  'https://c.tenor.com/49dpSIFkVusAAAAC/melting-blushing-anime-girl.gif',
  'https://c.tenor.com/KRanAbPK67gAAAAC/my-dress.gif',
  'https://c.tenor.com/tLLTTY_vi6UAAAAC/anime.gif',
  
  'https://c.tenor.com/yY7EhaDIy8wAAAAC/girl-blush.gif',
  'https://c.tenor.com/qcaSPLhZgBwAAAAd/anime-anime-shy.gif',
  'https://c.tenor.com/opoMIJ7CIl8AAAAC/anime-blushing.gif',
  'https://c.tenor.com/ZXsS-5L_sOQAAAAC/shikimoris-not-just-a-cutie-kawaii-dake-ja-nai-shikimorisan.gif',
  'https://c.tenor.com/CWnPiOhLm_IAAAAC/girl-cute.gif',
  'https://c.tenor.com/MxVdwoBgJ8YAAAAC/fuuka-miyazawa-anime.gif',
  'https://c.tenor.com/r3jQx9Wot14AAAAC/reina-kousaka-cute.gif',
  'https://c.tenor.com/nQI4bxAYjcsAAAAC/hibike.gif'
]

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
