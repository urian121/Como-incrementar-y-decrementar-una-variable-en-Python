# PASO 1, Crear mi entorno virtual

`python -m venv env `

# PASO 2, Activar el entorno virtual ejecutando;

`. env/Scripts/activate`

# PASO 3, Ya dentro del entorno virtual instalar flask

`pip install flask`

# PASO 4, Instalar Python MySQL Connector, es una bibliote (Driver) para conectar Python con MySQL

`pip install mysql-connector-python`

# PASO 5, Lista todos mis paquetes

`pip list  o pip freeze`

# Crear/Actualizar el fichero requirements.txt:

`pip freeze > requirements.txt`

# (env)$ deactivate Para desactivar nuestro entono virtual

# IMPORTANTE, para correr el proyecto solo debes ejecutar el archivo

# requirements.txt con el comando;

`pip install -r requirements.txt`

# en el mismo se encuentran todas las dependecias del proyecto.

# Nota: cuando vallas hacer una actualizacion del archivo requirements.txt

# debes estar dentro del entorno virtual pero no dentro de la carpera app solo en mi entorno.

# Comando para actualizar pip: python -m pip install --upgrade pip

# Instalar pip install python-dotenv para el control de variables de entorno

# NOTA: CUANDO USO EL METODO FETCH O AXIOS PARA REALIZAR UNA SOLICITUD HTTP, Y LA FUNCION ESTA EN ALGUN ARCHIVO JS, NO FUNCIONA, HAY QUE AGREGAR LA FUNCION EN EL MISMO ARCHIVO DEBAJO USANDO CUSTOMJS
