import pandas as pd
import mysql.connector

def conectar_banco_dados(host, usuario, senha, banco_dados):
    try:
        conexao = mysql.connector.connect(
            host=host,
            user=usuario,
            password=senha,
            database=banco_dados
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

def obter_querys():
    print("Digite suas consultas uma por vez. Digite 'fim' quando terminar.\n")
    querys = []
    while True:
        consulta = input("Insira sua consulta (ou pule linhas para continuar): ").strip()
        if consulta.lower() == "fim":
            break
        querys.append(consulta)
    return querys

def remover_linhas_duplicadas(df):
    resposta = input("Deseja remover linhas duplicadas? (s/n): ").strip().lower()
    if resposta == "s":
        df.drop_duplicates(inplace=True)
    return df

def remover_colunas_vazias(df):
    resposta = input("Deseja remover colunas vazias? (s/n): ").strip().lower()
    if resposta == "s":
        df.dropna(axis=1, how='all', inplace=True)
    return df

def gerar_arquivo_csv(df, nome_arquivo):
    delimitador = input("Digite o delimitador desejado para o arquivo CSV (ex: ',' ou ';'): ").strip()
    df.to_csv(nome_arquivo, sep=delimitador, index=False)
    print(f"Arquivo {nome_arquivo} gerado com sucesso!")

def main():
    host = input("Digite o endereço do servidor MySQL: ")
    usuario = input("Digite o nome de usuário do MySQL: ")
    senha = input("Digite a senha do MySQL: ")
    banco_dados = input("Digite o nome do banco de dados: ")

    conexao = conectar_banco_dados(host, usuario, senha, banco_dados)
    if conexao:
        querys = obter_querys()
        for i, query in enumerate(querys, 1):
            cursor = conexao.cursor()
            try:
                cursor.execute(query)
                colunas = [i[0] for i in cursor.description]
                dados = cursor.fetchall()
                if dados:
                    df = pd.DataFrame(dados, columns=colunas)
                    df = remover_linhas_duplicadas(df)
                    df = remover_colunas_vazias(df)
                    nome_arquivo = f"resultado_query_{i}.csv"
                    gerar_arquivo_csv(df, nome_arquivo)
                else:
                    print("A consulta não retornou resultados.")
            except mysql.connector.Error as err:
                print(f"Erro ao executar a consulta: {err}")
            finally:
                cursor.close()
        conexao.close()

if __name__ == "__main__":
    main()
