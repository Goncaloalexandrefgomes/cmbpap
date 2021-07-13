import psycopg2

class Funcionarios:

    def __init__(self):
        self.reset()

    def reset(self):
        self.id = None
        self.nome = None
        self.email = None
        self.telemovel = None
        self.cargo = None
        self.idade = None
        self.salario = None
        self.morada = None

    def herokudb(self):
        from db import Database
        mydb = Database()
        return psycopg2.connect(host=mydb.Host, database=mydb.Database, user=mydb.User, password=mydb.Password, sslmode='require')

    def inserirF(self, nome, email, telemovel, cargo, idade, salario, morada):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("CREATE TABLE IF NOT EXISTS funcionarios (id serial primary key ,nome text,email text, telemovel text, cargo text, idade text, salario numeric , morada text)")
        db.execute("INSERT INTO funcionarios VALUES (DEFAULT , %s, %s, %s, %s, %s, %s, %s)", (nome, email, telemovel, cargo, idade, salario, morada))
        ficheiro.commit()
        ficheiro.close()

    def existe(self, login):
        try:
            ficheiro = self.herokudb()
            db = ficheiro.cursor()
            db.execute("SELECT * FROM usr WHERE login = %s", (login,))
            valor = db.fetchone()
            ficheiro.close()
        except:
            valor = None
        return valor

    def log(self, login, password):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("SELECT * FROM usr WHERE login = %s and password = %s", (login, self.code(password),))
        valor = db.fetchone()
        ficheiro.close()
        return valor

    def alterar(self, login, password):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("UPDATE usr SET password = %s WHERE login = %s", (self.code(password), login))
        ficheiro.commit()
        ficheiro.close()

    def apaga(self, login):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("DELETE FROM usr WHERE login = %s", (login,))
        ficheiro.commit()
        ficheiro.close()

    @staticmethod
    def code(passe):
        import hashlib
        return hashlib.sha3_256(passe.encode()).hexdigest()