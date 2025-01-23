# Construção e Análise de um Dataset de Horóscopos Diários

Este repositório reúne scripts e documentação para coletar, limpar e analisar textos de horóscopos diários obtidos do site [Horoscope.com](https://www.horoscope.com/). O objetivo é criar um conjunto de dados **organizado** e **anotado** (com valores de sentimento) para uso em projetos de Processamento de Linguagem Natural (NLP).

## Descrição Geral

1. **Coleta de Dados (Web Scraping)**  
   - Os horóscopos são coletados diariamente via Python, acessando as páginas de cada signo no site.  
   - As informações — data, signo e texto do horóscopo — são armazenadas em um formato tabular (CSV).

2. **Limpeza e Organização**  
   - O CSV é lido e convertido em um *DataFrame* do **pandas**, onde se remove duplicatas, linhas vazias e ruídos.  
   - O texto é padronizado (letras minúsculas, remoção de caracteres indesejados) para simplificar análises posteriores.

3. **Análise de Dados**  
   - **Análise de Sentimento (TextBlob)**: Mede a polaridade (positiva ou negativa) e subjetividade de cada horóscopo.  
   - **Frequência de Palavras**: Identifica termos mais comuns (após remoção de *stopwords*).  
   - **Visualização**: Geração de gráficos e nuvens de palavras para melhor compreensão dos resultados.
