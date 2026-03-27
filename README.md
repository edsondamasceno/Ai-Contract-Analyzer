
# 🤖 AI Contract Analyzer

## 📌 Visão Geral
Sistema completo de IA para análise automatizada de contratos utilizando **LLMs (Large Language Models)**, **RAG (Retrieval-Augmented Generation)** e **processamento assíncrono**.

Este projeto demonstra como construir uma **arquitetura escalável orientada a IA**, capaz de lidar com fluxos reais de documentos.

---

## 🚀 Funcionalidades

- 📄 Upload e análise de contratos em PDF
- 🧠 Geração automática de:
  - Resumo
  - Cláusulas principais
  - Análise de riscos
- ⚡ Processamento assíncrono com Celery + Redis
- 🔍 Busca semântica com RAG (FAISS)
- 🗄️ Persistência com PostgreSQL
- 🌐 Interface web com Streamlit
- 🐳 Execução via Docker (ambiente isolado)

---

## 🏗️ Arquitetura

```
Usuário (Streamlit)
        ↓
FastAPI (Backend)
        ↓
Celery (Processamento assíncrono)
        ↓
LLM (OpenAI API)
        ↓
PostgreSQL + FAISS (armazenamento e busca)
```

---

## 🧰 Tecnologias Utilizadas

- **Backend:** FastAPI
- **Frontend:** Streamlit
- **IA / LLM:** OpenAI API

