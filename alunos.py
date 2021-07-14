import psycopg2

class Alunos:

    def __init__(self):
        self.reset()

    def reset(self):
        self.id = None
        self.nome = None
        self.email = None
        self.telemovel = None
        self.instrumento = None
        self.idade = None
        self.mensalidade = None
        self.morada = None

    def herokudb(self):
        from db import Database
        mydb = Database()
        return psycopg2.connect(host=mydb.Host, database=mydb.Database, user=mydb.User, password=mydb.Password, sslmode='require')

    def inserirA(self, nome, email, telemovel, instrumento, idade, mensalidade, morada):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("CREATE TABLE IF NOT EXISTS alunos (id serial primary key ,nome text,email text, telemovel text, instrumento text, idade text, mensalidade numeric , morada text)")
        db.execute("INSERT INTO alunos VALUES (DEFAULT , %s, %s, %s, %s, %s, %s, %s)", (nome, email, telemovel, instrumento, idade, mensalidade, morada))
        ficheiro.commit()
        ficheiro.close()

    @property
    def lista(self):
        try:
            ficheiro = self.herokudb()
            db = ficheiro.cursor()
            db.execute("select * from alunos ORDER BY nome")
            db.execute("select * from alunos")
            valor = db.fetchall()
            ficheiro.close()
        except:
            valor = None
        return valor

    @staticmethod
    def code(passe):
        import hashlib
        return hashlib.sha3_256(passe.encode()).hexdigest()