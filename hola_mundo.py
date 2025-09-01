#!/usr/bin/env python3
import os

def main():
    # Obtener el nombre de usuario desde la variable de entorno
    username = os.getenv('USERNAME', 'Usuario')
    
    print(f"¡Hola {username}!")
    print("Este es mi primer workflow de GitHub Actions")
    print("¡Estoy aprendiendo a automatizar procesos!")

if __name__ == "__main__":
    main()
