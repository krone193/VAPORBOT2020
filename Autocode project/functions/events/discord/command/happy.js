const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/Fi5H8EfqtFAAAAAC/yay-yeah.gif',
  'https://c.tenor.com/11yz3HKByNYAAAAC/happy-anime.gif',
  'https://c.tenor.com/-dYzuY3XsU4AAAAC/happy-anime-happy.gif',
  'https://c.tenor.com/LMxwdxg5Ba8AAAAC/gabriel-dropout.gif',
  'https://media.giphy.com/media/KKB54xpucNE4M/giphy.gif',
  'https://media.giphy.com/media/PR3wumHIdsBhu/giphy.gif',
  'https://media.giphy.com/media/tX23iQaQYEcKI/giphy.gif',
  'https://media.giphy.com/media/cxPtMDHG8Ljry/giphy.gif',
  'https://i.kym-cdn.com/photos/images/original/001/202/123/bb4.gif',
  'https://c.tenor.com/6rrdak4Gu6oAAAAC/anime-girl.gif',
  
  'https://c.tenor.com/mKTS5nbF1zcAAAAd/cute-anime-dancing.gif',
  'https://c.tenor.com/0YpPpIrN0AIAAAAC/anime-girl.gif',
  'https://c.tenor.com/qDo_bNq100UAAAAd/cyan-cyan-hijirikawa.gif',
  'https://c.tenor.com/j3j7xWQq6JAAAAAC/excited-anime.gif',
  'https://c.tenor.com/y5e5UzxbmtkAAAAC/zero-two.gif',
  'https://c.tenor.com/m90Q1qgMbAsAAAAC/zero-two-darling-zero-two.gif',
  'https://c.tenor.com/DVbymBMiCtoAAAAC/omg-happy.gif',
  'https://c.tenor.com/beNfnN65kHQAAAAC/yay-excited.gif',
  'https://c.tenor.com/t-3aFcNhMfIAAAAC/toradora-taiga-excited.gif',
  'https://c.tenor.com/QkQOrEEGsAAAAAAC/animu-anime.gif',
  
  'https://c.tenor.com/35MQTGdC3oAAAAAC/mari-cheer.gif',
  'https://c.tenor.com/ufRspWK10iIAAAAC/charlotte-sharotto.gif',
  'https://c.tenor.com/W2ho7L2F7VEAAAAC/yume-nijino-aikatsu-stars.gif',
  'https://c.tenor.com/pO2h1B_Lk1wAAAAC/anime-girl.gif',
  'https://c.tenor.com/dT2vlcBLUu4AAAAC/shikimori-shikimoris-not-just-cute.gif',
  'https://c.tenor.com/6ZEEhhxHyu8AAAAC/animehappy-shy.gif',
  'https://c.tenor.com/sE3FzUTEnl8AAAAC/kyoko-toshino.gif',
  'https://c.tenor.com/tZuynAi5avIAAAAC/i-love-you.gif',
  'https://c.tenor.com/fQkZ4o3emwgAAAAC/happy-good.gif',
  'https://c.tenor.com/U94nuh9Tvd4AAAAC/joshiraku-girl.gif',
  
  'https://c.tenor.com/tLFc6lDha_EAAAAC/anime-girl.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
