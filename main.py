# Meu primeiro código
import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('escola_musica.db')
cursor = conn.cursor()

# Criação da tabela de inscrições se ela ainda não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS inscricoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    instrumento TEXT NOT NULL,
    contato TEXT NOT NULL,
    email TEXT NOT NULL,
    escola_publica BOOLEAN NOT NULL
)
''')

# Função para coletar dados do usuário
def inscrever_aluno():
    print("==== Ficha de Inscrição ====")
    
    nome = input("Nome Completo: ")
    idade = int(input("Idade: "))
    instrumento = input("Instrumento de Interesse: ")
    contato = input("Telefone para Contato: ")
    email = input("Email: ")
    escola_publica = input("Estudante de escola pública? (sim/não): ").lower()

    # Conversão da resposta para booleano
    escola_publica = True if escola_publica == "sim" else False

    # Inserindo os dados no banco
    cursor.execute('''
        INSERT INTO inscricoes (nome, idade, instrumento, contato, email, escola_publica)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, idade, instrumento, contato, email, escola_publica))

    conn.commit()
    print(f"\nAluno(a) {nome} inscrito(a) com sucesso!\n")

# Função para listar todos os inscritos
def listar_inscritos():
    cursor.execute("SELECT * FROM inscricoes")
    inscritos = cursor.fetchall()

    if inscritos:
        print("==== Lista de Inscritos ====")
        for inscrito in inscritos:
            print(f"ID: {inscrito[0]} | Nome: {inscrito[1]} | Idade: {inscrito[2]} | Instrumento: {inscrito[3]} | Contato: {inscrito[4]} | Email: {inscrito[5]} | Escola Pública: {'Sim' if inscrito[6] else 'Não'}")
    else:
        print("Nenhum aluno inscrito.")

# Função principal
def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Inscrever novo aluno")
        print("2. Listar todos os inscritos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inscrever_aluno()
        elif opcao == '2':
            listar_inscritos()
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

# Fecha a conexão com o banco de dados ao finalizar o programa
conn.close()
