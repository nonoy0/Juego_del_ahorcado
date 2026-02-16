import random

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
    main()