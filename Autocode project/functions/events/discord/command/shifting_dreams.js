const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const ytdl = require('ytdl-core');
const voice = require('../../../../helpers/voicefunc.js');

const CommandName = `shifting_dreams`;
const CommandDescription = `relax your mind, traveller. Let the dream machine run`;
const CommandSuccessPhrase = `░R░e░l░a░x░ ░y░o░u░r░ ░m░i░n░d░,░ ░t░r░a░v░e░l░l░e░r░:░ ░t░h░e░ ░d░r░e░a░m░ ░m░a░c░h░i░n░e░ ░i░s░ ░b░o░o░t░i░n░g░\n`;
const CommandSuccessGif = null;
const CommandErrorPhrase = `You have to relax to ride the train of thoughts\n`;
const CommandErrorGif = `https://c.tenor.com/6-oOTCHm_Y8AAAAC/depressed-anime.gif`;
const CommandContentList = [
  'https://www.youtube.com/watch?v=BgQXB-K-JE8',  // SIXTHCLONE - Beats to get LOST in Space
  'https://www.youtube.com/watch?v=DVp544ddupo',  // SIXTHCLONE - Ins0mnia™ (不眠症) // OFFICIAL VIDEO
  'https://www.youtube.com/watch?v=lAPGtQN46lE',  // SIXTHCLONE - Rimini Okinawa™ // OFFICIAL VIDEO
  'https://www.youtube.com/watch?v=Ao2KofI8RsA',  // SIXTHCLONE - Timeless™ [タイムレス] // OFFICIAL VIDEO
  'https://www.youtube.com/watch?v=fzU0db_F100',  // SIXTHCLONE - The Last Day
  'https://www.youtube.com/watch?v=9nRbuFtHywo',  // SIXTHCLONE - ＣＯＳＴＡＮＺＯ／ＷＡＶＥ™ [コスタンツォ]
  'https://www.youtube.com/watch?v=nQfBoWU3Nxw',  // SIXTHCLONE - Ьim.Ьum.Ьam(Ь).™ 「公式ビデオ」 // OFFICIAL VIDEO
  'https://www.youtube.com/watch?v=QdopZ6jlqVI',  // SIXTHCLONE - Parliamo di ビデオゲーム
  'https://www.youtube.com/watch?v=ZYj5WnhoIUw',  // SIXTHCLONE - [*] .ｈａｎａｂｉ.txt
  'https://www.youtube.com/watch?v=bXT5kC7-mpE',  // SIXTHCLONE - M Ø N S T E R 「お化け」- Official Video
  'https://www.youtube.com/watch?v=nSk8S2m4qtk',  // SIXTHCLONE - _Beautiful1987.ｔｏｒｒｅｎｔ
  'https://www.youtube.com/watch?v=oZ71RokWFNs',  // SIXTHCLONE - Eroi di un Sogno™ (ビデオ) // OFFICIAL VIDEO
  'https://www.youtube.com/watch?v=jEOnbNzYbIM',  // SIXTHCLONE - __error.gif
  'https://www.youtube.com/watch?v=0Ft7Q_TrjFY',  // SIXTHCLONE - ｃｈａｔ 1999 [広告]
];

let CommandContent = [];
let VoiceChannel;
let UserSelection = Number(context.params.event.data.options[0].value);

if (UserSelection > CommandContentList.length) {
  CommandContent = CommandContentList;
} else {
  CommandContent[0] = CommandContentList[UserSelection];
}

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
return true;
