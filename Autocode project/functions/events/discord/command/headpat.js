const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/YGQYQKrSsCIAAAAC/anime-pat.gif',
  'https://c.tenor.com/OUSrLXimAq8AAAAC/head-pat-anime.gif',
  'https://c.tenor.com/g_61F9hKhV4AAAAC/pat-head-pat.gif',
  'https://c.tenor.com/Wth7fEpgZ7EAAAAC/neko-anime-girl.gif',
  'https://c.tenor.com/lnoDyTqMk24AAAAC/anime-anime-headrub.gif',
  'https://c.tenor.com/oZ-sZLLPf0QAAAAC/pat-anime.gif',
  'https://c.tenor.com/dLdNYQrLsp4AAAAC/umaru-frown.gif',
  'https://c.tenor.com/jEfC8cztigIAAAAC/anime-pat.gif',
  'https://c.tenor.com/JWx5wmF6bqAAAAAC/charlotte-pat.gif',
  'https://c.tenor.com/tYS5DBIos-UAAAAd/kyo-ani-musaigen.gif',
  
  'https://c.tenor.com/6dLDH0npv6IAAAAC/nogamenolife-shiro.gif',
  'https://c.tenor.com/Fxku5ndWrN8AAAAC/head-pat-anime.gif',
  'https://c.tenor.com/TRxNL32jtEIAAAAC/anime-pat.gif',
  'https://c.tenor.com/EtvotzSToyMAAAAd/petra-rezero.gif',
  'https://c.tenor.com/RDfGm9ftwx0AAAAC/anime-pat.gif',
  'https://c.tenor.com/SONjh216O60AAAAC/pat-head-anime.gif',
  'https://c.tenor.com/2x1pihH4hUgAAAAC/anime-pat.gif',
  'https://c.tenor.com/PNauZOtjW-oAAAAC/anime-cute.gif',
  'https://c.tenor.com/9R7fzXGeRe8AAAAC/fantasista-doll-anime.gif',
  'https://c.tenor.com/zBPha3hhm7QAAAAC/anime-girl.gif',
  
  'https://c.tenor.com/g75K3KA3VeAAAAAd/anime-sleep.gif',
  'https://c.tenor.com/edHuxNBD6IMAAAAC/anime-head-pat.gif',
  'https://c.tenor.com/Y7B6npa9mXcAAAAC/rikka-head-pat-pat-on-head.gif',
  'https://c.tenor.com/FHWa_rEd4IAAAAAC/anime-headpats.gif',
  'https://c.tenor.com/Dps8ADQJ3RgAAAAC/fuuka-miyazawa-kukuru-misakino.gif',
  'https://c.tenor.com/YaFzR7EkabYAAAAC/head-pat-anime.gif',
  'https://c.tenor.com/G2dlcQAz87sAAAAC/happy-anime.gif',
  'https://c.tenor.com/3zhdZLyAl6EAAAAC/pat.gif',
  'https://c.tenor.com/G14pV-tr0NAAAAAC/anime-head.gif',
  'https://c.tenor.com/je7KbiyjaWgAAAAC/head-pats-anime.gif',
  
  'https://c.tenor.com/Jj-vHGZOgT4AAAAC/anime-anime-girl.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
