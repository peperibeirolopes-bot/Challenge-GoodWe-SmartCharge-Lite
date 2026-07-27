import sqlite3
from datetime import datetime
from interface.tarifas import calcular_valor

def conectar():

    conexao = sqlite3.connect("database/carregadores.db")

    return conexao

def criar_tabela():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carregadores (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nome TEXT NOT NULL,

            potencia INTEGER NOT NULL,

            status TEXT NOT NULL

        )
    """)

    conexao.commit()

    conexao.close()

def criar_tabela_sessoes():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessoes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            carregador_id INTEGER NOT NULL,

            veiculo TEXT NOT NULL,

            inicio TEXT NOT NULL,

            fim TEXT,

            energia REAL,

            valor REAL,

            status TEXT NOT NULL,

            FOREIGN KEY (carregador_id)
                REFERENCES carregadores(id)

        )
    """)

    conexao.commit()

    conexao.close()

def inserir_carregador(nome, potencia, status):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO carregadores
        (nome, potencia, status)

        VALUES (?, ?, ?)
    """, (nome, potencia, status))

    conexao.commit()

    conexao.close()

def listar_carregadores():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM carregadores
    """)

    resultados = cursor.fetchall()

    conexao.close()

    carregadores = []

    for linha in resultados:

        carregador = {
            "id": linha[0],
            "nome": linha[1],
            "potencia": linha[2],
            "status": linha[3]
        }

        carregadores.append(carregador)

    return carregadores

def mostrar_banco():

    carregadores = listar_carregadores()

    print("\n=== BANCO DE DADOS ===")

    for carregador in carregadores:
        print(carregador)

    print("======================\n")

def atualizar_carregador(id, nome, potencia, status):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE carregadores

        SET
            nome = ?,
            potencia = ?,
            status = ?

        WHERE id = ?
    """, (nome, potencia, status, id))

    conexao.commit()

    conexao.close()

def excluir_carregador(id):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM carregadores
        WHERE id = ?
    """, (id,))

    conexao.commit()

    conexao.close()

def listar_carregadores_livres():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM carregadores
        WHERE status = 'Livre'
    """)

    resultados = cursor.fetchall()

    conexao.close()

    carregadores = []

    for linha in resultados:

        carregadores.append({
            "id": linha[0],
            "nome": linha[1],
            "potencia": linha[2],
            "status": linha[3]
        })

    return carregadores

def iniciar_sessao(carregador_id, veiculo):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO sessoes(
            carregador_id,
            veiculo,
            inicio,
            status
        )
        VALUES (?, ?, ?, ?)
    """, (
        carregador_id,
        veiculo,
        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Em andamento"
    ))

    cursor.execute("""
        UPDATE carregadores
        SET status = 'Ocupado'
        WHERE id = ?
    """, (carregador_id,))

    conexao.commit()

    conexao.close()

def listar_sessoes():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            sessoes.id,
            carregadores.nome,
            sessoes.veiculo,
            sessoes.inicio,
            sessoes.fim,
            sessoes.energia,
            sessoes.valor,
            sessoes.status
        FROM sessoes
        INNER JOIN carregadores
            ON carregadores.id = sessoes.carregador_id
        ORDER BY sessoes.id DESC
    """)

    resultados = cursor.fetchall()

    conexao.close()

    sessoes = []

    for linha in resultados:
        
        sessoes.append({

            "id": linha[0],
            "carregador": linha[1],
            "veiculo": linha[2],
            "inicio": linha[3],
            "fim": linha[4],
            "energia": linha[5],
            "valor": linha[6],
            "status": linha[7]

        })

    return sessoes

def encerrar_sessao(sessao_id):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT carregador_id, inicio
        FROM sessoes
        WHERE id = ?
    """, (sessao_id,))

    carregador_id, inicio = cursor.fetchone()

    inicio = datetime.strptime(
        inicio,
        "%d/%m/%Y %H:%M:%S"
    )

    fim = datetime.now()

    horas = (fim - inicio).total_seconds() / 3600

    cursor.execute("""
        SELECT potencia
        FROM carregadores
        WHERE id = ?
    """, (carregador_id,))

    potencia = cursor.fetchone()[0]

    energia = round(potencia * horas, 2)

    valor = calcular_valor(energia)

    cursor.execute("""
        UPDATE sessoes
        SET
            fim = ?,
            energia = ?,
            valor = ?,
            status = 'Finalizada'
        WHERE id = ?
    """, (
        fim.strftime("%d/%m/%Y %H:%M:%S"),
        energia,
        valor,
        sessao_id
    ))

    cursor.execute("""
        UPDATE carregadores
        SET status='Livre'
        WHERE id=?
    """, (carregador_id,))

    conexao.commit()

    conexao.close()

def obter_estatisticas():

    conexao = conectar()

    cursor = conexao.cursor()

    # Total de carregadores
    cursor.execute("SELECT COUNT(*) FROM carregadores")
    total = cursor.fetchone()[0]

    # Livres
    cursor.execute("""
        SELECT COUNT(*)
        FROM carregadores
        WHERE status='Livre'
    """)
    livres = cursor.fetchone()[0]

    # Ocupados
    cursor.execute("""
        SELECT COUNT(*)
        FROM carregadores
        WHERE status='Ocupado'
    """)
    ocupados = cursor.fetchone()[0]

    # Manutenção
    cursor.execute("""
        SELECT COUNT(*)
        FROM carregadores
        WHERE status='Manutenção'
    """)
    manutencao = cursor.fetchone()[0]

    # Energia total
    cursor.execute("""
        SELECT SUM(energia)
        FROM sessoes
        WHERE status='Finalizada'
    """)

    energia = cursor.fetchone()[0]

    if energia is None:
        energia = 0

    # Receita total
    cursor.execute("""
        SELECT SUM(valor)
        FROM sessoes
        WHERE status='Finalizada'
    """)

    receita = cursor.fetchone()[0]

    if receita is None:
        receita = 0

    conexao.close()

    return {
        "carregadores": total,
        "livres": livres,
        "ocupados": ocupados,
        "manutencao": manutencao,
        "energia": round(energia, 2),
        "receita": round(receita, 2)
    }