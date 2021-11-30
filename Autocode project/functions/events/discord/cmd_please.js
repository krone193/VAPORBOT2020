const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'please';
const CommandDescription = "you can't resist those pretty eyes, can you?";
const CommandContent = [
  'https://c.tenor.com/j-mVhVzhSAYAAAAC/anime-cry.gif',
  'https://c.tenor.com/AawIsMGnR88AAAAC/llorar1-cry.gif',
  'https://c.tenor.com/-bXrej4rT3cAAAAC/anime-girl.gif',
  'https://i.kym-cdn.com/photos/images/newsfeed/000/967/856/9cf.gif',
  'https://data.whicdn.com/images/326326292/original.gif'
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
