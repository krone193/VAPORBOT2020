const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'sad';
const CommandDescription = "sometimes life's hard, allow me to embrace and convey your feelings";
const CommandContent = [
  'https://64.media.tumblr.com/c75a7492ed6153828ccfea76ab659cae/tumblr_pwnqrr3v2M1yqkoyvo1_500.gif',
  'https://c.tenor.com/ESe9mqJlywkAAAAC/anime-girl.gif',
  'https://c.tenor.com/EizBjV8lOFUAAAAd/sad-girl.gif',
  'https://c.tenor.com/PHBzhcOds5oAAAAC/lonely-windy.gif',
  'https://c.tenor.com/AY7ipPod8eQAAAAC/anime-alone.gif',
  'https://c.tenor.com/zAlabxg7g3UAAAAd/anime-sad.gif',
  'https://c.tenor.com/dznqHVbWPlUAAAAC/in-the-rain-sad-story.gif',
  'https://cdn40.picsart.com/174293536000202.gif?to=crop&type=webp&r=-1x-1&q=95',
  'https://c.tenor.com/VTqa0X2W6LUAAAAC/80s-running.gif',
  'https://c.tenor.com/Mlgi6bkVkG8AAAAC/emotional-cry.gif',
  'https://c.tenor.com/Foyauwn9foIAAAAC/crying-anime.gif'
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
