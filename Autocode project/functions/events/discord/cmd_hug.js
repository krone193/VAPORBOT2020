const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const CommandName = 'hug';
const CommandDescription = "everyone wants one, don't be shy";
const CommandContent = [
  'https://c.tenor.com/pYzpQgkAQJkAAAAC/violet-evergarden-hug.gif',
  'https://c.tenor.com/FJaQ1MKAtowAAAAd/idk-what-anime-this-is-from-but-its-anime-girls-hugging.gif',
  'https://c.tenor.com/3ergzHiRIBwAAAAC/hug-cuddle.gif',
  'https://c.tenor.com/2tStVop0CowAAAAC/lindo-adorable.gif',
  'https://c.tenor.com/xoZfAA2Rz1oAAAAC/anime-manga.gif',
  'https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif',
  'https://c.tenor.com/Pd2sMiVr09YAAAAC/hug-anime-hug.gif',
  'https://c.tenor.com/UhcyGsGpLNIAAAAC/hug-anime.gif',
  'https://c.tenor.com/zEz00ZxujqMAAAAC/blush-hug.gif',
  'https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif',
  'https://c.tenor.com/0vl21YIsGvgAAAAC/hug-anime.gif',
  'https://c.tenor.com/keasv-Cnh4kAAAAd/hug-cuddle.gif',
  'https://acegif.com/wp-content/gif/anime-hug-91.gif'
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
