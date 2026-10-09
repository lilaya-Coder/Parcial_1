# Solución de IA para LogiTech Chile S.A. (RAG & Agentes)

**Asignatura:** Ingeniería de Soluciones con IA (ISY0101)  
**Evaluación:** Evaluación Parcial N°1 — Duoc UC 2025  
**Integrantes:** Lisandro Laya  

---

##  Descripción del Proyecto
Sistema inteligente de asistencia para soporte postventa basado en **Agentes LLM (ReAct)** y una arquitectura **RAG (Retrieval-Augmented Generation)**. Permite responder consultas sobre garantías y manuales técnicos en PDF, además de consultar el estado de pedidos mediante APIs estructuradas.

---

##  Requisitos Previos e Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/lilaya-Coder/Parcial_1.git
   cd Parcial_1
   
   python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
OPENAI_API_KEY=tu_api_key_aqui
python SRC/main.py
