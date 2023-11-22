/*----------------------------------------------------------------------------*/
/*--- Required libraries and files -------------------------------------------*/
/*----------------------------------------------------------------------------*/
const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});


/*----------------------------------------------------------------------------*/
/*--- Internal functions -----------------------------------------------------*/
/*----------------------------------------------------------------------------*/
async function extractusername (event) {
  return `${event.member.user.username}`;
}
/*----------------------------------------------------------------------------*/
async function extractusericon (event) {
  return `https://cdn.discordapp.com/avatars/${event.member.user.id}/${event.member.user.avatar}.png`;
}
/*----------------------------------------------------------------------------*/
async function messagecreate (channel, content, embed) {
  await lib.discord.channels['@0.2.0'].messages.create({
    channel_id: channel,
    content: content + '\n',
    embed: embed
  });
}
/*----------------------------------------------------------------------------*/
async function randomcontent (content) {
  let rCycles = Math.floor(Math.random() * content.length);
  let rSumval;
  let rIndex;
  for (i = 0; i < rCycles; i++) {
    rSumval = Math.floor(Math.random() * content.length);
  }
  rIndex = (Math.floor(Math.random() * content.length)) + rSumval;
  if (rIndex >= content.length) rIndex -= content.length;
  return content[rIndex];
}

/*----------------------------------------------------------------------------*/
/*--- Callable functions -----------------------------------------------------*/
/*----------------------------------------------------------------------------*/
module.exports = {
  /* sendgif function
   * event:       context's event generated from Discord
   * content:     array with gif's links
   * embed:       use VAPORBOT2020 embedded gif style
   * colour:      specify the colour of the embed (nullable if embed is false)
   */
  sendgif: async (event, content, embed, colour) => {
    if (embed) {
      await messagecreate(
        `${event.channel_id}`,
        '',
        {
          author: {
            name: await extractusername(event),
            icon_url: await extractusericon(event),
          },
          title: '',
          color: colour,
          image: { url: await randomcontent(content) }
        }
      );
    } else {
      await messagecreate(
        `${event.channel_id}`,
        await randomcontent(content),
        null
      );
    }
  },
  /* embedyttrack function
   * event:       context's event generated from Discord
   * content:     optional message to display
   * title:       embed title
   * description: embed description
   * imageurl:    image to embed
   * colour:      specify the colour of the embed (nullable if embed is false)
   */
  embedyttrack: async (event, content, title, description, imageurl, colour) => {
    await messagecreate(
      `${event.channel_id}`,
      content,
      {
        author: {
          name: await extractusername(event),
          icon_url: await extractusericon(event),
        },
        title: title,
        description: description,
        color: colour,
        image: { url: imageurl }
      }
    );
  },
  /* randomcontent function
   * content: array from which extract an element
   */
  randomcontent: async (content) => {
    return await randomcontent(content);
  },
  /* delay function
   * time: milliseconds to wait
   */
  delay: async (time) => {
    return new Promise(resolve => setTimeout(resolve, time));
  },
  /* debugmsg function
   * event:       context's event generated from Discord
   * content:     plain text
   */
  debugmsg: async (content) => {
    await messagecreate(
      `${process.env.DEBUG_CHANNEL}`,
      content,
      null
    );
  },
}
