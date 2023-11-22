const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const voicefunc = require('../../../../../helpers/voicefunc.js');

const CommandContent = [
  'https://c.tenor.com/VBiQ6Eo5ltcAAAAC/anime-music.gif',
  'https://c.tenor.com/XqarTGE4_d4AAAAd/liella-love-live.gif',
  'https://c.tenor.com/gaxGj7lADG8AAAAC/anime-girl-anime.gif',
  'https://c.tenor.com/IqAoS4pb2r0AAAAC/anime-music.gif',
  'https://c.tenor.com/0cMAX4Ljad8AAAAC/aimoto-rinku-d4dj-first-mix.gif',
  'https://c.tenor.com/gReZ1TkRFbEAAAAd/miku-nakano-go-toubun-no-hanayome.gif'
]

if (context.params.event.channel_id == `${process.env.MUSIC_CHANNEL_CIPOLLE}`) {
  if (context.params.event.member.user.username == `${process.env.BOT_NAME}`) voicefunc.connectcallback();
  if ((context.params.event.member.user.bot)) return;
  if (context.params.event.self_deaf && !context.params.event.self_mute) return;
  if (context.params.event.self_video && !context.params.event.self_mute) return;
  await lib.discord.channels['@0.2.2'].messages.create({
    channel_id: `${process.env.MUSIC_TEXT_CHANNEL_CIPOLLE}`,
    content: '\n',
    embed: {
      author: {
        name: `${context.params.event.member.user.username}`,
        icon_url: `https://cdn.discordapp.com/avatars/${context.params.event.member.user.id}/${context.params.event.member.user.avatar}.png`,
      },
      title: 'Reach out for your D̷̝̥̘̣̮̀͆̚͝Ŗ̵̊̀͌͗E̴̘̚̕A̴̦̺̪̎̇͗ͅM̵̡̛͎̗͖̉̈́̀̿ͅŚ̸̡̘̠͓̉`',
      description: `while listening to A̸͎̦͒́̿ ̷͖̺̿̃Ḙ̶̅͌ ̸̻̬͍̐̕S̴͓̼̪͊ ̴̺̦̈́T̶͇̈̈́͝ ̵̦̊̿H̷̳̟̥̆̂̓ ̵̞̓̒E̸͔̻̭̋̔ ̶̲̻͆T̴̨̳̝͗ ̶̟̮̮̽Ị̷̜̯͋͗͠ ̷̢̛͎̭̿C̷̝͊̃ ̵̩̤̤̊̈́ music`,
      color: Number(`${process.env.EMBED_COLOUR}`),
      image: {
        url: CommandContent[Math.floor(Math.random() * CommandContent.length)],
      },
      thumbnail: {
        url: `${process.env.THUMBNAIL_PICTURE}`,
      }
    }
  });
}
