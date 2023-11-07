import sqlite3 as sql

class DB:
    def __init__(self, db):
        self.db = db
        self.conn = sql.connect(self.db)
        self.cursor = self.conn.cursor()

    def criar_tabelas(self):
        tabela_cliente = '''
        CREATE TABLE IF NOT EXISTS Cliente (
            CPF TEXT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            cep TEXT NOT NULL,
            numero TEXT NOT NULL,
            complemento TEXT,
            cpf_func TEXT,
            PRIMARY KEY (CPF),
            FOREIGN KEY (cpf_func) REFERENCES Funcionario(cpf)
        );'''
        self.cursor.execute(tabela_cliente)

        tabela_funcionario = '''
        CREATE TABLE IF NOT EXISTS Funcionario (
            cpf TEXT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            cep TEXT NOT NULL,
            numero TEXT NOT NULL,
            complemento TEXT,
            cargo TEXT NOT NULL,
            salario REAL NOT NULL,
            PRIMARY KEY (cpf)
        );'''
        self.cursor.execute(tabela_funcionario)
        self.conn.commit()

    def inserir_cliente(self, cpf, nome, telefone, cep, numero, complemento, cpf_func):
        query = "INSERT INTO Cliente (CPF, nome, telefone, cep, numero, complemento, cpf_func) VALUES (?, ?, ?, ?, ?, ?, ?);"
        self.cursor.execute(query, (cpf, nome, telefone, cep, numero, complemento, cpf_func))
        self.conn.commit()

    def inserir_5_clientes(self, tuplas_clientes):
        for tupla in tuplas_clientes:
            self.inserir_cliente(*tupla)

    def listar_clientes(self):
        query = "SELECT * FROM Cliente;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def pesquisar_cliente(self, cpf):
        query = "SELECT * FROM Cliente WHERE CPF = ?;"
        self.cursor.execute(query, (cpf,))
        return self.cursor.fetchall()

    def pesquisar_nomes_semelhantes(self, nome):
        query = "SELECT * FROM Cliente WHERE nome LIKE ?;"
        self.cursor.execute(query, ('%' + nome + '%',))
        return self.cursor.fetchall()

    def atualizar_cliente(self, cpf, nome, telefone, cep, numero, complemento, cpf_func):
        query = "UPDATE Cliente SET nome=?, telefone=?, cep=?, numero=?, complemento=?, cpf_func=? WHERE CPF=?;"
        self.cursor.execute(query, (nome, telefone, cep, numero, complemento, cpf_func, cpf))
        self.conn.commit()

    def deletar_cliente(self, cpf):
        query = "DELETE FROM Cliente WHERE CPF = ?;"
        self.cursor.execute(query, (cpf,))
        self.conn.commit()

    def inserir_funcionario(self, cpf, nome, telefone, cep, numero, complemento, cargo, salario):
        query = "INSERT INTO Funcionario (cpf, nome, telefone, cep, numero, complemento, cargo, salario) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        self.cursor.execute(query, (cpf, nome, telefone, cep, numero, complemento, cargo, salario))
        self.conn.commit()

    def listar_funcionarios(self):
        query = "SELECT * FROM Funcionario;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def pesquisar_funcionarios(self, cpf):
        query = "SELECT * FROM Funcionario WHERE cpf = ?;"
        self.cursor.execute(query, (cpf,))
        return self.cursor.fetchall()

    def atualizar_funcionario(self, cpf, nome, telefone, cep, numero, complemento, cargo, salario):
        query = "UPDATE Funcionario SET nome=?, telefone=?, cep=?, numero=?, complemento=?, cargo=?, salario=? WHERE cpf = ?;"
        self.cursor.execute(query, (nome, telefone, cep, numero, complemento, cargo, salario, cpf))
        self.conn.commit()

    def deletar_funcionario(self, cpf):
        query = "DELETE FROM Funcionario WHERE cpf = ?;"
        self.cursor.execute(query, (cpf,))
        self.conn.commit()

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()

def main():
    nome_db = 'tp4.db'
    db = DB(nome_db)
    db.criar_tabelas()

    # Inserir um cliente
    db.inserir_cliente('12345', 'João Paulo', '1234567890', '12345', '1A', 'Apto 101', '10001')

    # Inserir 5 clientes
    tuplas_clientes = [
        ('67890', 'Pedro Henrique', '9876543210', '54321', '2B', 'Apto 102', '10001'),
        ('54321', 'João Pedro', '5555555555', '54321', '3C', 'Apto 103', '10002'),
        ('99999', 'Maria Socorro', '1111111111', '54321', '4D', 'Apto 104', '10001'),
        ('88888', 'Maria do Socorro', '2222222222', '54321', '5E', 'Apto 105', '10002'),
        ('77777', 'Maria João Pedro', '3333333333', '54321', '6F', 'Apto 106', '10002')
    ]
    db.inserir_5_clientes(tuplas_clientes)

    # Listar todos os clientes
    clientes = db.listar_clientes()
    print("Clientes:")
    for cliente in clientes:
        print(cliente)

    # Pesquisar cliente pelo CPF
    cpf_pesquisado = '12345'
    resultado_pesquisa = db.pesquisar_cliente(cpf_pesquisado)
    if resultado_pesquisa:
        print(f"Cliente encontrado com CPF {cpf_pesquisado}:")
        for cliente in resultado_pesquisa:
            print(cliente)
    else:
        print(f"Nenhum cliente encontrado com CPF {cpf_pesquisado}.")

    # Pesquisar clientes com nomes semelhantes
    nome_pesquisado = 'Pedro'
    resultado_pesquisa_nome = db.pesquisar_nomes_semelhantes(nome_pesquisado)
    if resultado_pesquisa_nome:
        print(f"Clientes encontrados com nome semelhante a '{nome_pesquisado}':")
        for cliente in resultado_pesquisa_nome:
            print(cliente)
    else:
        print(f"Nenhum cliente encontrado com nome semelhante a '{nome_pesquisado}'.")

    # Atualizar um cliente
    db.atualizar_cliente('12345', 'João Paulo', '1234567890', '12345', '1A', 'Apto 101', '10002')

    # Deletar um cliente
    db.deletar_cliente('67890')

    # Inserir dois funcionários
    db.inserir_funcionario('10001', 'Marcos Aurélio', '1234567890', '12345', '1A', 'Apto 101', 'Cargo 1', 5000.00)
    db.inserir_funcionario('10002', 'Elizabete Apóstrofe', '9876543210', '54321', '2B', 'Apto 102', 'Cargo 2', 6000.00)

    # Listar funcionários
    funcionarios = db.listar_funcionarios()
    print("Funcionários:")
    for funcionario in funcionarios:
        print(funcionario)

    # Pesquisar funcionário pelo CPF
    cpf_funcionario_pesquisado = '10001'
    resultado_pesquisa_funcionario = db.pesquisar_funcionarios(cpf_funcionario_pesquisado)
    if resultado_pesquisa_funcionario:
        print(f"Funcionário encontrado com CPF {cpf_funcionario_pesquisado}:")
        for funcionario in resultado_pesquisa_funcionario:
            print(funcionario)
    else:
        print(f"Nenhum funcionário encontrado com CPF {cpf_funcionario_pesquisado}.")

    # Atualizar um funcionário
    db.atualizar_funcionario('10001', 'Marcos Aurélio', '1234567890', '12345', '1A', 'Apto 103', 'Cargo 1', 7000.00)

    # Deletar um funcionário
    db.deletar_funcionario('10002')

    db.fechar_conexao()

if __name__ == "__main__":
    main()
