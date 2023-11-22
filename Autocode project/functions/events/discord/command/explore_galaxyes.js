const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const ytdl = require('ytdl-core');
const voice = require('../../../../helpers/voicefunc.js');

const CommandName = `explore_the_universe`;
const CommandDescription = `fasten your seatbelts and get ready for a ride across all galaxyes`;
const CommandSuccessPhrase = `░F░a░s░t░e░n░ ░y░o░u░r░ ░s░e░a░t░b░e░l░t░s░,░ ░r░i░d░e░r░:░ ░g░e░t░ ░r░e░a░d░y░ ░f░o░r░ ░l░i░f░t░ ░o░f░f░!░\n`;
const CommandSuccessGif = null;
const CommandErrorPhrase = `You have to believe in yourself to survive in the Universe\n`;
const CommandErrorGif = `https://c.tenor.com/6-oOTCHm_Y8AAAAC/depressed-anime.gif`;
const CommandContent = [
  'https://www.youtube.com/watch?v=oGWf8tQO__4',
  'https://www.youtube.com/watch?v=YP9nrR-ym3c',
  'https://www.youtube.com/watch?v=nQfBoWU3Nxw',
  'https://www.youtube.com/watch?v=9nRbuFtHywo',
  'https://www.youtube.com/watch?v=ea_UOPzuyZU',
  'https://www.youtube.com/watch?v=t1LguJbIF3I',
  'https://www.youtube.com/watch?v=YTRHBA7Ld0k',
  'https://www.youtube.com/watch?v=_AXIOfilxi0',
  'https://www.youtube.com/watch?v=E6ZKYrAi8NQ'
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
