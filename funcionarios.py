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