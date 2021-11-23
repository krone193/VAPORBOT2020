const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

const GifDaUtilizzare = [
  'https://animesher.com/orig/1/118/1189/11893/animesher.com_gif-kawaii-girl-1189328.gif',
  'https://c.tenor.com/e5wqsfGmy2IAAAAC/anime-aesthetic.gif'
]

let guilds = await lib.discord.guilds['@0.0.6'].list({
  limit: 100
});

let channels = await lib.discord.guilds['@0.0.6'].channels.list({
  guild_id: guilds[0].id
});

let generalChannel = channels.find((channel) => {
  return channel.name === 'general';
});

if (generalChannel) {
  let botInfo = await lib.discord.users['@0.0.6'].me.list();
  await lib.discord.channels['@0.0.6'].messages.create({
    channel_id: generalChannel.id,
    content: [
      `Hello there, wait just a moment please, I'm still finishing to prepare myself`
    ].join('\n')
  });
  await lib.discord.channels['@0.0.6'].messages.create({
    channel_id: generalChannel.id,
    content: [
      GifDaUtilizzare[1]
    ].join('\n')
  });
  await lib.discord.channels['@0.0.6'].messages.create({
    channel_id: generalChannel.id,
    content: [
      `I'm ready in all my A̸͎̦͒́̿ ̷͖̺̿̃Ḙ̶̅͌ ̸̻̬͍̐̕S̴͓̼̪͊ ̴̺̦̈́T̶͇̈̈́͝ ̵̦̊̿H̷̳̟̥̆̂̓ ̵̞̓̒E̸͔̻̭̋̔ ̶̲̻͆T̴̨̳̝͗ ̶̟̮̮̽Ị̷̜̯͋͗͠ ̷̢̛͎̭̿C̷̝͊̃ ̵̩̤̤̊̈́S̸̨͇̍.`
    ].join('\n')
  });
}