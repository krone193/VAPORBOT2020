const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
const vapor = require('../../../../helpers/vaporfunc.js');

const CommandContent = [
  'https://c.tenor.com/MN1hqkhC9KEAAAAC/anime-hair-flip.gif',
  'https://c.tenor.com/SplAvaLIUpIAAAAC/black-hair.gif',
  'https://c.tenor.com/Y2xxPef5KJsAAAAC/zero-two-darling-in-the-franxx.gif',
  'https://c.tenor.com/Gka2XHXOUbUAAAAC/hair-flip-sassy.gif',
  'https://c.tenor.com/5xa8xEczo8wAAAAC/homura-chika.gif',
  'https://c.tenor.com/R_iIVnTdKIoAAAAC/anime-girls.gif',
  'https://c.tenor.com/kFPzUhqW0r8AAAAC/flip-hair-girl.gif',
  'https://c.tenor.com/6dQY0CXo8-oAAAAC/hair-flip-homura.gif',
  'https://c.tenor.com/3u5DQiRx__MAAAAC/anime-hair.gif',
  'https://64.media.tumblr.com/5e666e582345ed35d1f4c43ca4f79e73/tumblr_phceozedbr1th206io1_640.gifv',
  
  'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d8aec9ac-9b78-4fb9-8f4e-320ff8de23a3/d4rn2bn-4a040f14-76ab-4a55-9e09-794375c6e361.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q4YWVjOWFjLTliNzgtNGZiOS04ZjRlLTMyMGZmOGRlMjNhM1wvZDRybjJibi00YTA0MGYxNC03NmFiLTRhNTUtOWUwOS03OTQzNzVjNmUzNjEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.1KMEpgDEq4FQ3kqJHeCWWwlgz_zEkJpSP9E4E6D_boQ',
  'https://i.gifer.com/1oVC.gif',
  'http://pa1.narvii.com/5679/bd394ac3d4a3c8c96d7e6504a8c28581f2f65d97_hq.gif',
  'https://giffiles.alphacoders.com/345/34574.gif',
  'https://c.tenor.com/9NUWB3EZn5sAAAAC/hair-flip-aesthetic.gif',
  'https://www.kotaku.com.au/wp-content/uploads/sites/3/2017/02/11/irm3dwdg8zlpwzod55hb.gif?quality=80&w=660',
  'https://c.tenor.com/_hFFcCCh2SEAAAAC/girly-air-force-gripen.gif'
];

await vapor.sendgif(
  context.params.event,
  CommandContent,
  true,
  Number(`${process.env.EMBED_COLOUR}`)
);

return 0;
