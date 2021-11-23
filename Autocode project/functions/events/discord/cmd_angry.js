const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'angry';
const CommandDescription = "let me show 'em how pissed off you are";
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
  'https://c.tenor.com/IWKYIP6AMIgAAAAd/miku-nakano-the-quintessential-quintuplets.gif'
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
