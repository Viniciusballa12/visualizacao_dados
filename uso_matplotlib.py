import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())

#Gráficos de Barras
plt.figure(figsize=(10, 6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Divisão de escolaridade - 1')
plt.xlabel('Nivel de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisão de Escolaridade - 2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')

#Gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.2f%%', startangle=180)
plt.title('Distribuição de Nivel de Educação')
plt.show()

#Grafico de Dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.title('Dispersão de Idade e Salario')
plt.show()

#Criar o gráfico de pizza
plt.figure(figsize=(8, 8))














