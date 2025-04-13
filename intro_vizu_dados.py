import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pyparsing import alphas

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

#Histograma
plt.hist(df['salario'])
plt.show()

#Histograma - Parâmentro
plt.figure(figsize=(10, 6))
plt.hist(df['salario'],bins=100, color='red', alpha=0.8)
plt.title('Histograma - Distribuição de Salários')
plt.xlabel('salario')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

#Múltiplos gráficos
plt.figure(figsize=(10,6))
plt.subplot(2, 2, 1) # 2 linha, 2 colunas, 1 gráfico
#Gráfico de Dispersão
plt.scatter(df['salario'], df['salario'], color='#48f205', alpha=0.6, s=30)
plt.title('Dispersão - Idade e Anos de Experiência')
plt.xlabel('salario')
plt.ylabel('Anos de Experiência')

plt.subplot( 1,2,2)
plt.scatter(df['salario'], df['anos_experiencia'], color='#48f205', alpha=0.6, s=30)
plt.title('Dispersão - Idade e Anos de Experiências')
plt.xlabel('Salário')
plt.ylabel('Salário')

#Mapa de calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2,3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salários e Idade')

plt.tight_layout()
plt.show()