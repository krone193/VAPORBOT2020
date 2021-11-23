const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const ytdl = require('ytdl-core');

const CommandName = 'explore_dreams';
const CommandDescription = 'relax your mind, traveller. Let the dream machine run';
const CommandPhrase = '`░R░e░l░a░x░ ░y░o░u░r░ ░m░i░n░d░,░ ░t░r░a░v░e░l░l░e░r░:░ ░t░h░e░ ░d░r░e░a░m░ ░m░a░c░h░i░n░e░ ░i░s░ ░b░o░o░t░i░n░g░`\n';
const CommandContent = [
  'https://www.youtube.com/watch?v=yQBxKv9_2Sk',
  'https://www.youtube.com/watch?v=8P_RLKl2UNY',
  'https://www.youtube.com/watch?v=BgQXB-K-JE8',
  'https://www.youtube.com/watch?v=DVp544ddupo',
  'https://www.youtube.com/watch?v=6TEGPexTqr4'
];
const ErrorPhrase = 'You have to relax to ride the train of thoughts\n';

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
  let downloadInfo = await ytdl.getInfo(`${youtubelink}`);
  
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
