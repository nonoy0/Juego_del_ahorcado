# PROYECTO: Juego del Ahorcado
# ESTUDIANTE: Mateo de la Bastida
# FASE: 1 - Configuración del Entorno y Estructura

import random

def main():
    print("--- INICIANDO SISTEMA ---")
    
    # ---------------------------------------------------------
    # CAPA DE DATOS [Referencia a tu documento: Banco de Palabras]
    # Se implementa la Alternativa C: Banco interno predefinido.
    # ---------------------------------------------------------
    banco_palabras = ["ALGORITMO", "PYTHON", "SISTEMAS", "CODIGO"]
    print(f"[Sistema]: Banco de palabras cargado: {len(banco_palabras)} disponibles.")
    
    # ---------------------------------------------------------
    # CAPA DE LÓGICA [Referencia: Inicialización de variables]
    # Configuración inicial de contadores según requisitos.
    # ---------------------------------------------------------
    palabra_secreta = random.choice(banco_palabras)
    vidas_maximas = 6 
    letras_usadas = []
    
    # Verificación de ambiente para el desarrollador (tú)
    print(f"[Debug]: La palabra seleccionada para pruebas es: {palabra_secreta}")
    print(f"[Debug]: Vidas configuradas en: {vidas_maximas}")
    
    # ---------------------------------------------------------
    # CAPA DE PRESENTACIÓN (Avance)
    # ---------------------------------------------------------
    print("\nEl ambiente de desarrollo está listo.")
    print("Las librerías 'random' funcionan correctamente.")
    print("Esperando implementación del bucle principal en el Paso 2...")

if __name__ == "__main__":
    main()