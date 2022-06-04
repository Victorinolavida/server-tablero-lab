const { Schema, model } = require("mongoose");


const dataBaseSchema = new Schema({
  name: {
    type: String,
    unique: true
  },
  data: {
    type: Object,
  },
  UpdateAt: {
    type: String,
    default: new Date().toDateString()
  }
})



module.exports = model('DataBase', dataBaseSchema)