#  Verificador de Fuerza de Contraseñas – Python

Este proyecto analiza y clasifica la seguridad de una contraseña basándose en criterios fundamentales de autenticación segura. Evalúa la presencia de mayúsculas, minúsculas, números, símbolos, longitud mínima y además detecta patrones débiles como **sucesiones consecutivas** (`abc`, `123`, etc.).

---

##  Características

- ✔️ Evalúa 6 criterios clave de seguridad:
  - Longitud mínima (12 caracteres)
  - Uso de letras **mayúsculas**
  - Uso de letras **minúsculas**
  - Inclusión de **números**
  - Inclusión de **símbolos**
  - **Evita sucesiones** de letras o números como `abc`, `123`, `xyz`, etc.
    
-  Clasifica la contraseña como:
  - 🔴 Débil
  - 🟡 Media
  - 🟢 Fuerte

-  Componentes y uso:
- ✅ Usa expresiones regulares y lógica condicional
-  Ideal para formación en ciberseguridad y buenas prácticas

---

## 🧠 Tecnologías utilizadas

- **Python 3**
- Librerías estándar:
  - `re` (expresiones regulares)

---

##  ¿Cómo usarlo?

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/Rick5001/verificador-de-fuerza-contrasena.git
   cd verificador-de-fuerza-contrasena
