const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'smile';
const CommandDescription = "kind people are always my kind of people";
const CommandContent = [
  'https://c.tenor.com/U1p83COiAPYAAAAC/anime-happy-anime-smile.gif',
  'https://c.tenor.com/6x5NsgRFxFUAAAAC/animegirl-anime.gif',
  'https://c.tenor.com/nuKmYDgaDpAAAAAC/anime-smile.gif',
  'https://c.tenor.com/Vtjibw10S4AAAAAC/cute-smiling.gif',
  'https://c.tenor.com/IyKy95tPdNgAAAAC/smiling-thinking.gif',
  'https://animesher.com/orig/0/99/997/9970/animesher.com_anime-girl-happy-anime-girl-gif-hyouka-997030.gif',
  'https://images6.fanpop.com/image/photos/38400000/Cute-anime-girl-blushing-anime-38465673-500-275.gif',
  'https://data.whicdn.com/images/327605476/original.gif',
  'https://c.tenor.com/xHbq3PpKgiEAAAAC/phone-cellphone.gif',
  'https://c.tenor.com/DbRVEHMsm-YAAAAC/yoruka-smile-yoruka.gif',
  'https://c.tenor.com/P6Cih-37NKAAAAAC/anime-girl.gif',
  'https://c.tenor.com/rGhny9QnU5EAAAAC/anime-girl.gif',
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
