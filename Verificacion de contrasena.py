import re

def contiene_sucesion(contraseña):
    letras = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"

    contraseña_lower = contraseña.lower()

    for i in range(len(letras) - 2):
        if letras[i:i+3] in contraseña_lower:
            return True

    for i in range(len(numeros) - 2):
        if numeros[i:i+3] in contraseña:
            return True

    return False

def verificar_fuerza(contraseña):
    fuerza = 0
    criterios = {
        "longitud": len(contraseña) >= 12,
        "mayúsculas": re.search(r"[A-Z]", contraseña),
        "minúsculas": re.search(r"[a-z]", contraseña),
        "números": re.search(r"[0-9]", contraseña),
        "símbolos": re.search(r"[\W_]", contraseña),
        "sin sucesiones": not contiene_sucesion(contraseña)
    }

    for criterio, cumple in criterios.items():
        if cumple:
            fuerza += 1

    if fuerza <= 2:
        nivel = "🔴 Débil"
    elif fuerza == 3 or fuerza == 4:
        nivel = "🟡 Media"
    else:
        nivel = "🟢 Fuerte"

    print("\n Evaluación de la contraseña:")
    for criterio, cumple in criterios.items():
        estado = "✅" if cumple else "❌"
        print(f" - {criterio.capitalize():<16}: {estado}")

    print(f"\n Nivel de seguridad: {nivel}")

# --- MAIN ---
if __name__ == "__main__":
    print(" Verificador de Fuerza de Contraseña")
    contraseña = input("Ingresa la contraseña a evaluar: ")
    verificar_fuerza(contraseña)
