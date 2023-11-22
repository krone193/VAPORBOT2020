/* Origin     : VAPORBOT2020
 * File name  : hourly.js
 * Webhook    : Scheduler - Once an hour
 * Author     : krone
 */

/**
 * An example typed API that generates a hello world message
 *   Read more about typing at: https://github.com/acode/functionscript
 * @param {string} name The name to say hello to
 * @param {integer} count The number of times to say hello
 * @returns {object} body
 * @ {array} messages A list of messages
 */
const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../helpers/vaporfunc.js');


const CommandContent = [
  'https://c.tenor.com/Rf5v6glMta8AAAAC/hey-waves.gif'
]


function LastSunday (year, month) {
  var date = new Date(year,month,1,12);
  let dayDiff = date.getDay() == 0 ? 7 : date.getDay();
  date.setDate(date.getDate() - dayDiff);
  return date;
}

function DaylightSaving (date, legal, solar) {
  let month = date.getMonth() + 1;
  // Apr, May, Jun, Jul, Aug, Sept
  if (month > 3 && month < 10) date.setHours(date.getHours() + 2);
  // Jan, Feb, Nov, Dec
  else if (month < 3 || month - 10 > 0) date.setHours(date.getHours() + 1);
  // Mar
  else if (month == 3) date.getDate() < legal.getDate() ? date.setHours(date.getHours() + 1) : date.setHours(date.getHours() + 2);
  // Oct
  else if (month == 10) date.getDate() < solar.getDate() ? date.setHours(date.getHours() + 2) : date.setHours(date.getHours() + 1);
}


var currentdate = new Date();
var legalstart  = LastSunday(currentdate.getFullYear(), 3);    // last sunday of March
var solarstart  = LastSunday(currentdate.getFullYear(), 10);    // last sunday of October


DaylightSaving(currentdate, legalstart, solarstart);      // adjust currentdate to local italian time
if (currentdate.getDay() > 0 && currentdate.getDay() < 6) {
  // working day start
  if (currentdate.getHours() == 8 && currentdate.getMinutes() == 00) {
    await lib.discord.channels['@0.2.0'].messages.create({
      channel_id: `${process.env.CIPOLLE_GENERAL_CHANNEL}`,
      content: '@everyone',
      embed: {
        title: "°˖✧◝(⁰▿⁰)◜✧˖°  H E L L O  °˖✧◝(⁰▿⁰)◜✧˖°",
        description: "Let this positive energy fill your day with determination <3",
        color: Number(`${process.env.EMBED_COLOUR}`),
        image: { url: 'https://c.tenor.com/phH0IQwbox8AAAAC/i-got-this-anime.gif' }
      }
    });
  // launch break
  } else if (currentdate.getHours() == 12 && currentdate.getMinutes() == 30) {
    await lib.discord.channels['@0.2.0'].messages.create({
      channel_id: `${process.env.CIPOLLE_GENERAL_CHANNEL}`,
      content: '@everyone',
      embed: {
        title: "(ﾉ´ヮ`)ﾉ  Y U M M Y  ＼(￣▽￣)／",
        description: 'Another morning is gone, stay determined!',
        color: Number(`${process.env.EMBED_COLOUR}`),
        image: { url: 'https://c.tenor.com/GRUsbHL9C_IAAAAC/zerotwo.gif' }
      }
    });
  // ElFa working day end
  } else if (currentdate.getHours() == 17 && currentdate.getMinutes() == 00) {
    await lib.discord.channels['@0.2.0'].messages.create({
      channel_id: `${process.env.CIPOLLE_GENERAL_CHANNEL}`,
      content: '@everyone',
      embed: {
        title: "o(≧▽≦)o ☆  E L F A  ☆～('▽^人)",
        description: 'Another day has passed, see ya and love to all of you :3',
        color: Number(`${process.env.EMBED_COLOUR}`),
        image: { url: 'https://c.tenor.com/Rf5v6glMta8AAAAC/hey-waves.gif' }
      }
    });
  // CISA working day end
  } else if (currentdate.getHours() == 17 && currentdate.getMinutes() == 30) {
    await lib.discord.channels['@0.2.0'].messages.create({
      channel_id: `${process.env.CIPOLLE_GENERAL_CHANNEL}`,
      content: '@everyone',
      embed: {
        title: "o(≧▽≦)o ☆  C I S A  ☆～('▽^人)",
        description: 'Another day has passed, see ya and love to all of you :3',
        color: Number(`${process.env.EMBED_COLOUR}`),
        image: { url: 'https://media.tenor.com/FSK1EksixakAAAAC/thumbs-up-anime.gif' }
      }
    });
  // coffee breaks
  } else if ((currentdate.getHours() == 9 && currentdate.getMinutes() == 0) ||
            (currentdate.getHours() == 15 && currentdate.getMinutes() == 0)) {
    await lib.discord.channels['@0.2.0'].messages.create({
      channel_id: `${process.env.CIPOLLE_COFFEE_CHANNEL}`,
      content: '@everyone',
      embed: {
        title: "(￣ρ￣)..zzZZ C O F F E E T I M E ლ(ಠ_ಠ ლ)",
        description: "Let's go drink some coffee, pls (♡˙︶˙♡)",
        color: Number(`${process.env.EMBED_COLOUR}`),
          image: { url: 'https://c.tenor.com/iDy78BQ8324AAAAC/anime-smell.gif' }
        }
      });
    }
} else {
  // reply to @Angs bot coffee spam during week-ends
  if ((currentdate.getHours() == 9 && currentdate.getMinutes() == 0) ||
      (currentdate.getHours() == 15 && currentdate.getMinutes() == 0)) {
    await vapor.delay(20000);
    await lib.discord.channels['@0.2.0'].messages.create({
      channel_id: `${process.env.CIPOLLE_COFFEE_CHANNEL}`,
      content: '',
      embed: {
        title: "(っ´ω`)ﾉ(╥ω╥) A N G S  I ' M  H E R E ヽ(￣ω￣(。。 )ゝ",
        description: "Your determination is remarkable. \nI'll always be here for you ♡( ◡‿◡ )",
        color: Number(`${process.env.EMBED_COLOUR}`),
        image: { url: 'https://c.tenor.com/qGn2vL8tTMUAAAAC/yuri-reina-kousaka.gif' }
      }
    });
  }
}
