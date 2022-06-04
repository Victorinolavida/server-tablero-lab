const { PythonShell } = require('python-shell');
const DataBase = require("../models/dataBase");


const runPythonFile = (name, res, isUpdate = false, pathPython) => {

  console.log(pathPython)

  let options = {
    mode: 'text',
    scriptPath: pathPython
  };

  PythonShell.run(`${name}.py`, options, async function (err, result) {

    if (err) {

      return res.status(400).json({ msg: `${name} no es un valor válido` })

    };


    if (isUpdate) {
      console.log('actualizando')

      const oldDataBase = await DataBase.findOneAndUpdate({ name }, {
        UpdateAt: new Date().toDateString(),
        data: JSON.parse(result[0])
      }, { new: true })

      return res.json(oldDataBase)
    }

    console.log('creando')
    const newDataBase = new DataBase({
      name,
      data: JSON.parse(result[0])
    })

    await newDataBase.save()

    return res.status(201).json(newDataBase)

  });



}

module.exports = runPythonFile;