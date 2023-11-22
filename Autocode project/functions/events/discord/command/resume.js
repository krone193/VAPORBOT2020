const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const voice = require('../../../../helpers/voicefunc.js');
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandPhrase = '`░R░e░s░u░m░i░n░g░,░ ░w░h░e░r░e░ ░w░e░r░e░ ░w░e░?░`\n';
const SuccessGif = 'https://c.tenor.com/s3lwSOIVsU4AAAAC/shiroi-suna-no-aquatope-the-aquatope-on-white-sand.gif';

if (await voice.resume(`${context.params.event.guild_id}`, `${process.env.VOICE_CHANNEL_ID}`)) {
  await vapor.embedyttrack(
    context.params.event,
    '',
    CommandPhrase,
    null,
    SuccessGif,
    Number(`${process.env.EMBED_COLOUR}`)
  );
}
