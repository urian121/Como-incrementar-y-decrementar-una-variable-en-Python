from flask import Flask, render_template, url_for, redirect


# Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)


 # Definir y asignar un valor a current_value
current_value = 0
@app.route('/')
def inicio():
    return render_template('base_index.html', current_value=current_value)

@app.route("/increment")
def increment():
    ''' 
    Cuando se declara una variable como "global" dentro de una función, 
    se indica que esa variable se refiere a la misma variable definida 
    fuera de la función, en lugar de crear una nueva variable local con el mismo nombre.
    '''
    global current_value
    current_value += 1
    '''devolviendo el valor actual de la variable "current_value" como una cadena de texto (str).'''
    return str(current_value)

@app.route("/decrement")
def decrement():
    global current_value
    if current_value > 0:
        current_value -= 1
    return str(current_value)


@app.route('/reset')
def reset():
    global current_value
    current_value = 0
    return str(current_value)



@app.route('/info', methods=['GET', 'POST'])
def editProfile():
    '''
    La función render_template() en Flask se utiliza para renderizar plantillas 
    HTML utilizando el motor de plantillas Jinja2
    '''
    return render_template('public/pages/info.html')



# Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    'url_for() se usa para generar las URLs basadas en los nombres de las funciones definidas'
    return redirect(url_for('inicio'))


@app.errorhandler(500)
def server_error(error):
    ''' 
    La función redirect de Flask se usa para redirigir a una ruta en especifico (inicio).
     '''
    return redirect(url_for('inicio'))



# Ejecutando el objeto Flask
if __name__ == '__main__':
    '''
    app.run(debug=True, port=5000) se utiliza para iniciar el servidor Flask
    y comenzar a escuchar las solicitudes entrantes
    '''
    app.run(debug=True, port=5000)
