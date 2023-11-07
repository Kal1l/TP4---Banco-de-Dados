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

    def inserir_5_clientes(tupla):
    for i in range(5):
        db.inserir_cliente(tupla.cpf[i], tupla.nome[i], tupla.telefone, cep, numero, complemento, cpf_func)

    def listar_clientes(self):
        query = "SELECT * FROM Cliente;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def pesquisar_clinte(self,cpf):
        query = "SELECT * FROM Funcionario WHERE cpf=?;"
        self.cursor.execute(query,(cpf,))
        return self.cursor.fetchall()

    def pesquisar_nomes_semelhantes(self,nome):
        query = "SELECT * FROM Funcionario WHERE nome LIKE ?;"
        self.cursor.execute(query, ('%' + nome + '%',))
        return self.cursor.fetchall()

    def atualizar_cliente(self, cpf, nome, telefone, cep, numero, complemento, cpf_func):
        query = "UPDATE Cliente SET nome=?, telefone=?, cep=?, numero=?, complemento=?, cpf_func=? WHERE CPF=?;"
        self.cursor.execute(query, (nome, telefone, cep, numero, complemento, cpf_func, cpf))
        self.conn.commit()

    def deletar_cliente(self, cpf):
        query = "DELETE FROM Cliente WHERE CPF=?;"
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

    def pesquisar_funcionarios(self,cpf):
        query = "SELECT * FROM Funcionario WHERE cpf=?;"
        self.cursor.execute(query,(cpf,))
        return self.cursor.fetchall()

    def atualizar_funcionario(self, cpf, nome, telefone, cep, numero, complemento, cargo, salario):
        query = "UPDATE Funcionario SET nome=?, telefone=?, cep=?, numero=?, complemento=?, cargo=?, salario=? WHERE cpf=?;"
        self.cursor.execute(query, (nome, telefone, cep, numero, complemento, cargo, salario, cpf))
        self.conn.commit()

    def deletar_funcionario(self, cpf):
        query = "DELETE FROM Funcionario WHERE cpf=?;"
        self.cursor.execute(query, (cpf,))
        self.conn.commit()

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()

    def main():
    nome_db = 'tp4.db'
    db = DB(nome_db)
    db.criar_tabelas()

    # Inserir 1 cliente
    cliente1=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    # Inserir 5 clientes
    cliente2=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    cliente3=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    cliente4=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    cliente5=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    cliente6=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    cliente7=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    cliente8=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    cliente9=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    cliente10=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    cliente11=('1', 'Cliente 1', '1234567890', '12345', '1A', 'Apto 101', 1)
    lote1=(cliente2,cliente3,cliente4,cliente5,cliente6)
    lote2=(cliente7,cliente8,cliente9,cliente10,cliente11)
    db.inserir_5_clientes(lote1)
    db.inserir_5_clientes(lote2)

    # Listar todos os clientes
    clientes = db.listar_clientes()
    print("Clientes:")
    for cliente in clientes:
        print(cliente)

    # Pesquisar clientes pelo CPF
    cpf_pesquisado = '12345'
    resultado_pesquisa = db.pesquisar_cliente(cpf_pesquisado)
    if resultado_pesquisa:
        print(f"Cliente encontrado com CPF {cpf_pesquisado}:")
        for cliente in resultado_pesquisa:
            print(cliente)
    else:
        print(f"Nenhum cliente encontrado com CPF {cpf_pesquisado}.")

    # Pesquisar clientes com nomes semelhantes
    nome_pesquisado = 'Cliente'
    resultado_pesquisa_nome = db.pesquisar_nomes_semelhantes(nome_pesquisado)
    if resultado_pesquisa_nome:
        print(f"Clientes encontrados com nome semelhante a '{nome_pesquisado}':")
        for cliente in resultado_pesquisa_nome:
            print(cliente)
    else:
        print(f"Nenhum cliente encontrado com nome semelhante a '{nome_pesquisado}'.")

    # Atualizar um cliente
    db.atualizar_cliente('12345', 'Cliente Atualizado', '9876543210', '54321', '2B', 'Apto 102', 2)

    # Listar clientes novamente após a atualização
    clientes = db.listar_clientes()
    print("\nClientes após atualização:")
    for cliente in clientes:
        print(cliente)

    # Deletar um cliente
    db.deletar_cliente('12345')

    # Listar clientes após a exclusão
    clientes = db.listar_clientes()
    print("\nClientes após exclusão:")
    for cliente in clientes

    # Inserir funcionário
    db.inserir_funcionario(1, 'Funcionário 1', '1234567890', '12345', '1A', 'Apto 101', 'Cargo 1', 5000.00)
    db.inserir_funcionario(2, 'Funcionário 2', '0234567891', '12345', '1A', 'Apto 102', 'Cargo 2', 10000.00)

    # Listar funcionários
    funcionarios = db.listar_funcionarios()
    print("\nFuncionários:")
    for funcionario in funcionarios:
        print(funcionario)

    # Pesquisar funcionários pelo CPF
    cpf_funcionario_pesquisado = 1
    resultado_pesquisa_funcionario = db.pesquisar_funcionarios(cpf_funcionario_pesquisado)
    if resultado_pesquisa_funcionario:
        print(f"Funcionário encontrado com CPF {cpf_funcionario_pesquisado}:")
        for funcionario in resultado_pesquisa_funcionario:
            print(funcionario)
    else:
        print(f"Nenhum funcionário encontrado com CPF {cpf_funcionario_pesquisado}.")

    # Atualizar um funcionário
    db.atualizar_funcionario(1, 'Funcionário Atualizado', '9876543210', '54321', '2B', 'Apto 102', 'Cargo 2', 6000.00)

    # Listar funcionários novamente após a atualização
    funcionarios = db.listar_funcionarios()
    print("\nFuncionários após atualização:")
    for funcionario in funcionarios:
        print(funcionario)

    # Deletar um funcionário
    db.deletar_funcionario(1)

    # Listar funcionários após a exclusão
    funcionarios = db.listar_funcionarios()
    print("\nFuncionários após exclusão:")
    for funcionario in funcionarios

    db.fechar_conexao()

if __name__ == "__main__":
    main()