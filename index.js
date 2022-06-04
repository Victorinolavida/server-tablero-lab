const express = require('express');
const app = express();
const cors = require('cors');
const connect = require('./db/db');
const { getDataBaseByName } = require('./controllers/controller');


connect()
console.log(__dirname)
//endpoint
app.use('/', express.static('public'));
app.use(cors())
app.get("/api/:name", (req, res) => {
  getDataBaseByName(req, res, `${__dirname}/python`)
})


const port = process.env.PORT;
app.listen(port, () => console.log(`Server connected to ${port}`));

