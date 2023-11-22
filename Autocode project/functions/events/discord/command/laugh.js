const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/k-pqAMqGrcYAAAAC/joshiraku-anime.gif',
  'https://c.tenor.com/NlhCOfkZugAAAAAC/animegirl-laughing.gif',
  'https://c.tenor.com/4gpOJNzpb44AAAAC/zsanime-anime.gif',
  'https://c.tenor.com/XbGebOy9Lf0AAAAC/anime-girl.gif',
  'https://c.tenor.com/GwJ2vJ1gnfcAAAAC/anime-anime-laughing.gif',
  'https://c.tenor.com/74Win7VdWDoAAAAC/anime-laughing.gif',
  'https://c.tenor.com/aRU6Zrm3LlQAAAAC/anime-cuteness.gif',
  'https://c.tenor.com/1qSJzP3BHqIAAAAd/anime-cute.gif',
  'https://c.tenor.com/EqrI4CB-grYAAAAC/anime-happy.gif',
  'https://c.tenor.com/gRzf7IcsGj8AAAAC/laugh-tale.gif',
  
  'https://c.tenor.com/fqRNsILmXHQAAAAC/anime-girl.gif',
  'https://c.tenor.com/QT7B-4g9hQwAAAAC/nagomi-yui-delicious-party-precure.gif',
  'https://tenor.com/view/cima-garahau-laugh-waifu-anime-girl-gif-19083486',
  'https://c.tenor.com/wOaXuM1UjAkAAAAC/suigintou-happy.gif',
  'https://c.tenor.com/M8HIZLaAO9QAAAAC/genshiken-ohno.gif',
  'https://c.tenor.com/CnHr_4hkdKkAAAAC/anime-laughing.gif',
  'https://c.tenor.com/QGUzjSX0oB4AAAAC/laughing-laugh.gif',
  'https://c.tenor.com/4Iogx5LSMjoAAAAC/anime-happy.gif',
  'https://c.tenor.com/FcGCiQ9nyMwAAAAC/ai-fyuumi-fuyuumi.gif',
  'https://c.tenor.com/dCiR4yyFZvkAAAAC/ai-fuyuumi-oreshura.gif',
  
  'https://c.tenor.com/gzrDHhHjIYcAAAAC/kitagawa-marin-beach.gif',
  'https://c.tenor.com/7ksO4mwLsf4AAAAC/ngakak-laugh.gif',
  'https://c.tenor.com/skm4CsAaDLQAAAAC/sailor-moon-laugh.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
