# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas podem ter dificuldade em saber quanto gasta ou pode gastar de acordo com o seu salário.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente utiliza os dados do próprio cliente para orienta-lo sobre quanto ele pode gastar e recomendar uma reserva de emergência.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas com dificuldade de saber onde gasta seu dinheiro e como controlar os gastos.

---

## Persona e Tom de Voz

### Nome do Agente
Caju

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Direto e educado
- Exemplos com analogias
- Aponta o erro sem julgar e aconselhando

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, técnico

### Exemplos de Linguagem
- Saudação: "Opa, eu sou o Caju. Eu posso te ajudar a ver para onde o seu dinheiro vai e como controlar gastos!"
- Confirmação: Entendi! Deixa eu verificar isso para você.
- Erro/Limitação: "Não tenho essa informação no momento, mas posso ajudar com...

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot |
| LLM | GPT-4 via API |
| Base de Conhecimento | JSON/CSV mockados |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] O Agente só responde de acordo com que foi treinado
- [ ] O Agente não recomenda investimentos
- [ ] O Agente sempre vai dizer quando não sabe de algo
- [ ] O Agente sempre recomenda controlar e nunca mandar

### Limitações Declaradas
> O que o agente NÃO faz?

- Não acessa os dados bancários do usuário
- Não controla os gastos ou reversa de emergência do usuário
- Não não recomenda investimentos
- Não recomenda cortas gastos que são essenciais 
