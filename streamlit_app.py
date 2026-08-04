import streamlit as st

st.title("🎈hello alunos")
st.write("Bem-vindos ao nosso aplicativo Streamlit! Aqui você pode explorar diferentes funcionalidades e interagir com os dados de maneira intuitiva. Aproveite a experiência!")

import pandas as pd
# Exemplo de DataFrame
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [24, 30, 22, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}
df = pd.DataFrame(data)

# Definir região para cada cidade
regiao_por_cidade = {
    'São Paulo': 'Sudeste',
    'Rio de Janeiro': 'Sudeste',
    'Belo Horizonte': 'Sudeste',
    'Curitiba': 'Sul'
}
df['Região'] = df['Cidade'].map(regiao_por_cidade)

# Calcular porcentagem de alunos por região
regiao_contagem = df['Região'].value_counts().rename_axis('Região').reset_index(name='Alunos')
regiao_contagem['Porcentagem'] = (regiao_contagem['Alunos'] / regiao_contagem['Alunos'].sum() * 100).round(1)

st.subheader('Tabela de Alunos')
st.table(df)

st.subheader('Porcentagem de alunos por região')
st.table(regiao_contagem)

st.bar_chart(regiao_contagem.set_index('Região')['Alunos'])

