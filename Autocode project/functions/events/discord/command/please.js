const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/j-mVhVzhSAYAAAAC/anime-cry.gif',
  'https://c.tenor.com/AawIsMGnR88AAAAC/llorar1-cry.gif',
  'https://c.tenor.com/-bXrej4rT3cAAAAC/anime-girl.gif',
  'https://i.kym-cdn.com/photos/images/newsfeed/000/967/856/9cf.gif',
  'https://data.whicdn.com/images/326326292/original.gif',
  'https://c.tenor.com/KJssr8kEMGcAAAAC/anime-girl.gif'
]

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
