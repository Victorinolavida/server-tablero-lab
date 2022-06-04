const DataBase = require("../models/dataBase");
const runPythonFile = require('../helpers/python')



//TODO: poner una lista de opciones en el name, ya que se puede poner
//cualquier string

const getDataBaseByName = async (req, res, pathPython) => {
  // FIXME: hacer que solo acepte nombres de bases
  const { name } = req.params

  if (!name) {
    return res.statu(400).json({ msg: 'El nombre es obligatorio' })
  }


  try {

    console.log('buscando db')

    const database = await DataBase.findOne({ name })

    console.log(database)

    if (!database) {
      console.log('si no existe')

      runPythonFile(name, res, false, pathPython)

    } else {
      console.log('si existe y:')
      const today = new Date().toDateString();

      if (today === database['UpdateAt']) {
        console.log('esta al dia')
        res.json(database)
      } else {
        console.log('es del dia pasado')

        runPythonFile(name, res, true, pathPython)
      }

    }

  } catch (error) {
    console.log(error)

  }




}


module.exports = {
  getDataBaseByName
}

