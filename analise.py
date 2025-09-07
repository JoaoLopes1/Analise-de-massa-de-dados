import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega o arquivo CSV para um DataFrame do pandas.
try:
    df = pd.read_csv('core_data_202509030929.csv')
    print("Arquivo carregado com sucesso!")
except FileNotFoundError:
    print("Erro: O arquivo 'core_data_202509030929.csv' não foi encontrado.")
    exit()


# Função para extrair e processar os dados da coluna 'data'
def parse_data_column(data_str):
    """
    Processa a string JSON da coluna 'data', extraindo o 'error'
    e os 6 valores de 'result'.
    """
    try:
        data_dict = json.loads(data_str)
        error = data_dict.get('error')
        result_str = data_dict.get('result')
        if result_str:
            # Converte os valores de 'result' para float
            result_parts = [float(x) for x in result_str.split(',')]
        else:
            result_parts = [None] * 6
        return [error] + result_parts
    except (json.JSONDecodeError, AttributeError, ValueError):
        # Retorna nulo se houver erro no processamento
        return [None] * 7

# Aplica a função na coluna 'data' para criar as novas colunas
parsed_data = df['data'].apply(parse_data_column)
df[['error', 'result_1', 'result_2', 'result_3', 'result_4', 'result_5', 'result_6']] = pd.DataFrame(parsed_data.tolist(), index=df.index)

# Converte a coluna 'register_datetime' para o formato de data e hora
df['register_datetime'] = pd.to_datetime(df['register_datetime'])

# Remove a coluna 'data' original, que não é mais necessária
df = df.drop(columns=['data'])

print("Limpeza e pré-processamento dos dados concluídos.")
print("Novas colunas criadas: 'error', 'result_1' a 'result_6'")



# Gera estatísticas descritivas para as novas colunas
print("\n--- Estatísticas Descritivas ---")
print(df[['result_1', 'result_2', 'result_3', 'result_4', 'result_5', 'result_6']].describe())

# Verifica os valores na coluna 'error'
print("\n--- Contagem de Valores na Coluna 'error' ---")
print(df['error'].value_counts())


print("\nGerando visualizações...")

# Histograms para cada coluna 'result'
plt.figure(figsize=(15, 10))
for i, col in enumerate(['result_1', 'result_2', 'result_3', 'result_4', 'result_5', 'result_6'], 1):
    plt.subplot(2, 3, i)
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribuição de {col}')
    plt.xlabel(col)
    plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('result_distributions.png')
plt.close()
print("- Gráfico de distribuições salvo como 'result_distributions.png'")

# Gráfico de Série Temporal para 'result_4'
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='register_datetime', y='result_4')
plt.title('Série Temporal de result_4')
plt.xlabel('Data')
plt.ylabel('result_4')
plt.grid(True)
plt.savefig('result_4_time_series.png')
plt.close()
print("- Gráfico de série temporal salvo como 'result_4_time_series.png'")


# Mapa de Calor de Correlação
plt.figure(figsize=(10, 8))
correlation_matrix = df[['result_1', 'result_2', 'result_3', 'result_4', 'result_5', 'result_6']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor de Correlação das Variáveis Result')
plt.savefig('correlation_heatmap.png')
plt.close()
print("- Mapa de calor de correlação salvo como 'correlation_heatmap.png'")

print("\nAnálise concluída!")