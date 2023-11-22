const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const ytdl = require('ytdl-core');
const voice = require('../../../../helpers/voicefunc.js');

const CommandName = `rainy_mood`;
const CommandDescription = `allow the dream machine to lull your sorrow`;
const CommandSuccessPhrase = `░B░e░ ░a░t░ ░e░a░s░e░, ░I░ ░w░i░l░l░ ░t░a░k░e░ ░c░a░r░e░ ░o░f░ ░y░o░u░\n`;
const CommandSuccessGif = `https://c.tenor.com/UOu5DnxHRUYAAAAC/sad-anime.gif`;
const CommandErrorPhrase = `It never rains but it pours\n`;
const CommandErrorGif = `https://c.tenor.com/6-oOTCHm_Y8AAAAC/depressed-anime.gif`;
const CommandContent = [
  'https://www.youtube.com/watch?v=WnFs85pLmj4',    // Arthur Rubinstein - Chopin Nocturne Op. 9, No. 1 in B flat
  'https://www.youtube.com/watch?v=Nu48Z45ibxQ',    // Arthur Rubinstein - Chopin Nocturne Op. 9, No. 2 in E flat
  'https://www.youtube.com/watch?v=sx31YcLXAug',    // Arthur Rubinstein - Chopin Nocturne Op. 9, No. 3 in B
  'https://www.youtube.com/watch?v=waoKj8tAb7A',    // Arthur Rubinstein - Chopin Nocturne Op. 15, No. 1 in F
  'https://www.youtube.com/watch?v=L1w2_2WG5q4',    // Arthur Rubinstein - Chopin Nocturne Op. 15, No. 3 in G
  'https://www.youtube.com/watch?v=8lvNjO3TQAA',    // Arthur Rubinstein - Chopin Nocturne Op. 27, No. 1 in C sharp
  'https://www.youtube.com/watch?v=U92QEmtR63E',    // Arthur Rubinstein - Chopin Nocturne Op. 32, No. 1 in B
  'https://www.youtube.com/watch?v=ttLRonyyMak',    // Arthur Rubinstein - Chopin Nocturne Op. 32, No. 2 in A flat
  'https://www.youtube.com/watch?v=ymouzrzzgZ0',    // Arthur Rubinstein - Chopin Nocturne Op. 37, No. 2 in G
  'https://www.youtube.com/watch?v=h_vZtpjNKVE',    // Arthur Rubinstein - Chopin Nocturne Op. 48, No. 1 in C minor
  'https://www.youtube.com/watch?v=nqEk73LvnzQ',    // Arthur Rubinstein - Chopin Nocturne Op. 48, No. 2 in F sharp minor
  'https://www.youtube.com/watch?v=NONg06Pf0v8',    // Arthur Rubinstein - Chopin Nocturne Op. 55, No. 1 in F Minor
  'https://www.youtube.com/watch?v=MyVFBkHepRw',    // Arthur Rubinstein - Chopin Nocturne Op. 55, No. 2 in E flat
  'https://www.youtube.com/watch?v=2oYaEHzn6Kg',    // Arthur Rubinstein - Chopin Nocturne Op. 62, No. 1 in B
  'https://www.youtube.com/watch?v=zf8YUL_jlF0',    // Arthur Rubinstein - Chopin Nocturne Op. 62, No. 2 in E
  'https://www.youtube.com/watch?v=vJpAIOFN5WQ',    // Arthur Rubinstein - Chopin Nocturne Op. 72, No. 1 in E minor
  'https://www.youtube.com/watch?v=FyuQMTkdFaU',    // Sontag Shogun - The Things We Let Fall Apart
  'https://www.youtube.com/watch?v=_u3l7Dd_WDc',    // Sontag Shogun - It Billows Up
  'https://www.youtube.com/watch?v=tC1DjgbVYY0',    // Sontag Shogun - no.7 (Scattered Bits)
  'https://www.youtube.com/watch?v=-C7ZsVuG2fY',    // Sontag Shogun - Lament
  'https://www.youtube.com/watch?v=c6f4lJVwMs8',    // Sontag Shogun - The Thunderswan
];

let VoiceChannel;

if (context.params.event.guild_id == process.env.GUID_CIPOLLE) {
  VoiceChannel = `${process.env.MUSIC_CHANNEL_CIPOLLE}`;
} else {
  VoiceChannel = `${process.env.MUSIC_CHANNEL_FREN}`;
}

await voice.play(
  context.params.event,
  CommandContent,
  VoiceChannel,
  CommandSuccessPhrase,
  CommandSuccessGif,
  CommandErrorPhrase,
  CommandErrorGif
);
