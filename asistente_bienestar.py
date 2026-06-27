#librerias para el tiempo y para seleccion aleatoria 
import time
import random

# =====================================================================
# PROYECTO INTEGRADOR: ASISTENTE DE BIENESTAR Y DESCONEXIÓN DIGITAL
# ASIGNATURA: INGENIERÍA DE SOFTWARE
# =====================================================================

def iniciar_asistente():
    print("¡BIENVENIDO AL ASISTENTE DE DESCONEXIÓN DIGITAL!")
    
    # UNIDAD 3: CAPTURA DE DATOS Y LOGICA CONDICIONAL (ANÁLISIS DE RIESGO)
    try:
        horas = float(input("Por favor, ingresa el promedio de horas diarias que usas redes sociales: "))
    except ValueError:
        print("Entrada no válida. Se asumirá un consumo de 0 horas para el inicio.")
        horas = 0.0

    # Clasificación del nivel de riesgo del usuario
    if horas > 5:
        clasificacion = "CRÍTICO"
        recomendacion = "Alerta severa. Sufres de hiperestimulación tecnológica. Se recomienda desconexión inmediata."
    elif horas >= 2:
        clasificacion = "MODERADO"
        recomendacion = "Riesgo potencial de dependencia. Intenta reducir el uso recreativo de pantallas."
    else:
        clasificacion = "BAJO"
        recomendacion = "Consumo saludable y equilibrado. ¡Sigue así!"

    print(f"\n[DIAGNÓSTICO INICIAL]: Tu nivel de consumo es {clasificacion}.")
    print(f"[RECOMENDACIÓN]: {recomendacion}\n")

    # UNIDAD 3: ESTRUCTURA REPETITIVA (BUCLE PRINCIPAL DEL MENÚ)
    opcion = 0
    while opcion != 4:
        print("----------------------------------------------------")
        print(f"MENÚ PRINCIPAL (Estado actual de Riesgo: {clasificacion})")
        print("----------------------------------------------------")
        print("1. Ver recomendaciones detalladas")
        print("2. Iniciar Método Pomodoro (Enfoque de 25 min)")
        print("3. Solicitar Reto del Día (Desconexión Analógica)")
        print("4. Salir de la aplicación")
        print("----------------------------------------------------")
        
        try:
            opcion = int(input("Selecciona una opción (1-4): "))
        except ValueError:
            print("Por favor, ingresa un número válido entre 1 y 4.")
            continue

        if opcion == 1:
            print(f"\n>>> RECOMENDACIÓN COMPLETA PARA NIVEL {clasificacion}:")
            if clasificacion == "CRÍTICO":
                print("- Establece límites estrictos en tus apps de hasta 30 minutos al día.\n- Apaga pantallas 2 horas antes de dormir.\n- Realiza un ayuno digital los fines de semana.")
            elif clasificacion == "MODERADO":
                print("- Activa el modo escala de grises en tu celular.\n- Dedica la primera hora de tu mañana a actividades sin pantallas.\n- Deja el teléfono fuera de la habitación al dormir.")
            else:
                print("- Mantén tus buenas rutinas actuales.\n- Comparte tus hábitos saludables con amigos o familiares.")
                
        elif opcion == 2:
            print("\n>>> ¡BLOQUE DE ENFOQUE INICIADO! Concentración total por los próximos 25 minutos.")
            print("El temporizador se ejecutará de forma simulada/reducida para la demostración académica:")
            
            # UNIDAD 3: TEMPORIZADOR SÍNCRONO 
            # Simularemos una cuenta regresiva 
            for segundos_restantes in range(5, 0, -1):
                print(f"Tiempo de enfoque restante: {segundos_restantes} segundos... \r", end="")
                time.sleep(1) # Detiene la ejecución exactamente un segundo
                
            print("\n¡TIEMPO CUMPLIDO! Fin del bloque de enfoque. \a") # El caracter '\a' genera un pitido físico del sistema
            print("Comienza tu descanso activo de 5 minutos. ¡Aléjate de las pantallas!\n")
            
        elif opcion == 3:
            # Lista de actividades para mitigar la fatiga mental
            retos = [
                "Lee 5 páginas de un libro en formato físico.",
                "Haz 10 estiramientos corporales o camina un poco por tu habitación.",
                "Ordena un espacio de tu escritorio que esté desorganizado.",
                "Toma un vaso de agua con calma y sin mirar ningún dispositivo electrónico.",
                "Escribe en un papel tres metas personales para el día de hoy."
            ]
            print(f"\n>>> RETO ALEATORIO ASIGNADO: {random.choice(retos)}\n")
            
        elif opcion == 4:
            print("\n====================================================")
            print("Gracias por usar el Asistente de Bienestar Digital.")
            print("¡Cuida tu salud mental y hasta pronto!")
            print("====================================================\n")
        else:
            print("Opción fuera de rango. Selecciona un número del 1 al 4.")

# Punto de entrada oficial del script en Python
if __name__ == "__main__":
    iniciar_asistente()
