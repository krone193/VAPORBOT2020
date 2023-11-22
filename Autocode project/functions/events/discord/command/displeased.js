const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/G_YeALOH-iAAAAAC/mao-amatsuka-mad.gif',
  'https://c.tenor.com/Ln-j0vBojk0AAAAC/pouty-anime.gif',
  'https://c.tenor.com/Jj7RpBC7U_AAAAAC/anime-girl.gif',
  'https://c.tenor.com/7dWlqDyO8wYAAAAC/anime-angry.gif',
  'https://c.tenor.com/eSiR-TcUZqgAAAAC/oniai-anastasia-nasuhara.gif',
  'https://c.tenor.com/wYBkuol2tGYAAAAC/anime-girl.gif',
  'https://c.tenor.com/cc1EzfBVr4oAAAAC/yandere-tagged.gif',
  'https://c.tenor.com/iRcsL7dOStMAAAAC/anime-beat.gif',
  'https://c.tenor.com/ZLEOf9jtiXUAAAAC/anime-girl.gif',
  'https://c.tenor.com/pS7NXIeIhkoAAAAC/anime-mad.gif',
  
  'https://c.tenor.com/_yoOkigNCyEAAAAC/annoyed-chrome-shelled-regios.gif',
  'https://c.tenor.com/RzzMIcmEuD4AAAAC/anime-twitching.gif',
  'https://c.tenor.com/lut1_cT745oAAAAC/anime-knife.gif',
  'https://c.tenor.com/bMF2vEGS_GoAAAAC/anime-annoyed.gif',
  'https://c.tenor.com/DJk8RI8ZLvQAAAAC/angry-mad.gif',
  'https://c.tenor.com/NpG1XpDq0ncAAAAC/cute-angry.gif',
  'https://c.tenor.com/SCObc5XBXAsAAAAC/shikimori-shikimori-not-just-cute.gif',
  'https://c.tenor.com/2hJu9gEGq9sAAAAC/shikimori-angry.gif',
  'https://c.tenor.com/oeVwCt6fPGUAAAAC/002-zero.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
