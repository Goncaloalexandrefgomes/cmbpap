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
        return psycopg2.connect(host=mydb.Host, database=mydb.Database, user=mydb.User, password=mydb.Password,
                                sslmode='require')

    def inserirF(self, nome, email, telemovel, cargo, idade, salario, morada):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute(
            "CREATE TABLE IF NOT EXISTS funcionarios (id serial primary key ,nome text,email text, telemovel text, cargo text, idade text, salario numeric , morada text)")
        db.execute("INSERT INTO funcionarios VALUES (DEFAULT , %s, %s, %s, %s, %s, %s, %s)",
                   (nome, email, telemovel, cargo, idade, salario, morada))
        ficheiro.commit()
        ficheiro.close()

    def apaga(self, id):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("DELETE FROM funcionarios WHERE id = %s", (id,))
        ficheiro.commit()
        ficheiro.close()

    def alterar(self, id, v1, v2, v3, v4, v5, v6, v7):
        ficheiro = self.herokudb()
        db = ficheiro.cursor()
        db.execute("UPDATE funcionarios SET nome = %s WHERE id = %s", (v1, id))
        db.execute("UPDATE funcionarios SET email = %s WHERE id = %s", (v2, id))
        db.execute("UPDATE funcionarios SET telemovel = %s WHERE id = %s", (v3, id))
        db.execute("UPDATE funcionarios SET cargo = %s WHERE id = %s", (v4, id))
        db.execute("UPDATE funcionarios SET idade = %s WHERE id = %s", (v5, id))
        db.execute("UPDATE funcionarios SET salario = %s WHERE id = %s", (v6, id))
        db.execute("UPDATE funcionarios SET morada = %s WHERE id = %s", (v7, id))
        ficheiro.commit()
        ficheiro.close()

    def select(self, id):
        try:
            ficheiro = self.herokudb()
            db = ficheiro.cursor()
            db.execute("select * from funcionarios where id = %s", (id,))
            valor = db.fetchone()
            ficheiro.close()
            self.id = valor[0]
            self.nome = valor[1]
            self.email = valor[2]
            self.telemovel = valor[3]
            self.cargo = valor[4]
            self.idade = valor[5]
            self.salario = valor[6]
            self.morada = valor[7]
        except:
            self.reset()
        return

    @property
    def lista(self):
        try:
            ficheiro = self.herokudb()
            db = ficheiro.cursor()
            db.execute("select * from funcionarios ORDER BY nome")
            db.execute("select * from funcionarios")
            valor = db.fetchall()
            ficheiro.close()
        except:
            valor = None
        return valor

    @staticmethod
    def code(passe):
        import hashlib
        return hashlib.sha3_256(passe.encode()).hexdigest()
