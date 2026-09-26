import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ MONTAR CONTEXTO ============
preferencias = perfil.get('preferencias', {})
reserva = perfil.get('reserva_emergencia', {})
metas = perfil.get('metas', [])

metas_texto = "\n".join(
    (
        f"- {meta.get('meta', 'Meta sem nome')}: "
        f"atual R$ {meta.get('valor_atual', 0):,.2f} / "
        f"meta R$ {meta.get('valor_necessario', 0):,.2f} "
        f"(prazo: {meta.get('prazo', 'N/A')})"
    )
    for meta in metas
) if metas else "- Nenhuma meta cadastrada."

contexto = f"""
CLIENTE:
- Nome: {perfil.get('nome', 'N/A')}
- Idade: {perfil.get('idade', 'N/A')} anos
- Profissão: {perfil.get('profissao', 'N/A')}
- Renda mensal: R$ {perfil.get('renda_mensal', 0):,.2f}
- Prioridade: {preferencias.get('prioridade', 'N/A')}
- Objetivo principal: {preferencias.get('objetivo_principal', 'N/A')}
- Aceita cortes: {preferencias.get('aceita_recomendacoes_de_cortes', 'N/A')}

OBJETIVOS FINANCEIROS:
{metas_texto}

PATRIMÔNIO:
- Patrimônio total: R$ {perfil.get('patrimonio_total', 0):,.2f}
- Reserva de emergência: R$ {reserva.get('valor_atual', 0):,.2f} / meta R$ {reserva.get('valor_meta', 0):,.2f}
- Meses de despesas cobertos: {reserva.get('meses_de_despesas', 0)}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False, justify='left')}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False, justify='left')}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============

SYSTEM_PROMPT = """Você é Caju, um agente de educação e organização financeira pessoal.

### QUEM VOCÊ É:
Você é um assistente financeiro virtual chamado Caju. Seu papel é ajudar pessoas a entender melhor seus próprios gastos, organizar sua vida financeira e acompanhar seus objetivos.

### OBJETIVO:
Seu principal objetivo é ajudar o usuário a:
- Entender para onde seu dinheiro está indo;
- Organizar suas receitas e despesas;
- Identificar quanto sobra ou falta após seus gastos;
- Acompanhar sua reserva de emergência;
- Acompanhar metas financeiras;
- Identificar possíveis excessos de gastos;
- Ter maior controle e consciência sobre sua vida financeira.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============ INTERFACE ============
st.title("💰 Caju, Seu Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))