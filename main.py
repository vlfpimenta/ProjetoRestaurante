import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Análise de Vendas de Bebidas')

# entrada dos dados via CSV
file_path = "ListaRestaurante.csv"
df = pd.read_csv(file_path)

df['Margem de Lucro (%)'] = ((df['PrecoVenda'] - df['PrecoCompra']) / df['PrecoCompra']) * 100      # coluna "margem de lucro" na exibição do DataFrame. precisa ser melhor formatada

st.write('## Visão Geral dos Dados')
st.write(df)

st.write('## Quantidade de Vendas por Produto')
bar_chart = st.bar_chart(df[['Produto', 'Quantidade']].set_index('Produto'))                        # gráfico de barras de quantidade de vendas

st.write('## Distribuição de Vendas por Produto')
fig, ax = plt.subplots()
ax.pie(df['Quantidade'], labels=df['Produto'], autopct='%1.1f%%', startangle=90)                    # gráfico de pizza de distribuição de vendas por produto
ax.axis('equal')
st.pyplot(fig)

produto_mais_caro = df.loc[df['PrecoVenda'].idxmax()]
produto_mais_barato = df.loc[df['PrecoVenda'].idxmin()]

st.write('## Produto Mais Caro')
st.write(produto_mais_caro)

st.write('## Produto Mais Barato')
st.write(produto_mais_barato)

# Comparação entre tipos de produtos
tipos_de_produtos = df['Produto'].apply(lambda x: x.split()[0]).unique()                            # primeiro termo do nome do produto

st.write('## Comparação entre Tipos de Produtos')
for tipo in tipos_de_produtos:
    produtos_do_tipo = df[df['Produto'].str.startswith(tipo)]
    st.write(f'### {tipo.capitalize()}s')
    st.write(produtos_do_tipo[['Produto', 'Quantidade', 'PrecoCompra', 'PrecoVenda', 'Margem de Lucro (%)']])

correlacao = df[['Quantidade', 'PrecoCompra', 'PrecoVenda', 'Margem de Lucro (%)']].corr()          # matriz de correlação

st.write('## Matriz de Correlação')
st.write(correlacao)

st.write('## Visualização da Matriz de Correlação (Heatmap)')
fig, ax = plt.subplots()
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
st.pyplot(fig)

# Scatter plot entre quantidade e preços
# st.write('## Scatter Plot entre Quantidade e Preços')
# scatter_plot = sns.pairplot(df[['Quantidade', 'PrecoCompra', 'PrecoVenda']])
# t.pyplot()