const express = require('express');
const app = express();
const cors = require('cors');
const connect = require('./db/db');
const { getDataBaseByName } = require('./controllers/controller');


connect()

//endpoint
app.use(cors())
app.get("/api/:name", getDataBaseByName)




const port = process.env.PORT || 8000;
app.listen(port, () => console.log(`Server connected to ${port}`));

