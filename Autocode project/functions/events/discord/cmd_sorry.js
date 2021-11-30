const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'sorry';
const CommandDescription = "don't be proud and say you're sorry, maybe everything will be over with an head pat";
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
  'https://c.tenor.com/Q_l4jFzVOTUAAAAC/anime-shy.gif'
]

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
