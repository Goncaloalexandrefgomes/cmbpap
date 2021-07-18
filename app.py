from flask import Flask, render_template, request, url_for, redirect
from user import User
from funcionarios import Funcionarios
from alunos import Alunos
from diretor import Diretor

app = Flask(__name__)
usr = User()
fun = Funcionarios()
alu = Alunos()
dire = Diretor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    dados = alu.lista
    dados2 = fun.lista
    return render_template('dashboard.html', tabela=dados, tabela2=dados2)

@app.route('/app-calendar')
def calendar():
    return render_template('app-calendar.html')

@app.route('/app-contact')
def contact():
    dados = fun.lista
    return render_template('app-contact.html', tabela=dados, max=len(dados))

@app.route('/app-contactalunos')
def contactalunos():
    dados = alu.lista
    return render_template('app-contactalunos.html', tabela=dados, max=len(dados))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    dados = dire.lista
    #id = dados[li][0]
    dire.select(id)
    if request.method == 'POST':
        if "delete" in request.form:
            dire.apaga(id)
            return redirect('/app-contactalunos')
        elif "edit" in request.form:
            v1 = request.form['nome']
            v2 = request.form['email']
            v3 = request.form['telemovel']
            v4 = request.form['morada']
            dire.alterar(id, v1, v2, v3, v4)
            dire.select(id)
            return redirect('/profile')
    #dire.inserirD('Goncalo Gomes', 'goncalo.gomes1412003@gmail.com', 963965166, 'Rua de Cima')
    return render_template('profile.html', tabela=dire.lista)

@app.route('/app-contact-detail/<int:li>', methods=['GET', 'POST'])
def contactdetail(li):
    dados = alu.lista
    id = dados[li][0]
    alu.select(id)
    if request.method == 'POST':
        if "delete" in request.form:
            alu.apaga(id)
            return redirect('/app-contactalunos')
        elif "edit" in request.form:
            v1 = request.form['nome']
            v2 = request.form['email']
            v3 = request.form['telemovel']
            v4 = request.form['instrumento']
            v5 = request.form['idade']
            v6 = request.form['mensalidade']
            v7 = request.form['morada']
            alu.alterar(id, v1, v2, v3, v4, v5, v6, v7)
            alu.select(id)
            return redirect('/app-contactalunos')
    return render_template('app-contact-detail.html', tabela=alu.lista, li=li)

@app.route('/app-contact-detailfuncionarios/<int:li>', methods=['GET', 'POST'])
def detailfuncionarios(li):
    dados = fun.lista
    id = dados[li][0]
    fun.select(id)
    if request.method == 'POST':
        if "delete" in request.form:
            fun.apaga(id)
            return redirect('/app-contact')
        elif "edit" in request.form:
            v1 = request.form['nome']
            v2 = request.form['email']
            v3 = request.form['telemovel']
            v4 = request.form['cargo']
            v5 = request.form['idade']
            v6 = request.form['salario']
            v7 = request.form['morada']
            fun.alterar(id, v1, v2, v3, v4, v5, v6, v7)
            fun.select(id)
            return redirect('/app-contact')
    return render_template('app-contact-detailfuncionarios.html', tabela=fun.lista, li=li)

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

@app.route('/addaluno', methods=['GET', 'POST'])
def addaluno():
    # alu.inserirA('Rosa Lopes', 'email@gmail.com', 123456789, 'bateria', 16, 60, 'Rua de Baixo 212')
    if request.method == 'POST':
        v1 = request.form['nome']
        v2 = request.form['email']
        v3 = request.form['telemovel']
        v4 = request.form['instrumento']
        v5 = request.form['idade']
        v6 = request.form['mensalidade']
        v7 = request.form['morada']
        alu.inserirA(v1, v2, v3, v4, v5, v6, v7)
        return redirect('/app-contactalunos')
    return render_template('addaluno.html', alu=alu,)

@app.route('/addfuncionario', methods=['GET', 'POST'])
def addfuncionario():
    #fun.inserirF('Rosa Lopes', 'email@gmail.com', 123456789, 'professor - bateria', 43, 1250, 'Rua de Baixo 212')
    if request.method == 'POST':
        v1 = request.form['nome']
        v2 = request.form['email']
        v3 = request.form['telemovel']
        v4 = request.form['cargo']
        v5 = request.form['idade']
        v6 = request.form['salario']
        v7 = request.form['morada']
        fun.inserirF(v1, v2, v3, v4, v5, v6, v7)
        return redirect('/app-contact')
    return render_template('addfuncionario.html', fun=fun,)

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