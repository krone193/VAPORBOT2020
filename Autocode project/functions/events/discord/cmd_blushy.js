const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'blushy';
const CommandDescription = "そんなことないです (so-nn-na-ko-to-na-i-de-su)";
const CommandContent = [
  'https://c.tenor.com/eT_HnoX8eKoAAAAC/happy-anime.gif',
  'https://c.tenor.com/voCLgP3672MAAAAC/anime-manga.gif',
  'https://c.tenor.com/vjgGw6IEFuUAAAAC/brilho-anime.gif',
  'https://c.tenor.com/-E4Y8d-JxL4AAAAC/soft-neko.gif',
  'https://c.tenor.com/uT9BWeRBJwYAAAAC/blushing-anime-girl.gif',
  'https://c.tenor.com/2cWyWrf4ucAAAAAC/cyan-hijirikawa-show-by-rock.gif',
  'https://c.tenor.com/hCqcNUuWCf0AAAAC/blush-anime.gif',
  'https://c.tenor.com/6NbEUdgkBq4AAAAC/smile-happy.gif',
  'https://c.tenor.com/Vu533jLjgw0AAAAC/shy-ughm.gif',
  'https://c.tenor.com/kEKQYGO0riUAAAAC/red-anime.gif',
  'https://c.tenor.com/4JBrfqDM83UAAAAC/smile-cute.gif',
  'https://c.tenor.com/e5GIh587OssAAAAC/anime-blushing.gif',
  'https://c.tenor.com/fapsneQ0NTkAAAAd/embarrassed-embarrasment.gif',
  'https://c.tenor.com/l-ItaKTK6hgAAAAC/miku-anime.gif'
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
