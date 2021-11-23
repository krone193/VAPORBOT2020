const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const MentionEmbed = [
  'Hello there!',
  "I'm a bot powered by raw A̸͎̦͒́̿ ̷͖̺̿̃Ḙ̶̅͌ ̸̻̬͍̐̕S̴͓̼̪͊ ̴̺̦̈́T̶͇̈̈́͝ ̵̦̊̿H̷̳̟̥̆̂̓ ̵̞̓̒E̸͔̻̭̋̔ ̶̲̻͆T̴̨̳̝͗ ̶̟̮̮̽Ị̷̜̯͋͗͠ ̷̢̛͎̭̿C̷̝͊̃ ̵̩̤̤̊̈́S̸̨͇̍.",
  'and pure ᑎOᔕTᗩᒪGIᗩ',
];

await lib.discord.channels['@0.0.6'].messages.create({
  channel_id: `${context.params.event.channel_id}`,
  content: '\n',
  embed: {
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
      url: `${process.env.MENTION_GIF}`,
    },
    thumbnail: {
      url: `${process.env.THUMBNAIL_PICTURE}`,
    }
  },
  tts: false
});
