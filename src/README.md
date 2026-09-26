# Código da Aplicação

Esta pasta contém a aplicação principal do agente financeiro em Streamlit.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal do chatbot financeiro
├── README.md           # Documentação da pasta src
└── ...                 # Futuras extensões da aplicação
```

## Exemplo de requirements.txt

```txt
streamlit
pandas
requests
```

## Como Rodar

```bash
# A partir da raiz do projeto
python -m streamlit run .\src\app.py
```

> O arquivo `app.py` referencia dados localizados na pasta `data`, por isso a execução deve ocorrer a partir da raiz do repositório para manter os caminhos corretos.

### Rodando o modelo localmente com Ollama

Para que a aplicação funcione no modo local, o modelo precisa estar sendo executado no computador antes de abrir a interface.

```bash
# 1) Instale o Ollama e depois baixe o modelo configurado na aplicação
ollama pull gpt-oss

# 2) Inicie o servidor local do Ollama
ollama serve
```

Em outro terminal, rode a aplicação:

```bash
python -m streamlit run .\src\app.py
```

A aplicação está configurada para chamar o endpoint local do Ollama em `http://localhost:11434/api/generate` com o modelo `gpt-oss`.

Se o modelo não aparecer na lista local, use:

```bash
ollama list
```

Se necessário, baixe novamente:

```bash
ollama pull gpt-oss
```
