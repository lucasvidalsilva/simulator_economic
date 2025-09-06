# 🏦 simulator_economic
**Motor de Simulação Econômica com Databricks e PySpark**

## Contexto
Bancos, fintechs e consultorias precisam avaliar **impactos** macroecômicos em suas carteiras de crédito.
Mas o que isso significa afinal?

Os elementos mencionados não podem olhar só para um cliente individual ou para o contrato de crédito em si.
Pois o dinheiro que emprestam está inserido dentro de uma engrenagem maior: a economia. Se o cenário 
macroecômico muda, juros sobem, desemprego cresce, inflação aperta. 

Esse projeto busca implementar um **simuladador econômico em larga escala**, rodando em **PySpark + Delta Lake**,
capaz de criar cenários e calcular impactos nos indicadores financeiros. 

## Objetivo do Projeto
* Ingerir séries históricas econômicas (Selic, IPCA, inadimplência, crédito)
* Estruturar camadas **Broze** -> **Silver** -> **Gold** no Delta Lake.
* Permitir **simulações parametrizadas** (Ex: "Selic +1,5 p.p.")
* Gerar tabelas de saída com indicadores projetados.
* Disponibilizar resultados para **dashboard** e **consulta**.

## Exemplos de Cenários Simulados (Exemplos)
1. **Cenário Selic**
* Pergunta: "Se a Selic subir de 10,5% para 12,0%?"
* Resultado: acontece x com a inadimplência e o crédito total fica y.
2. **Cenário Inflação**
* Pergunta: "E se o IPCA subir 2 p.p.?"
* Resultado: consume diminui, inadimplência cresce...
3. **Cenário de Estresse Econômico**
* Pergunta: "O que acontece se o desemprego aumentar 3% e o PIB cair?"
* Resultado: liquidez bancária reduz e inadimplência alta..

## Arquitetura
1. **Bases Públicas** (SGS Bacen, ESTBAN, IBGE, B3).
2. <span style="color: brown;">Bronze</span>: Ingestão bruta.
3. <span style="color: silver;">Silver</span>: Tratamento, validação, normalização de séries.
4. <span style="color: orange;">Gold</span>: Cenários Simulados
5. **Dashboard App** (analise e consulta dos dados).

## Stack Tecnologia
* PySpark -> processamento distribuído.
* Delta Lake -> versionamento e consistência.
* Python (pandas, requests, streamlit) -> ingestão de APIs e visualização dos dados

## Como rodar localmente
...

## Inspiração
Esse projeto nasceu da ideia de usar a engenharia de dados não só para ETL, mas como **motor de inteligência consultiva**,
unido tecnologia e análise econômico.