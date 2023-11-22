const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
//'https://c.tenor.com/iDy78BQ8324AAAAC/anime-smell.gif',
  'https://c.tenor.com/OQsdGc_qxyQAAAAC/anime-tea.gif',
  'https://c.tenor.com/2ztTxOV470gAAAAC/anime.gif',
  'https://c.tenor.com/j7eopdA1o1QAAAAC/k-on-azusa.gif'
]

context.params.event.channel_id = `${process.env.CIPOLLE_COFFEE_CHANNEL}`;

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
