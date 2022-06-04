const fs = require('fs')
const { mkdirFile } = require('./mkdirfile')

const isUpdatable = (name) => {
  const today = new Date().toDateString();
  let canUpdate;

  mkdirFile(name)

  const file = `data/${name}/day.txt`

  if (fs.existsSync(file)) {

    const dataFile = fs.readFileSync(file, 'utf-8')

    if (dataFile === today) {

      canUpdate = false;
      console.log('los datos estan al día')

    } else {

      canUpdate = true;
      fs.writeFileSync(file, today)
      console.log('los datos necesitan actualizarse__dif-day')
    }

  } else {

    canUpdate = true;
    fs.writeFileSync(file, today)
    console.log('los datos necesitan actualizarse__dif-day')
  }

  return canUpdate;
}

module.exports = isUpdatable



// let canUpdate;
// const dirFile = `data/${name}`;

// if (dirFile) {
//   const file = dirFile + '/day.txt'
//   const existDate = fs.existsSync(file);
//   const today = new Date().toDateString();
//   console.log(today)
//   //si existe el archivo day.txt
//   if (existDate) {
//     const dataFile = fs.readFileSync(file, 'utf-8')

//     if (dataFile === today) {
//       canUpdate = false;
//       console.log('los datos estan al día')
//     } else {
//       canUpdate = true;
//       fs.writeFileSync(file, today)
//       console.log('los datos necesitan actualizarse__dif-day')
//     }

//   } else {
//     fs.writeFileSync(file, today)
//     fs.mkdirSync(dirFile)
//     canUpdate = true
//     console.log(dirFile, file)
//     console.log('los datos necesitan actualizarse')
//   }


// } else {
//   console.log(dirFile, file)
//   fs.mkdirSync(dirFile)
//   fs.writeFileSync(file, today)
//   console.log('los datos necesitan actualizarse___nodir')
//   canUpdate = true;

// }

// return canUpdate

// }



