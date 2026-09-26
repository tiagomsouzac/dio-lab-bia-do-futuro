# Base de Conhecimento

## Dados Utilizados

Os dados utilizados pelo Caju estão armazenados na pasta `data` em arquivos JSON. Eles são utilizados como uma base de conhecimento para que o agente consiga analisar a situação financeira do usuário e fornecer respostas de acordo com os dados disponíveis.

| Arquivo | Formato | O que Caju faz? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Aqui ele conhece melhor como você interage |
| `perfil_investidor.json` | JSON | Aqui ele vê tudo o que você investe |
| `produtos_financeiros.json` | JSON |Aqui ele te mostra tipos de investimento |
| `transacoes.csv` | CSV | Aqui ele vê como funciona suas entradas e saídas |

---

## Adaptações nos Dados

Os dados mockados foram adaptados para que o Caju pudesse trabalhar principalmente com controle e organização financeira.

O arquivo `perfil_investidor.json` foi expandido para incluir informações como:

- Despesas mensais separadas por categoria;
- Dívidas;
- Total de despesas;
- Saldo mensal estimado;
- Valor atual e objetivo da reserva de emergência;
- Metas financeiras;
- Preferências e objetivo principal do usuário.

O arquivo `produtos_financeiros.json` também foi adaptado. As informações foram estruturadas com foco educacional, permitindo que Caju explique conceitos como renda fixa, renda variável, risco e liquidez sem recomendar diretamente um investimento ao usuário.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON da pasta `data` são carregados pelo agente e disponibilizados como contexto para o LLM durante a interação.

O `perfil_investidor.json` fornece os dados financeiros do usuário, enquanto o `produtos_financeiros.json` funciona como uma base de informações educacionais sobre produtos financeiros.

### Como os dados são usados no prompt?

Os dados são inseridos no contexto enviado ao LLM juntamente com as instruções de comportamento do Caju.

O agente utiliza os dados disponíveis para responder às perguntas do usuário, realizar cálculos e apresentar análises financeiras.

O Caju deve utilizar somente as informações disponíveis na base de conhecimento e na conversa atual. Caso não possua informações suficientes para responder, deve informar essa limitação em vez de inventar dados.

Além disso, informações presentes em `produtos_financeiros.json` são utilizadas apenas para fins educacionais, não sendo utilizadas para recomendar investimentos específicos.

---

## Exemplo de Contexto Montado

> Exemplo simplificado de como os dados podem ser apresentados ao agente:

```text
Dados do Cliente:

Nome: João Silva
Idade: 32 anos
Profissão: Analista de Sistemas

Renda mensal: R$ 5.000,00

Despesas mensais:
- Moradia: R$ 1.500,00
- Alimentação: R$ 800,00
- Transporte: R$ 500,00
- Contas básicas: R$ 400,00
- Saúde: R$ 200,00
- Lazer: R$ 300,00
- Assinaturas: R$ 100,00
- Outros: R$ 200,00

Total de despesas: R$ 4.000,00
Saldo mensal estimado: R$ 1.000,00

Reserva de emergência:
- Valor atual: R$ 10.000,00
- Meta: R$ 15.000,00

Metas financeiras:
1. Completar reserva de emergência
   Valor necessário: R$ 15.000,00
   Prazo: 2027-03

2. Entrada do apartamento
   Valor necessário: R$ 50.000,00
   Prazo: 2027-12


Regras do Caju:
- Não inventar informações financeiras.
- Informar quando não houver dados suficientes.
- Não recomendar investimentos específicos.
- Não determinar quanto o usuário deve gastar.
- Utilizar os dados disponíveis para auxiliar no controle financeiro.
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
