# -*- coding: utf-8 -*-
"""populations_2023.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T-05TRVTNOZnXJNNZwcZOOhRuYsIN2D8
"""

# Commented out IPython magic to ensure Python compatibility.
# Visual Python: Data Analysis > Import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import plotly.express as px
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

# Visual Python: Data Analysis > File
df = pd.read_csv('/content/world_city_populations_2023.csv')
df

del df['Unnamed: 7']

df

df_20 = df.head(20)

del df_20['Unnamed: 7']

# Visual Python: Visualization > Seaborn
plt.figure(figsize=(15, 6))
sns.barplot(data=df_20, x='City', y='Pop2023')
plt.xticks(fontsize=7)
plt.xlabel('20 Maiores cidades ')
plt.ylabel('População 2023')
plt.title('20 Maiores Cidades de 2023')
plt.ticklabel_format(style='plain', axis='y')
plt.yticks([0, 5_000_000, 10_000_000, 15_000_000, 20_000_000, 25_000_000, 30_000_000, 35_000_000],
           ['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M'])
plt.show()

df_pop_2023 = df['Pop2023']

df_pop_2022 = df['Pop2022']

cidades = df['City']

aggregated_data = df.groupby('Continent')['Pop2023'].sum()
cores = ['Aqua', 'DarkTurquoise']
plt.pie(aggregated_data, labels=aggregated_data.index, autopct='%1.1f%%', colors=cores)
plt.title('População em 2023 por Continente')
plt.show()

# DataFrame com os dados
# Supondo que seu DataFrame seja chamado "df" com as colunas "Pop2023" e "Continent"

# Verificar a contagem de ocorrências de cada continente
continent_count = df['Continent'].value_counts()

# Imprimir a contagem de ocorrências
print(continent_count)

continent_values = df['Continent'].unique()

if 'North America' in continent_values:
    print('Tem')
else:
    print('Não tem')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# DataFrame com os dados
# Supondo que seu DataFrame seja chamado "df" com as colunas "Pop2022", "Pop2023" e "City"

# Ordenar o DataFrame pela população de 2023 em ordem decrescente
df_sorted = df.sort_values(by='Pop2023', ascending=False)

# Selecionar as 10 maiores cidades
df_top_10 = df_sorted.head(10)

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 6))

# Definir a largura das barras
bar_width = 0.35

# Definir os índices das barras
bar_indexes = np.arange(len(df_top_10))

# Plotar as barras de 2022 (laranja)
ax.bar(bar_indexes, df_top_10['Pop2022'], width=bar_width, color='MediumSlateBlue', label='2022')

# Plotar as barras de 2023 (azul)
ax.bar(bar_indexes + bar_width, df_top_10['Pop2023'], width=bar_width, color='MediumPurple', label='2023')

# Definir o título do gráfico
ax.set_title('População de 2022 e 2023 das 10 Maiores Cidades')

# Definir o rótulo do eixo x
ax.set_xlabel('Cidades')

# Definir o rótulo do eixo y
ax.set_ylabel('População')

# Definir os rótulos do eixo x
ax.set_xticks(bar_indexes + bar_width / 2)
ax.set_xticklabels(df_top_10['City'])

# Girar os rótulos do eixo x em 45 graus para melhorar a legibilidade
plt.xticks(rotation=45, ha='right')

# Adicionar uma legenda
ax.legend()

# ax.set_facecolor('lightgray')

# Ajustar o espaçamento entre as barras
plt.tight_layout()

plt.yticks([0, 5_000_000, 10_000_000, 15_000_000, 20_000_000, 25_000_000, 30_000_000, 35_000_000],
           ['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M'])

# Mostrar o gráfico
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# DataFrame com os dados
# Supondo que seu DataFrame seja chamado "df" com as colunas "Pop2022", "Pop2023" e "City"

# Calcular a diferença entre as populações de 2022 e 2023
df['Diff'] = df['Pop2023'] - df['Pop2022']

# Calcular a porcentagem de diminuição de população
df['Percentage'] = (df['Diff'] / df['Pop2022']) * 100

# Ordenar o DataFrame pela diferença em ordem decrescente
df_sorted = df.sort_values(by='Diff', ascending=True)

# Selecionar as 10 cidades que mais perderam população
df_top_10_decrease = df_sorted.head(10)

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 6))

# Definir a largura das barras
bar_width = 0.35

# Definir os índices das barras
bar_indexes = np.arange(len(df_top_10_decrease))

# Cores para as barras
color1 = '#B0E0E6'  # Cor 1 para 2022 (azul escuro)
color2 = '#E0FFFF'  # Cor 2 para 2023 (azul)

# Plotar as barras de 2022
ax.bar(bar_indexes, df_top_10_decrease['Pop2022'], width=bar_width, color=color1, label='2022')

# Plotar as barras de 2023
ax.bar(bar_indexes + bar_width, df_top_10_decrease['Pop2023'], width=bar_width, color=color2, label='2023')

for i, v in enumerate(df_top_10_decrease.index):
    ax.text(i + bar_width/2, df_top_10_decrease['Pop2022'].iloc[i] + 100000, f'{df_top_10_decrease["Percentage"].iloc[i]:.2f}%', ha='center', color='black')

# Definir o título do gráfico
ax.set_title('População de 2022 e 2023 das 10 Cidades que Mais Perderam População')

# Definir o rótulo do eixo x
ax.set_xlabel('Cidades')

# Definir o rótulo do eixo y
ax.set_ylabel('População')

# Definir os rótulos do eixo x
ax.set_xticks(bar_indexes + bar_width / 2)
ax.set_xticklabels(df_top_10_decrease['City'], rotation=45, ha='right')

# Adicionar uma legenda
ax.legend()

ax.set_facecolor('Honeydew')

# Ajustar o espaçamento entre as barras
plt.tight_layout()

plt.yticks([0, 5_000_000, 10_000_000, 15_000_000, 20_000_000, 25_000_000, 30_000_000, 35_000_000],
           ['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M'])

# Mostrar o gráfico
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.ticker as ticker

# DataFrame com os dados
# Supondo que seu DataFrame seja chamado "df" com as colunas "Pop2022", "Pop2023", "City" e "Continent"

# Filtrar apenas as cidades da Europa
df_europe = df[df['Continent'] == 'Europe']

# Ordenar o DataFrame pela população de 2023 em ordem decrescente
df_sorted = df_europe.sort_values(by='Pop2023', ascending=False)

# Selecionar as 10 maiores cidades
df_top_10 = df_sorted.head(10)

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 6))

# Definir a largura das barras
bar_width = 0.35

# Definir os índices das barras
bar_indexes = range(len(df_top_10))

# Cores para as barras
# colors = sns.color_palette('muted', n_colors=2)
# Cores para as barras
color1 = '#00CED1'  # Cor 1
color2 = '#40E0D0'  # Cor 2

colors = [color1, color2]

# Plotar as barras de 2022
ax.bar(bar_indexes, df_top_10['Pop2022'], width=bar_width, color=colors[0], label='2022')

# Plotar as barras de 2023
ax.bar([i + bar_width for i in bar_indexes], df_top_10['Pop2023'], width=bar_width, color=colors[1], label='2023', alpha=0.8)

# Definir o título do gráfico
ax.set_title('População de 2022 e 2023 das 10 Maiores Cidades da Europa')

# Definir o rótulo do eixo x
ax.set_xlabel('Cidades')

# Definir o rótulo do eixo y
ax.set_ylabel('População')

# Definir os rótulos do eixo x
ax.set_xticks([i + bar_width/2 for i in bar_indexes])
ax.set_xticklabels(df_top_10['City'])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)


# Girar os rótulos do eixo x em 45 graus para melhorar a legibilidade
plt.xticks(rotation=45, ha='right')

# Exibir a porcentagem acima das barras
for i, v in enumerate(bar_indexes):
    percentage = ((df_top_10['Pop2023'].iloc[i] - df_top_10['Pop2022'].iloc[i]) / df_top_10['Pop2022'].iloc[i]) * 100
    text_y = min(df_top_10['Pop2023'].iloc[i] + 500000, df_top_10['Pop2023'].iloc[i] + 0.05 * df_top_10['Pop2023'].iloc[i])
    ax.annotate(f'{percentage:.2f}%',
                xy=(v + bar_width/2, df_top_10['Pop2023'].iloc[i]),
                xytext=(v + bar_width/2, text_y),
                ha='center',
                color='black',
                arrowprops=dict(arrowstyle='-', lw=0.8))

# Adicionar uma legenda
ax.legend()

# Formatar o eixo y para exibir números inteiros separados por vírgulas
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.grid(False)
style={'border': '1px solid white', 'backgroundColor': 'rgba(0,0,0,0)'},  # Remove a linha do retângulo e define o fundo como transparente ou branco

# Ajustar o espaçamento entre as barras
plt.tight_layout()

plt.show()

df_cidades_coun = df[['City', 'Country']]
