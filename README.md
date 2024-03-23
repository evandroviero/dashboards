# Streamlit

## O que é o Streamlit?

O Streamlit é uma poderosa ferramenta para a criação rápida e fácil de aplicativos web interativos para análise de dados e visualização. Com ele, os usuários podem transformar rapidamente scripts Python em aplicativos web interativos, sem a necessidade de conhecimento extenso em desenvolvimento web.

## Principais recursos

### Execução a cada nova requisição

Uma das características marcantes do Streamlit é que a aplicação é reexecutada a cada nova requisição do usuário. Isso significa que as atualizações feitas no código são imediatamente refletidas na aplicação web, proporcionando uma experiência de desenvolvimento ágil e iterativa.

### Cache de objetos

O Streamlit oferece um sistema de cache integrado, permitindo que resultados computacionalmente intensivos sejam armazenados em memória. Isso ajuda a otimizar o desempenho da aplicação, garantindo que cálculos pesados sejam realizados apenas quando necessário.

### Compartilhamento de objetos com Session

Com a funcionalidade de sessão do Streamlit, é possível compartilhar objetos entre diferentes partes da aplicação, mesmo quando estão em páginas diferentes. Isso facilita a comunicação de dados e estados entre os diferentes componentes do aplicativo, garantindo uma experiência coesa para o usuário final.

## Como começar

Para começar a usar o Streamlit, siga estas etapas simples:

1. Instale o Streamlit usando pip:

```bash
pip install streamlit
```

1. Crie um novo arquivo Python para o seu aplicativo e importe o Streamlit:
```python
import streamlit as st
```
1.1 Escreva o código do seu aplicativo, adicionando widgets interativos, gráficos e qualquer outra funcionalidade desejada.
1.2 Execute o aplicativo usando o seguinte comando no terminal:
```bash
streamlit run seu_aplicativo.py
```
1.3 Visualize o seu aplicativo no navegador e interaja com ele!

### Exemplo
Aqui está um exemplo simples de um aplicativo Streamlit:
```python
import streamlit as st

st.title('Meu Primeiro Aplicativo Streamlit')
nome = st.text_input('Digite seu nome:', 'Evandro Viero')
st.write(f'Olá, {nome}! Bem-vindo ao Streamlit.')
```

### Comandos Básicos
    st.write(): renderiza objetos como tabela, textos, etc...
    st.dataframe(): dataframe com várias opções
    st.table(): tabela estática
    st.text_input(): permite aos usuários inserir texto em um campo de entrada.
    st.checkbox(): oferece aos usuários a capacidade de selecionar ou desmarcar uma opção.
    st.selectbox(): permite aos usuários selecionar uma opção a partir de uma lista suspensa.
    st.sidebar(): cria uma barra lateral na interface do aplicativo para adicionar controles ou seções separadas.
    st.columns(): divide a tela em colunas, permitindo a organização e o layout de elementos de forma mais flexível.
    st.expander(): cria um contêiner expansível que oculta ou exibe seu conteúdo, proporcionando uma maneira de apresentar informações de forma condensada.

### Documentação
Para saber mais sobre o Streamlit e suas funcionalidades, consulte a [documentação oficial](https://streamlit.io).