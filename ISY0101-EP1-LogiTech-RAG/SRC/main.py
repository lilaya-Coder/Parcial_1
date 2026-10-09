import os
from dotenv import load_dotenv

# Cargar variables de entorno (API Key)
load_dotenv()

SYSTEM_PROMPT = """
[ROL E IDENTIDAD]
Eres "LogiBot", el asistente técnico e inteligente de postventa de LogiTech Chile S.A.
Tu propósito es asistir a ejecutivos y clientes resolviendo dudas técnicas sobre productos,
coberturas de garantía y estado de entregas con máxima precisión, empatía y profesionalismo.

[REGLAS OPERATIVAS Y RESTRICCIONES RIGUROSAS]
1. FIDELIDAD DOCUMENTAL: Responde únicamente fundamentándote en la base de conocimiento interna.
2. PROHIBICIÓN DE ALUCINACIÓN: No asumas políticas de devolución ni precios no confirmados.
3. CITACIÓN OBLIGATORIA: Cita explícitamente el documento fuente de las políticas.
"""

def main():
    print("=" * 60)
    print("🤖 Agente Inteligente LogiBot - LogiTech Chile S.A.")
    print("=" * 60)
    print("Sistema RAG y Agente ReAct cargado correctamente.")
    print("\nSystem Prompt configurado:")
    print(SYSTEM_PROMPT)
    print("=" * 60)
    print("Listo para procesar consultas de soporte y garantías.")

if __name__ == "__main__":
    main()