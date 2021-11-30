const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'displeased';
const CommandDescription = "dude, uncool";
const CommandContent = [
  'https://c.tenor.com/G_YeALOH-iAAAAAC/mao-amatsuka-mad.gif',
  'https://c.tenor.com/Ln-j0vBojk0AAAAC/pouty-anime.gif',
  'https://c.tenor.com/Jj7RpBC7U_AAAAAC/anime-girl.gif',
  'https://c.tenor.com/7dWlqDyO8wYAAAAC/anime-angry.gif',
  'https://c.tenor.com/eSiR-TcUZqgAAAAC/oniai-anastasia-nasuhara.gif',
  'https://c.tenor.com/wYBkuol2tGYAAAAC/anime-girl.gif',
  'https://c.tenor.com/cc1EzfBVr4oAAAAC/yandere-tagged.gif',
  'https://c.tenor.com/iRcsL7dOStMAAAAC/anime-beat.gif',
  'https://c.tenor.com/ZLEOf9jtiXUAAAAC/anime-girl.gif'
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
