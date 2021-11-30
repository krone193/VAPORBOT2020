const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'opsy';
const CommandDescription = "we all sometimes do some silly things";
const CommandContent = [
  'https://c.tenor.com/sjUvV_MMDksAAAAC/anime-girl.gif',
  'https://c.tenor.com/APIsjPJxtAUAAAAC/anime-sorry.gif',
  'https://c.tenor.com/lSwVx09EvFkAAAAC/jasorry-jaanime.gif',
  'https://c.tenor.com/q6vmV7JzZaAAAAAd/anime-oops-my-fault.gif'
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
