const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

try {
  BotOnVoiceChannel = false;
  await lib.discord.voice['@0.0.1'].channels.disconnect({
    guild_id: `${context.params.event.guild_id}`
  });
} catch (e) {}
