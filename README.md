# Como y que necesitas para correr este servidor

## necesitas:

- Una base con MongoDB y un link para conectarte a ella 
- Nodejs y npm instalados
- Python3 y pip 3 
  - beautifullsoup 

## Para arrancar el sevidor

edita el archivo **.example.env** y renombralo por **.env** y pega tu Link de Mongo, respetando lo que esta en el archivo **.example.env**.

una vez editado abre una terminal y en la carpeta del proyecto ejecuta
```bash

npm install
```

espera que termine todo correctamente y ejecuta :
```bash

npm run dev
```

y si todo sale bien te salda el mensaje 

```bash

Conectado correctamente a la base de datos
Server connected to 8000
```

que significa que todo salio bien