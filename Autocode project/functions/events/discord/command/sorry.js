const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/RNOB1JF8Br4AAAAC/sorry-crying.gif',
  'https://c.tenor.com/liqgmFIpRPkAAAAC/sad.gif',
  'https://c.tenor.com/V6XYNyS-Q4cAAAAC/reina-izumi.gif',
  'https://c.tenor.com/3iEVGwWyZbYAAAAC/anime-sorry.gif',
  'https://c.tenor.com/Gr-J0MjKtbcAAAAC/reina-izumi-sad.gif',
  'https://c.tenor.com/i9UkjLlNlt4AAAAC/anime-sorry.gif',
  'https://c.tenor.com/Tn9mzxqYNs4AAAAd/kukuru-misakino-anime.gif',
  'https://c.tenor.com/zakAfoTOysUAAAAC/remorseful-girl.gif',
  'https://c.tenor.com/kggqSoG5J64AAAAC/nagi-no.gif',
  'https://c.tenor.com/Q_l4jFzVOTUAAAAC/anime-shy.gif',
  
  'https://c.tenor.com/APIsjPJxtAUAAAAC/anime-sorry.gif',
  'https://c.tenor.com/lSwVx09EvFkAAAAC/jasorry-jaanime.gif',
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
