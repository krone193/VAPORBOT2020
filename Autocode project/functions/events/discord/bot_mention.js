const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const MentionEmbed = [
  'Hello there!',
  "I'm a bot powered by raw A̸͎̦͒́̿ ̷͖̺̿̃Ḙ̶̅͌ ̸̻̬͍̐̕S̴͓̼̪͊ ̴̺̦̈́T̶͇̈̈́͝ ̵̦̊̿H̷̳̟̥̆̂̓ ̵̞̓̒E̸͔̻̭̋̔ ̶̲̻͆T̴̨̳̝͗ ̶̟̮̮̽Ị̷̜̯͋͗͠ ̷̢̛͎̭̿C̷̝͊̃ ̵̩̤̤̊̈́S̸̨͇̍.",
  'and pure ᑎOᔕTᗩᒪGIᗩ',
];

const OldMentionGif = 'https://thumbs.gfycat.com/CourteousUnfoldedAntlion-max-1mb.gif';
const OldThumbnailImg = 'https://cutewallpaper.org/22/retro-wave-anime-girl-wallpapers/3136919788.jpg';

if (context.params.event.content.match(`@`)) {
  await lib.discord.channels['@0.0.6'].messages.create({
    channel_id: `${context.params.event.channel_id}`,
    content: '\n',
    embed: {
      author: {
        name: `${context.params.event.author.username}`,
        icon_url: `https://cdn.discordapp.com/avatars/${context.params.event.author.id}/${context.params.event.author.avatar}.png`,
      },
      title: '【﻿Ｖ Ａ Ｐ Ｏ Ｒ Ｂ Ｏ Ｔ ２ ０ ２ ０】',
      type: 'rich',
      color: Number(`${process.env.EMBED_COLOUR}`),
      description: MentionEmbed.join('\n'),
      fields: [{
        name: 'v'.concat(`${process.env.BOT_VERSION}`),
        value: [
          'phase: '.concat(`${process.env.BOT_PHASE}`),
        ].join('\n')
      }],
      image: {
        url: `${process.env.MENTION_GIF}`
      },
      thumbnail: {
        url: `${process.env.THUMBNAIL_PICTURE}`
      }
    },
    tts: false
  });
}
