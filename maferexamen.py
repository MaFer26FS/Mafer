import os
import sys
import subprocess

# Colores Neón (Códigos ANSI)
NEON_PURPLE = '\033[95m'
NEON_PINK = '\033[38;5;205m'
NEON_GREEN = '\033[92m'
RESET = '\033[0m'

def clear_screen():
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    """Muestra el banner personalizado en tonos neón."""
    clear_screen()
    print(f"{NEON_GREEN}=================================================={RESET}")
    print(f"{NEON_PURPLE}          _______  ______ ___ _____ _   _ ____  {RESET}")
    print(f"{NEON_PURPLE}         |  ___|  _ \\_ _| ____|  _ \\| | | / ___| {RESET}")
    print(f"{NEON_PURPLE}         | |_  | |_) | ||  _| | | | | | | \\___ \\ {RESET}")
    print(f"{NEON_PURPLE}         |  _| |  _ <| || |___| |_| | |_| |___) |{RESET}")
    print(f"{NEON_PURPLE}         |_|   |_| \\_\\___|_____|____/ \\___/|____/ {RESET}")
    print(f"{NEON_PURPLE}                    FRIENDS SCHOOL                {RESET}")
    print(f"{NEON_GREEN}=================================================={RESET}")
    print(f"{NEON_PINK}        __  __          ______ ______ _____       {RESET}")
    print(f"{NEON_PINK}       |  \\/  |   /\\   |  ____|  ____|  __ \\      {RESET}")
    print(f"{NEON_PINK}       | \\  / |  /  \\  | |__  | |__  | |__) |     {RESET}")
    print(f"{NEON_PINK}       | |\\/| | / /\\ \\ |  __| |  __| |  _  /      {RESET}")
    print(f"{NEON_PINK}       | |  | |/ ____ \\| |    | |____| | \\ \\      {RESET}")
    print(f"{NEON_PINK}       |_|  |_/_/    \\_\\_|    |______|_|  \\_\\     {RESET}")
    print(f"{NEON_PINK}                            MAFER                 {RESET}")
    print(f"{NEON_GREEN}=================================================={RESET}")

def ejecutar_comando(comando, descripcion):
    """Ejecuta un comando del sistema de forma segura."""
    print(f"\n{NEON_GREEN}[+] Ejecutando: {descripcion}...{RESET}")
    try:
        # shell=True permite ejecutar comandos complejos de terminal
        subprocess.run(comando, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"{NEON_PINK}[!] Error al ejecutar: {descripcion}{RESET}")

def asegurar_carpetas():
    """Verifica y crea automáticamente las carpetas necesarias."""
    # En Termux y QPython, 'Gen_Pass' es la carpeta donde se trabajará
    carpetas = ['Gen_Pass']
    for carpeta in carpetas:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"{NEON_GREEN}[+] Carpeta creada automáticamente: {carpeta}{RESET}")
        else:
            print(f"{NEON_PURPLE}[*] La carpeta '{carpeta}' ya existe.{RESET}")

def instalar_entorno():
    """Ejecuta la secuencia de comandos de configuración de tu ejemplo."""
    print(f"\n{NEON_PURPLE}--- Iniciando Instalación de Herramientas ---{RESET}")
    
    # Nota: termux-setup-storage requiere interacción del usuario (permisos)
    ejecutar_comando("termux-setup-storage", "Configurando almacenamiento de Termux")
    ejecutar_comando("apt update && apt upgrade -y", "Actualizando el sistema")
    ejecutar_comando("pkg install git python -y", "Instalando Git y Python 3")
    ejecutar_comando("apt update && apt install git python2 -y", "Instalando dependencias de Python 2")
    
    # Asegurar que la carpeta contenedora exista antes de clonar
    asegurar_carpetas()
    
    # Clonar repositorio dentro de la ruta actual
    if not os.path.exists("Maffs"):
        ejecutar_comando("git clone https://github.com/MaFer26FS/Maffs", "Clonando repositorio Maffs")
    else:
        print(f"{NEON_PURPLE}[*] El repositorio 'Maffs' ya ha sido clonado.{RESET}")

def ejecutar_generador():
    """Mueve el flujo a la carpeta y ejecuta el script solicitado."""
    # Verificamos si existe la carpeta destino
    ruta_destino = "Gen_Pass"
    
    if os.path.exists(ruta_destino):
        print(f"\n{NEON_GREEN}[+] Accediendo a la carpeta: {ruta_destino}{RESET}")
        os.chdir(ruta_destino)
        
        # Intentar ejecutar el script (Se usa 'python' para compatibilidad en Python 3/QPython)
        if os.path.exists("Gen_Pass.py"):
            ejecutar_comando("python Gen_Pass.py", "Ejecutando Gen_Pass.py")
        else:
            # Creamos un archivo temporal/ejemplo por si no existe en la carpeta creada de forma automática
            print(f"{NEON_PINK}[!] Gen_Pass.py no encontrado en la carpeta. Creando un archivo base...{RESET}")
            with open("Gen_Pass.py", "w") as f:
                f.write("print('Generador de contraseñas de Mafer activado.')\n")
            ejecutar_comando("python Gen_Pass.py", "Ejecutando Gen_Pass.py creado")
    else:
        print(f"{NEON_PINK}[!] Error: La carpeta {ruta_destino} no existe.{RESET}")

def menu():
    """Función principal del menú."""
    while True:
        mostrar_banner()
        print(f"{NEON_GREEN}[1]{RESET} Configurar Entorno e Instalar Herramientas")
        print(f"{NEON_GREEN}[2]{RESET} Crear Carpetas Automáticamente")
        print(f"{NEON_GREEN}[3]{RESET} Ejecutar Gen_Pass.py")
        print(f"{NEON_PINK}[4] Salir{RESET}")
        
        opcion = input(f"\n{NEON_PURPLE}Selecciona una opción: {RESET}")
        
        if opcion == "1":
            instalar_entorno()
            input(f"\n{NEON_GREEN}Presiona Enter para continuar...{RESET}")
        elif opcion == "2":
            asegurar_carpetas()
            input(f"\n{NEON_GREEN}Presiona Enter para continuar...{RESET}")
        elif opcion == "3":
            ejecutar_generador()
            input(f"\n{NEON_GREEN}Presiona Enter para continuar...{RESET}")
        elif opcion == "4":
            print(f"\n{NEON_PINK}¡Gracias por usar la herramienta de MAFER! Saliendo...{RESET}")
            sys.exit()
        else:
            print(f"\n{NEON_PINK}Opción no válida. Intenta de nuevo.{RESET}")
            import time
            time.sleep(1.5)

if __name__ == "__main__":
    menu()