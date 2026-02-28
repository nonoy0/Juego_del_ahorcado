''' import random

def main():
    print("--- PROYECTO AHORCADO: AVANCE DE ESTRUCTURAS DE CONTROL ---")
    
    # 1. Configuración de Variables (Fase 1)
    banco_palabras = ["SISTEMAS", "ALGORITMO", "PYTHON", "CODIGO"]
    palabra_secreta = random.choice(banco_palabras)
    vidas = 6
    letras_adivinadas = []
    
    print(f"[Debug] Palabra seleccionada: {palabra_secreta}") # Para que el profe vea que funciona
    print("Iniciando ciclo de juego (Validación de Vidas)...")

    # =========================================================
    # ESTRUCTURA REPETITIVA (WHILE)
    # El juego corre mientras las vidas sean mayores a 0.
    # NOTA: En este avance aún no validamos la victoria, solo el ciclo de vidas.
    # =========================================================
    while vidas > 0:
        
        print(f"\n---> Vidas restantes: {vidas}")
        
        # ESTRUCTURA REPETITIVA (FOR) - Visualización
        # Solo mostramos cómo se va llenando la palabra
        progreso = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                progreso += letra + " "
            else:
                progreso += "_ "
        
        print(f"Progreso actual: {progreso}")

        # Entrada de datos
        intento = input("Ingresa una letra: ").upper()

        # =========================================================
        # ESTRUCTURAS LÓGICAS (IF / ELSE)
        # =========================================================
        
        # Validación de entrada
        if len(intento) != 1:
            print(">>> AVISO: Ingresa solo una letra.")
            continue 
            
        # Lógica de juego
        if intento in letras_adivinadas:
            print(">>> AVISO: Letra repetida.")
        elif intento in palabra_secreta:
            print(f">>> ACIERTO: La letra '{intento}' es correcta.")
            letras_adivinadas.append(intento)
            # TODO: Implementar aquí la condición de ruptura si completa la palabra.
        else:
            print(f">>> FALLO: La letra '{intento}' no está.")
            vidas = vidas - 1  # Restamos vida (Contador)
            letras_adivinadas.append(intento)

    # Lógica de fin de juego (Solo por vidas agotadas en este avance)
    print("\n--- CICLO TERMINADO ---")
    print(f"Prueba finalizada. Se agotaron las vidas o se detuvo el ciclo.")

if __name__ == "__main__":
    main()'''
import random

# =========================================================
# UNIDAD 4: PROGRAMACIÓN FUNCIONAL (Funciones Lambda)
# =========================================================
# Lambda 1: Verifica si todas las letras de la palabra secreta están en la lista de adivinadas
verificar_victoria = lambda secreta, adivinadas: all(letra in adivinadas for letra in secreta)

# Lambda 2: Reemplaza las letras no adivinadas por guiones bajos
formatear_progreso = lambda secreta, adivinadas: " ".join([letra if letra in adivinadas else "_" for letra in secreta])

def main():
    print("=== PROYECTO FINAL: JUEGO DEL AHORCADO ===")
    
    # =========================================================
    # UNIDAD 1: VARIABLES Y ENTORNO
    # =========================================================
    banco_palabras = ["SISTEMAS", "ALGORITMO", "PYTHON", "CODIGO", "SOFTWARE"]
    palabra_secreta = random.choice(banco_palabras)
    vidas = 6
    letras_adivinadas = []

    # =========================================================
    # UNIDAD 3: ESTRUCTURAS REPETITIVAS (Bucle While)
    # =========================================================
    while vidas > 0:
        print(f"\n---> Vidas restantes: {vidas}")
        
        # Llamamos a nuestra función Lambda para mostrar el progreso
        progreso = formatear_progreso(palabra_secreta, letras_adivinadas)
        print(f"Progreso actual: {progreso}")

        # Comprobamos si el jugador ya ganó
        if verificar_victoria(palabra_secreta, letras_adivinadas):
            print(f"\n🏆 ¡VICTORIA! Has adivinado la palabra: {palabra_secreta} 🏆")
            break # Rompe el ciclo 'while' inmediatamente

        # Captura de datos del usuario
        intento = input("\nIngresa una letra: ").upper()

        # =========================================================
        # UNIDAD 2: ESTRUCTURAS LÓGICAS (If / Elif / Else)
        # =========================================================
        
        # 1. Filtro de seguridad: Solo 1 letra y debe ser del alfabeto
        if len(intento) != 1 or not intento.isalpha():
            print(">>> ⚠️ AVISO: Ingresa solo una letra válida (A-Z).")
            continue 
            
        # 2. Lógica del juego
        if intento in letras_adivinadas:
            print(">>> ⚠️ AVISO: Letra repetida. Intenta con otra.")
        elif intento in palabra_secreta:
            print(f">>> ✅ ACIERTO: La letra '{intento}' es correcta.")
            letras_adivinadas.append(intento)
        else:
            print(f">>> ❌ FALLO: La letra '{intento}' no está en la palabra.")
            vidas -= 1  # Restamos una vida
            letras_adivinadas.append(intento)

    # Condición de derrota (si el bucle while terminó porque las vidas llegaron a 0)
    if vidas == 0:
        print("\n💀 --- GAME OVER --- 💀")
        print(f"Te quedaste sin vidas. La palabra secreta era: {palabra_secreta}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()