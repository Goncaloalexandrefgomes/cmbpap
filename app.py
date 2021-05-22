from flask import Flask, render_template, request, url_for, redirect
from user import User

app = Flask(__name__)
usr = User()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/app-calendar')
def calendar():
    return render_template('app-calendar.html')

@app.route('/app-contact')
def contact():
    return render_template('app-contact.html')

@app.route('/app-contactalunos')
def contactalunos():
    return render_template('app-contactalunos.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/app-contact-detail')
def contactdetail():
    return render_template('app-contact-detail.html')

@app.route('/piano')
def piano():
    return render_template('piano.html')

@app.route('/guitarraacustica')
def guitarraacustica():
    return render_template('guitarraacustica.html')


@app.route('/bateria')
def bateria():
    return render_template('bateria.html')


@app.route('/canto')
def canto():
    return render_template('canto.html')


@app.route('/guitarra')
def guitarra():
    return render_template('guitarra.html')


@app.route('/guitarraeletrica')
def guitarraeletrica():
    return render_template('guitarraeletrica.html')


@app.route('/cavaquinho')
def cavaquinho():
    return render_template('cavaquinho.html')


@app.route('/saxofone')
def saxofone():
    return render_template('saxofone.html')


@app.route('/violino')
def violino():
    return render_template('violino.html')

@app.route('/pages-login-2', methods=['GET', 'POST'])
def pageslogin2():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['passe']
        if not usr.existe(v1):
            erro = 'O Utilizador não existe.'
        elif not usr.log(v1, v2):
            erro = 'A palavra passe está errada.'
        else:
            return redirect(url_for('dashboard'))
            erro = 'Bem-Vindo.'
    return render_template('pages-login-2.html', erro=erro)


@app.route('/registo', methods=['GET', 'POST'])
def registo():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['email']
        v3 = request.form['passe']
        v4 = request.form['cpasse']
        if usr.existe(v1):
            erro = 'O Utilizador já existe.'
        elif v3 != v4:
            erro = 'A palavra passe não coincide.'
        else:
            usr.gravar(v1, v2, v3)
    return render_template('registo.html', erro=erro)

@app.route('/newpasse', methods=['GET', 'POST'])
def newpasse():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v0 = request.form['apasse']
        v2 = request.form['passe']
        v3 = request.form['cpasse']
        if not usr.existe(v1):
            erro = 'O Utilizador não existe.'
        elif not usr.log(v1, v0):
            erro = 'A palavra passe está errada.'
        elif v2 != v3:
            erro = 'A palavra passe não coincide.'
        else:
            usr.alterar(v1, v2)
    return render_template('newpasse.html', erro=erro)

if __name__ == '__main__':
    app.run(debug=True)