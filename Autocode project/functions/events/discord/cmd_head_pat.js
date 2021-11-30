const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'head_pat';
const CommandDescription = "zai deserves all the head pats in the world";
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
  'https://c.tenor.com/PNauZOtjW-oAAAAC/anime-cute.gif'
];

await lib.discord.commands['@0.0.0'].create({
  guild_id: `${context.params.event.guild_id}`,
  name: CommandName,
  description: CommandDescription
});

await lib.discord.channels['@0.2.0'].messages.create({
  channel_id: `${context.params.event.channel_id}`,
  content: '\n',
  embed: {
    title: '\n',
    description: `<@!${context.params.event.member.user.id}>`,
    color: Number(`${process.env.EMBED_COLOUR}`),
    image: {
      url: CommandContent[Math.floor(Math.random() * CommandContent.length)],
    }
  }
});
