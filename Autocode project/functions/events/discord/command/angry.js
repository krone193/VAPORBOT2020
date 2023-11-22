const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/X3x3Y2mp2W8AAAAC/anime-angry.gif',
  'https://c.tenor.com/ikKAd57zDEwAAAAd/anime-mad.gif',
  'https://c.tenor.com/b76QnX1XVAcAAAAC/raiva-anime.gif',
  'https://c.tenor.com/jgFVzr3YeJwAAAAC/date-a-live-rage.gif',
  'https://c.tenor.com/qEJW8nS5aJEAAAAd/anime-girl.gif',
  'https://c.tenor.com/oxqylurVQmkAAAAC/touken-angry.gif',
  'https://c.tenor.com/u7pzpX6_Q5cAAAAC/anime-girl.gif',
  'https://c.tenor.com/7te6q4wtcYoAAAAC/mad-angry.gif',
  'https://c.tenor.com/MLsVzlSceaEAAAAC/anime-angry.gif',
  'https://c.tenor.com/IWKYIP6AMIgAAAAd/miku-nakano-the-quintessential-quintuplets.gif',
  
  'https://c.tenor.com/W7rxNeKBCRgAAAAC/darling-in-the-franxx-zero-two.gif',
  'https://c.tenor.com/DBWQXu6NKw0AAAAC/yor-yor-forger.gif',
  'https://c.tenor.com/YQ08ifsOb0EAAAAC/anime-angry.gif',
  'https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif',
  'https://c.tenor.com/vlgbPz0EA5MAAAAC/anime-darling.gif',
  'https://c.tenor.com/FR_k6CO0aicAAAAC/kopa22-anime.gif',
  'https://c.tenor.com/sIBmF8vS9xgAAAAC/joshiraku-hit.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
