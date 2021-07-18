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

    def apaga(self, id):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("DELETE FROM alunos WHERE id = %s", (id,))
        ficheiro.commit()
        ficheiro.close()

    def alterar(self, id, v1, v2, v3, v4, v5, v6, v7):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("UPDATE alunos SET nome = %s WHERE id = %s", (v1, id))
        db.execute("UPDATE alunos SET email = %s WHERE id = %s", (v2, id))
        db.execute("UPDATE alunos SET telemovel = %s WHERE id = %s", (v3, id))
        db.execute("UPDATE alunos SET instrumento = %s WHERE id = %s", (v4, id))
        db.execute("UPDATE alunos SET idade = %s WHERE id = %s", (v5, id))
        db.execute("UPDATE alunos SET mensalidade = %s WHERE id = %s", (v6, id))
        db.execute("UPDATE alunos SET morada = %s WHERE id = %s", (v7, id))
        ficheiro.commit()
        ficheiro.close()

    def select(self, id):
        try:
            ficheiro = self.herokudb()
            db = ficheiro.cursor()
            db.execute("select * from alunos where id = %s", (id,))
            valor = db.fetchone()
            ficheiro.close()
            self.id = valor[0]
            self.nome = valor[1]
            self.email = valor[2]
            self.telemovel = valor[3]
            self.instrumento = valor[4]
            self.idade = valor[5]
            self.mensalidade = valor[6]
            self.morada = valor[7]
        except:
            self.reset()
        return

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