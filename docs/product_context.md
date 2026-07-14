# Contexto do Produto

**Produto:** Assistente Virtual baseado em RAG para Atendimento de Serviços ao Cidadão
**Versão do documento:** 1.0
**Autor:** System/QA Engineering

---

## 1. Objetivo do Sistema

Fornecer um canal automatizado de atendimento que responda dúvidas de cidadãos sobre
serviços públicos (ex.: emissão de documentos, prazos, taxas, requisitos, horários de
atendimento, status de processos), utilizando arquitetura **RAG (Retrieval-Augmented
Generation)** para gerar respostas fundamentadas exclusivamente em uma base de
conhecimento aprovada (leis, portarias, manuais internos, FAQs oficiais).

**Objetivos específicos:**
- Reduzir tempo de espera e sobrecarga de atendimento humano em demandas de 1º nível.
- Garantir respostas rastreáveis e auditáveis (com citação de fonte).
- Minimizar risco de desinformação em serviços públicos.
- Disponibilizar atendimento 24/7 multicanal (web, WhatsApp, app).

---

## 2. Usuários

| Perfil | Descrição | Necessidade principal |
|---|---|---|
| Cidadão | Público geral solicitando informação sobre serviços | Respostas rápidas, claras e corretas |
| Atendente humano (backoffice) | Recebe casos escalados pelo assistente | Contexto completo da conversa + motivo do escalonamento |
| Administrador da base de conhecimento | Time responsável por manter/curar documentos-fonte | Painel de gestão de conteúdo, versionamento |
| Equipe de QA/Compliance | Audita respostas e conformidade | Logs, rastreabilidade, métricas de qualidade |

---

## 3. Funcionalidades

- Responder perguntas em linguagem natural sobre serviços públicos.
- Recuperar (retrieval) documentos relevantes da base de conhecimento aprovada.
- Gerar respostas (generation) fundamentadas nesses documentos, com citação da fonte.
- Indicar nível de confiança/incerteza na resposta.
- Escalar para atendimento humano quando não houver informação suficiente ou a
  confiança for baixa.
- Registrar logs de interação para auditoria (pergunta, documentos recuperados,
  resposta, feedback do usuário).
- Permitir feedback do cidadão (útil/não útil) para melhoria contínua.
- Suportar múltiplos canais (web, WhatsApp, app mobile).

---

## 4. Limitações

- O sistema **não substitui** decisão jurídica, administrativa ou processual — é
  apenas informativo.
- Não possui acesso a sistemas transacionais que exijam autenticação forte
  (ex.: abertura de processo em nome do cidadão), a menos que integrado explicitamente
  e com controle de identidade.
- A qualidade da resposta depende diretamente da cobertura e atualização da base de
  conhecimento (garbage in, garbage out).
- Não garante 100% de acurácia; respostas geradas por LLM podem conter erros
  residuais mesmo com RAG (mitigado, não eliminado).
- Não opera fora do domínio de serviços públicos definido no escopo (não é assistente
  de propósito geral).

---

## 5. Regras de Negócio

- RN-01: Toda resposta deve ser fundamentada em documentos da base de conhecimento
  aprovada; não é permitido gerar conteúdo baseado apenas no conhecimento paramétrico
  do modelo.
- RN-02: Toda resposta deve citar a(s) fonte(s) documental(is) utilizada(s).
- RN-03: Perguntas fora do domínio de serviços ao cidadão devem ser recusadas
  educadamente, com redirecionamento de escopo.
- RN-04: Solicitações envolvendo dados pessoais sensíveis de terceiros devem ser
  recusadas.
- RN-05: Quando a confiança da recuperação/geração estiver abaixo do limiar definido,
  o sistema deve escalar para atendimento humano em vez de "adivinhar".
- RN-06: Toda interação deve ser logada com metadados suficientes para auditoria
  (timestamp, documentos recuperados, versão da base, resposta gerada).
- RN-07: Atualizações na base de conhecimento devem passar por processo de aprovação
  antes de entrarem em produção (governança de conteúdo).

---

## 6. Comportamento Esperado

- Responder de forma clara, objetiva e no idioma do cidadão.
- Reconhecer quando não sabe a resposta e admitir a limitação, oferecendo
  escalonamento.
- Citar explicitamente a fonte (documento, artigo, seção) usada na resposta.
- Solicitar esclarecimento quando a pergunta for ambígua, em vez de assumir.
- Recusar-se educadamente diante de solicitações fora de escopo ou inadequadas,
  explicando o motivo.
- Manter neutralidade e tom institucional/respeitoso.

---

## 7. Comportamento Proibido

- Gerar respostas sem lastro documental (alucinação).
- Fornecer dados pessoais sensíveis de terceiros (CPF, endereço, saúde, dados
  financeiros de outra pessoa) mesmo que presentes na base.
- Emitir opinião pessoal, jurídica ou política sobre políticas públicas.
- Executar instruções embutidas em perguntas do usuário que tentem alterar seu
  comportamento, papel ou políticas de segurança (prompt injection).
- Inventar prazos, valores, número de protocolo ou status de processo não confirmados
  pela base de conhecimento/sistemas integrados.
- Prometer resultados de processos administrativos (ex.: "seu pedido será aprovado").

## 8. Escopo de Implementação do MVP

A visão de produto prevê suporte multicanal. Entretanto, o MVP deste projeto
implementará apenas o canal web.

Os canais WhatsApp e aplicativo mobile serão representados por contratos
de integração e cenários de teste, mas não serão implementados como interfaces
funcionais nesta versão.