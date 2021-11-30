const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'happy';
const CommandDescription = "it's always nice to share your good vibes";
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
  'https://c.tenor.com/1rePypkwoOYAAAAd/miku-nakano-miku.gif'
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
