
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criação da tabela de clientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
""")

conexao.commit()


# Função para salvar os dados do cliente
def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # Validação dos campos
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Por favor, preencha todos os campos!"
        )
        return

    # Validação simples do e-mail
    if "@" not in email or "." not in email:
        messagebox.showwarning(
            "Atenção",
            "Digite um e-mail válido!"
        )
        return

    try:
        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar o cliente:\n{erro}"
        )


# Função para limpar o formulário
def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


# Criação da janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x350")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="CADASTRO DE CLIENTES",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

# Campo Nome
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()

entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)

# Campo E-mail
label_email = tk.Label(janela, text="E-mail:")
label_email.pack()

entrada_email = tk.Entry(janela, width=40)
entrada_email.pack(pady=5)

# Campo Telefone
label_telefone = tk.Label(janela, text="Telefone:")
label_telefone.pack()

entrada_telefone = tk.Entry(janela, width=40)
entrada_telefone.pack(pady=5)

# Botões
botao_salvar = tk.Button(
    janela,
    text="Salvar Cliente",
    width=20,
    bg="green",
    fg="white",
    command=salvar_cliente
)
botao_salvar.pack(pady=10)

botao_limpar = tk.Button(
    janela,
    text="Limpar Formulário",
    width=20,
    command=limpar_formulario
)
botao_limpar.pack(pady=5)

# Foco inicial no campo nome
entrada_nome.focus()

# Inicialização da interface gráfica
janela.mainloop()



import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criação da tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
""")

conexao.commit()


# Função para salvar os dados do cliente
def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # Verifica se todos os campos foram preenchidos
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Por favor, preencha todos os campos!"
        )
        return

    # Validação simples do e-mail
    if "@" not in email or "." not in email:
        messagebox.showwarning(
            "Atenção",
            "Digite um e-mail válido!"
        )
        return

    try:
        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar o cliente:\n{erro}"
        )


# Função para limpar o formulário
def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


# Nova funcionalidade: visualizar clientes cadastrados
def visualizar_clientes():

    # Cria uma nova janela
    janela_clientes = tk.Toplevel(janela)
    janela_clientes.title("Clientes Cadastrados")
    janela_clientes.geometry("650x350")
    janela_clientes.resizable(False, False)

    # Título da janela
    titulo_clientes = tk.Label(
        janela_clientes,
        text="LISTA DE CLIENTES CADASTRADOS",
        font=("Arial", 14, "bold")
    )
    titulo_clientes.pack(pady=15)

    # Criação da tabela visual
    colunas = ("ID", "Nome", "E-mail", "Telefone")

    tabela = ttk.Treeview(
        janela_clientes,
        columns=colunas,
        show="headings"
    )

    # Configuração dos cabeçalhos
    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.heading("E-mail", text="E-mail")
    tabela.heading("Telefone", text="Telefone")

    # Configuração das larguras das colunas
    tabela.column("ID", width=50, anchor="center")
    tabela.column("Nome", width=180)
    tabela.column("E-mail", width=200)
    tabela.column("Telefone", width=150)

    tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Consulta os clientes no banco de dados
    try:
        cursor.execute("""
            SELECT id, nome, email, telefone
            FROM clientes
            ORDER BY id
        """)

        clientes = cursor.fetchall()

        # Insere os dados na tabela
        if clientes:
            for cliente in clientes:
                tabela.insert("", tk.END, values=cliente)
        else:
            messagebox.showinfo(
                "Informação",
                "Nenhum cliente cadastrado.",
                parent=janela_clientes
            )

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível consultar os clientes:\n{erro}",
            parent=janela_clientes
        )


# Criação da janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x430")
janela.resizable(False, False)

# Título principal
titulo = tk.Label(
    janela,
    text="CADASTRO DE CLIENTES",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

# Campo Nome
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()

entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)

# Campo E-mail
label_email = tk.Label(janela, text="E-mail:")
label_email.pack()

entrada_email = tk.Entry(janela, width=40)
entrada_email.pack(pady=5)

# Campo Telefone
label_telefone = tk.Label(janela, text="Telefone:")
label_telefone.pack()

entrada_telefone = tk.Entry(janela, width=40)
entrada_telefone.pack(pady=5)

# Botão Salvar Cliente
botao_salvar = tk.Button(
    janela,
    text="Salvar Cliente",
    width=25,
    bg="green",
    fg="white",
    command=salvar_cliente
)
botao_salvar.pack(pady=8)

# Botão Limpar Formulário
botao_limpar = tk.Button(
    janela,
    text="Limpar Formulário",
    width=25,
    command=limpar_formulario
)
botao_limpar.pack(pady=5)

# Novo botão Visualizar Clientes
botao_visualizar = tk.Button(
    janela,
    text="Visualizar Clientes",
    width=25,
    bg="blue",
    fg="white",
    command=visualizar_clientes
)
botao_visualizar.pack(pady=8)

# Foco inicial no campo nome
entrada_nome.focus()

# Inicialização da interface gráfica
janela.mainloop()

# Fechamento da conexão com o banco de dados
conexao.close()


# Fechamento da conexão ao encerrar a aplicação
conexao.close()
