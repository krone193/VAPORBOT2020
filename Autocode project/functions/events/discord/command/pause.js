const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const voice = require('../../../../helpers/voicefunc.js');
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandPhrase = '`░P░a░u░s░i░n░g░,░ ░r░e░a░l░i░t░y░ ░n░e░e░d░s░ ░y░o░u░`\n';
const SuccessGif = 'https://c.tenor.com/QxWHvmM7JfYAAAAd/getting-up-anime.gif';

if (await voice.pause(`${context.params.event.guild_id}`, `${process.env.VOICE_CHANNEL_ID}`)) {
  await vapor.embedyttrack(
    context.params.event,
    '',
    CommandPhrase,
    null,
    SuccessGif,
    Number(`${process.env.EMBED_COLOUR}`)
  );
}
