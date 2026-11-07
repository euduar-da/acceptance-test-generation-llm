### UTILIZAÇÃO DA INTELIGÊNCIA ARTIFICIAL NA GERAÇÃO DE CENÁRIOS DE TESTE DE ACEITAÇÃO

### Este repositório reúne os materiais, códigos e resultados do Trabalho de Conclusão de Curso (TCC) que investiga a utilização de Modelos de Linguagem de Grande Escala (LLMs) na geração de cenários de teste de aceitação em Gherkin, a partir de histórias de usuário (User Stories).

### O estudo analisa a capacidade de diferentes modelos de linguagem de produzir cenários de teste, considerando a similaridade com cenários de referência, a conformidade sintática e a percepção de profissionais da área de qualidade de software.

## Metodologia

A pesquisa foi conduzida por meio de um estudo experimental, utilizando **45 histórias de usuário** selecionadas do conjunto de dados de Dalpiaz (2018).

### Modelos de linguagem

Foram considerados três modelos de linguagem:

- **ChatGPT**
- **Gemini**
- **Claude**

### Estratégias de prompting

A geração dos cenários foi realizada utilizando três estratégias de *prompting*:

- **Zero-shot:** geração de cenários sem o fornecimento de exemplos.
- **One-shot:** geração de cenários com o fornecimento de um exemplo.
- **Few-shot:** geração de cenários com o fornecimento de múltiplos exemplos.

## Avaliação dos Cenários

A avaliação foi organizada em três etapas:

### 1. Similaridade textual

Os cenários gerados foram comparados com cenários de referência utilizando duas métricas automáticas:

- **BERTScore:** avalia a similaridade contextual entre os textos.
- **METEOR:** avalia a correspondência textual entre os cenários gerados e os cenários de referência.

### 2. Validação sintática

Foi utilizada a ferramenta **Gherkin-lint** para verificar a conformidade dos cenários gerados com as regras sintáticas e de estilo configuradas.

A partir dessa verificação, foi calculada a **Acurácia de Validação**, correspondente à proporção de arquivos `.feature` que não apresentaram erros na validação.

### 3. Avaliação com profissionais

Foi aplicado um formulário a profissionais da área de qualidade de software, com o objetivo de investigar suas percepções sobre a utilização de LLMs na elaboração de cenários de teste de aceitação.

Adicionalmente, os participantes avaliaram **três cenários gerados**, considerando os seguintes aspectos:

- **Clareza:** facilidade de compreensão dos cenários.
- **Completude:** presença de informações suficientes para representar o comportamento esperado.
- **Aplicabilidade:** possibilidade de utilização dos cenários no contexto prático de testes de software.

Essa etapa buscou complementar as avaliações automáticas, considerando a perspectiva de profissionais da área.

### Objetivo

Analisar os impactos positivos e negativos do uso de inteligência artificial na geração automatizada de cenários de teste de aceitação em Gherkin, considerando aspectos como qualidade, consistência e aplicabilidade a partir de requisitos descritos em linguagem natural