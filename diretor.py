import psycopg2

class Diretor:

    def __init__(self):
        self.reset()

    def reset(self):
        self.id = None
        self.nome = None
        self.email = None
        self.telemovel = None
        self.morada = None

    def herokudb(self):
        from db import Database
        mydb = Database()
        return psycopg2.connect(host=mydb.Host, database=mydb.Database, user=mydb.User, password=mydb.Password, sslmode='require')

    def inserirD(self, nome, email, telemovel, morada):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("CREATE TABLE IF NOT EXISTS diretor (id serial primary key ,nome text,email text, telemovel text, morada text)")
        db.execute("INSERT INTO diretor VALUES (DEFAULT , %s, %s, %s, %s)", (nome, email, telemovel, morada))
        ficheiro.commit()
        ficheiro.close()

    def alterar(self, id, v1, v2, v3, v4):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("UPDATE diretor SET nome = %s WHERE id = %s", (v1, id))
        db.execute("UPDATE diretor SET email = %s WHERE id = %s", (v2, id))
        db.execute("UPDATE diretor SET telemovel = %s WHERE id = %s", (v3, id))
        db.execute("UPDATE diretor SET morada = %s WHERE id = %s", (v4, id))
        ficheiro.commit()
        ficheiro.close()

    def select(self, id):
        try:
            ficheiro = self.herokudb()
            db = ficheiro.cursor()
            db.execute("select * from diretor where id = %s", (id,))
            valor = db.fetchone()
            ficheiro.close()
            self.id = valor[0]
            self.nome = valor[1]
            self.email = valor[2]
            self.morada = valor[3]
        except:
            self.reset()
        return

    @property
    def lista(self):
        try:
            ficheiro = self.herokudb()
            db = ficheiro.cursor()
            db.execute("select * from diretor ORDER BY nome")
            db.execute("select * from diretor")
            valor = db.fetchall()
            ficheiro.close()
        except:
            valor = None
        return valor

    @staticmethod
    def code(passe):
        import hashlib
        return hashlib.sha3_256(passe.encode()).hexdigest()