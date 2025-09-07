# Análise de Dados - Core Data

Script Python para análise exploratória de dados CSV com processamento de JSON aninhado e geração de visualizações estatísticas.

## Descrição

O script `analise.py` processa dados de sensores/medições armazenados em formato CSV, onde uma coluna contém dados JSON estruturados. Extrai valores numéricos, realiza limpeza de dados e gera visualizações para análise exploratória.

## Funcionalidades

- Carregamento e validação de arquivo CSV
- Processamento de dados JSON aninhados na coluna 'data'
- Extração de 6 valores numéricos (result_1 a result_6) e status de erro
- Conversão de timestamps para formato datetime
- Estatísticas descritivas das variáveis numéricas
- Análise de frequência de erros
- Geração de 3 tipos de visualizações

## Dependências

- pandas >= 1.3.0
- matplotlib >= 3.5.0
- seaborn >= 0.11.0

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

1. Coloque o arquivo `core_data_202509030929.csv` no mesmo diretório do script
2. Execute o script:

```bash
python analise.py
```

## Estrutura de Dados

O arquivo CSV deve conter:
- Coluna `data`: String JSON com formato `{"error": valor, "result": "val1,val2,val3,val4,val5,val6"}`
- Coluna `register_datetime`: Timestamp das medições

## Saídas

### Console
- Confirmação de carregamento
- Estatísticas descritivas (média, desvio padrão, quartis)
- Contagem de valores na coluna 'error'
- Progresso da geração de gráficos

### Arquivos Gerados
- `result_distributions.png`: Histogramas com KDE para cada variável
- `result_4_time_series.png`: Série temporal de result_4
- `correlation_heatmap.png`: Mapa de calor de correlações

## Estrutura do Projeto

```
Massa_de_dados/
├── analise.py
├── core_data_202509030929.csv
├── requirements.txt
├── README.md
├── result_distributions.png      (gerado)
├── result_4_time_series.png     (gerado)
└── correlation_heatmap.png      (gerado)
```

## Tratamento de Erros

- Verificação de existência do arquivo CSV
- Parsing robusto de JSON com fallback para valores nulos
- Conversão segura de tipos de dados
- Tratamento de valores ausentes ou inválidos

## Personalização

Para adaptar para outros dados:
1. Modifique o nome do arquivo na linha 8
2. Ajuste a função `parse_data_column()` se a estrutura JSON for diferente
3. Altere os parâmetros dos gráficos conforme necessário

## Exemplo de Dados

```csv
data,register_datetime
{"error": null, "result": "1.2,3.4,5.6,7.8,9.0,1.1"},2025-09-03 09:29:00
{"error": "sensor_fault", "result": "2.1,4.3,6.5,8.7,0.9,2.2"},2025-09-03 09:30:00
```
