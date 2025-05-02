from flask import Flask
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__,template_folder='template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql= MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('iniciar_sesion.html')

@app.route('/acceso-login', methods=["GET","POST"])
def acceso_login():
    
    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword':
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']
        
        cur=mysql.connection.cursor()
        
        cur.execute("SELECT * FROM usuarios WHERE correo = %s AND password = %s", (_correo, _password))
        accout = cur.fetchone()
        
        if accout:
            session['logueado'] = True
            session['id'] = accout['id']
            
            return render_template('inicio.html', message="Bienvenido")
        else:
            return render_template('iniciar_sesion.html', message="Usuario o contraseña incorrectos")
        
@app.route('/acceso-admin', methods=["GET","POST"])
def acceso_admin():
    
    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword':
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']
        
        cur=mysql.connection.cursor()
        
        cur.execute("SELECT * FROM usuarios WHERE correo = %s AND password = %s", (_correo, _password))
        accout = cur.fetchone()
        
        if accout:
            session['logueado'] = True
            session['id'] = accout['id']
            
            return render_template('admin.html', message="Bienvenido")
        else:
            return render_template('iniciar_sesion.html', message="Usuario o contraseña incorrectos")

        
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/informatica')
def informatica():
    return render_template('informatica.html')

@app.route('/gastronomia')
def gastronomia():
    return render_template('gastronomia.html')

@app.route('/contabilidadA')
def contabilidadA():
    return render_template('contabilidadA.html')

@app.route('/contabilidadB')
def contabilidadB():
    return render_template('contabilidadB.html')

@app.route('/mercadeoA')
def mercadeoA():
    return render_template('mercadeoA.html')

@app.route('/mercadeoB')
def mercadeoB():
    return render_template('mercadeoB.html')

@app.route('/refrigeracion')
def refrigeracion():
    return render_template('refrigeracion.html')

@app.route('/electronica')
def electronica():
    return render_template('electronica.html')

@app.route('/electricidad')
def electricidad():
    return render_template('electricidad.html')

@app.route('/pasantes')
def pasantes():
    return render_template('pasantes.html')

if __name__ == '__main__':
    app.secret_key="felix_hds"
    app.run(debug=True, host='0.0.0.0' , port=5000, threaded=True)