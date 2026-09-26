# Caju

Caju é um agente financeiro pessoal criado para ajudar o usuário a entender melhor seus gastos, controlar receitas e despesas, acompanhar metas e pensar de forma mais consciente sobre sua vida financeira.

O projeto combina duas camadas:

1. a lógica do agente, com regras, persona, guardrails e habilidades;
2. a aplicação em Streamlit, que transforma esse agente em um chatbot funcional para uso direto.

---

## Como o agente funciona

O agente usa a base de conhecimento do projeto para responder de forma contextualizada e segura. Os dados vêm de arquivos em [data](data), como:

- [data/perfil_investidor.json](data/perfil_investidor.json): perfil do cliente, renda, despesas, metas, patrimônio e reserva;
- [data/transacoes.csv](data/transacoes.csv): entradas e saídas financeiras;
- [data/historico_atendimento.csv](data/historico_atendimento.csv): histórico de conversa e contexto anterior;
- [data/produtos_financeiros.json](data/produtos_financeiros.json): conceitos gerais para apoio educativo.

A regra principal do agente é simples: ele só deve responder com base em dados reais disponíveis no projeto ou na conversa atual. Se faltarem informações, ele informa a limitação em vez de inventar respostas.

A estrutura do agente está em:

- [AGENTS.md](AGENTS.md): definição de papel, regras, guardrails e escopo;
- [agent/persona.md](agent/persona.md): personalidade do agente;
- [agent/knownledge](agent/knownledge): base de conhecimento interna do agente;
- [skills](skills): habilidades do agente, como análise de gastos, finanças pessoais e acompanhamento de metas.

---

## Como o programa funciona

A aplicação principal fica em [src/app.py](src/app.py). Ela:

- carrega os dados do cliente e do histórico;
- monta um contexto estruturado para o modelo;
- envia esse contexto para o modelo local do Ollama;
- retorna a resposta em uma interface interativa em Streamlit.

O fluxo principal é:

1. o usuário escreve uma pergunta sobre finanças;
2. a aplicação reúne os dados do perfil, transações e históricos;
3. o prompt do agente combina instruções de comportamento com o contexto do cliente;
4. o modelo local gera uma resposta;
5. a resposta é exibida na interface do chat.

A parte do programa foi pensada para funcionar com modelo local, usando o Ollama na porta padrão.

---

## Como rodar localmente

Antes de iniciar a aplicação, o modelo local precisa estar funcionando.

### 1. Instalar o Ollama

Baixe e instale o Ollama no computador.

### 2. Baixar o modelo

```bash
ollama pull gpt-oss
```

### 3. Iniciar o servidor local

```bash
ollama serve
```

### 4. Rodar a aplicação

A partir da raiz do projeto:

```bash
python -m streamlit run .\src\app.py
```

A aplicação está configurada para acessar o endpoint local do Ollama em http://localhost:11434/api/generate, usando o modelo gpt-oss.

---

## Estrutura do projeto

```text
repo/
├── AGENTS.md
├── README.md
├── data/
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
├── agent/
│   ├── knownledge/
│   └── persona.md
├── skills/
│   ├── 01-financas-pessoais.md
│   ├── 02-analise-de-gastos.md
│   └── 03-metas-financeiras.md
├── src/
│   ├── app.py
│   └── README.md
├── assets/
├── examples/
└── .git/
```

---

## Objetivo final

Este projeto une educação financeira, IA generativa e prototipagem de interface para criar um assistente útil, acessível e seguro, com foco em organização financeira pessoal e acompanhamento de objetivos do cliente.

A intenção não é recomendar investimentos específicos nem substituir profissionais, mas sim dar clareza, orientação e suporte para a tomada de decisão com responsabilidade.
