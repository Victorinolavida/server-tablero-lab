const fs = require('fs')


const mkdirFile = (name) => {

  let exist;

  if (!fs.existsSync(`data/${name}`)) {
    fs.mkdirSync(`data/${name}`)
  }



}

module.exports = {
  mkdirFile
}