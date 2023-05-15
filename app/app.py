from flask import Flask, request, redirect, render_template, url_for
# from confiDB import * #Importando conexion BD


# Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app
app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'

current_value = 0
@app.route('/')
def inicio():
    return render_template('base_index.html', current_value=current_value)

@app.route("/increment")
def increment():
    global current_value
    current_value += 1
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
    return render_template('public/pages/info.html')



# Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)



# Ejecutando el objeto Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)
