const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const ytdl = require('ytdl-core');

const CommandName = 'explore_the_universe';
const CommandDescription = 'fasten your seatbelts and get ready for a ride across all galaxyes';
const CommandPhrase = '`░F░a░s░t░e░n░ ░y░o░u░r░ ░s░e░a░t░b░e░l░t░s░,░ ░r░i░d░e░r░:░ ░g░e░t░ ░r░e░a░d░y░ ░f░o░r░ ░l░i░f░t░ ░o░f░f░!░`\n';
const CommandContent = [
  'https://www.youtube.com/watch?v=3yOCk4Kn-Ss',
  'https://www.youtube.com/watch?v=oGWf8tQO__4',
  'https://www.youtube.com/watch?v=YP9nrR-ym3c',
  'https://www.youtube.com/watch?v=nQfBoWU3Nxw',
  'https://www.youtube.com/watch?v=9nRbuFtHywo',
  'https://www.youtube.com/watch?v=ea_UOPzuyZU'
]
const ErrorPhrase = 'You have to believe in yourself to survive in the Universe\n';

let youtubelink = CommandContent[Math.floor(Math.random() * CommandContent.length)];

await lib.discord.commands['@0.0.0'].create({
  guild_id: `${context.params.event.guild_id}`,
  name: CommandName,
  description: CommandDescription
});

try {
  await lib.discord.voice['@0.0.1'].channels.disconnect({
    guild_id: `${context.params.event.guild_id}`
  });
} catch (e) {}

try {
  let downloadInfo = await ytdl.getInfo(youtubelink);
  
  await lib.discord.voice['@0.0.1'].tracks.play({
    channel_id: `${process.env.VOICE_CHANNEL_ID}`,
    guild_id: `${context.params.event.guild_id}`,
    download_info: downloadInfo
  });
  
  await lib.discord.channels['@0.2.0'].messages.create({
    channel_id: `${context.params.event.channel_id}`,
    content: CommandPhrase.concat(` ${downloadInfo.videoDetails.title}\n`),
  });
} catch (e) {
  await lib.discord.channels['@0.2.0'].messages.create({
    channel_id: `${context.params.event.channel_id}`,
    content: ErrorPhrase,
  });
}
