const mongoose = require("mongoose");
require('dotenv').config({ path: '.env' })


const connect = async () => {

  try {

    mongoose.connect(process.env.MONGO_LINK)

    console.log('Conectado correctamente a la base de datos')
  } catch (error) {
    console.log(error)
    console.log('no se pudo conectar')
  }

}

module.exports = connect