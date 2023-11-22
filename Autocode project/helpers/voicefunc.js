const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const ytdl = require('ytdl-core' );
const fs = require('fs')
const vapor = require('../helpers/vaporfunc.js');

let BotOnVoiceChannel = false;

async function disconnect (guild) {
  await lib.discord.voice['@0.0.1'].channels.disconnect({
    guild_id: guild
  });
  BotOnVoiceChannel = false;
}

async function pause (guild, channel) {
  BotOnVoiceChannel = false;
  await lib.discord.voice['@0.0.1'].tracks.pause({
    guild_id: guild,
    channel_id: channel
  });
}

async function resume (guild, channel) {
  await lib.discord.voice['@0.0.1'].tracks.resume({
    guild_id: guild,
    channel_id: channel
  });
}

module.exports = {
  onvoicechanel: async () => {
    return BotOnVoiceChannel;
  },
  
  connectcallback: async () => {
    BotOnVoiceChannel = true;
  },

  disconnect: async (guild) => {
    BotOnVoiceChannel = false;
    try {
      await disconnect(guild);
    } catch (error) {
      return error;
    } finally {
      return true;
    }
  },
  
  play: async (event, ytlinks, voicechannel, phrase, successgif, errorphrase, errorgif) => {
    let exit = false;
    let retry = 0;
    let youtubelink = await vapor.randomcontent(ytlinks);
    let youtubethumbnail = 'https://img.youtube.com/vi/' + youtubelink.substring(youtubelink.search("=") + 1).replace('&t=1s', '') + '/0.jpg';
    let username = `${event.member.user.username}`;
    let usericon = `https://cdn.discordapp.com/avatars/${event.member.user.id}/${event.member.user.avatar}.png`;

    if (successgif == null) successgif = youtubethumbnail;

    if (BotOnVoiceChannel) {
      if (await pause(event.guid_id, voicechannel) == false) {
        disconnect(event.guild_id);
      }
    }

    while (1) {
      retry++;
      try {
        let downloadInfo = await ytdl.getInfo(`${youtubelink}`);
        await lib.discord.voice['@0.0.1'].tracks.play({
          channel_id: `${voicechannel}`,
          guild_id: `${event.guild_id}`,
          download_info: downloadInfo
        });
        await vapor.embedyttrack(
          event,
          '',
          phrase.concat(` ${downloadInfo.videoDetails.title}\n`),
          null,
          successgif,
          Number(`${process.env.EMBED_COLOUR}`)
        )
        return true;
      } catch (error) {
        if (retry >= Number(`${process.env.STREAM_MAX_RETRY}`)) {
          await vapor.embedyttrack(
            event,
            '',
            errorphrase,
            error + '\n',
            errorgif,
            Number(`${process.env.EMBED_COLOUR}`)
          )
          await disconnect(`${event.guild_id}`);
          return false;
        }
      } finally {
        return true;
      }
    }
  },
  
  pause: async (guild, channel) => {
    try {
      pause(guild, channel);
      return true;
    } catch (error) {
      return error;
    } finally {
      return true;
    }
  },
  
  resume: async (guild, channel) => {
    try {
      resume(guild, channel);
    } catch (error) {
      return error;
    } finally {
      return true;
    }
  }
}
