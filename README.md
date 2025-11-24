## GUI Fourier & Laplace – Instrucciones rápidas

### Documentar el Punto 4
1. Ejecuta `python main.py`.
2. Selecciona **Serie de Fourier** y **Transformada de Laplace** desde el menú izquierdo; en cada caso:
   - Toma la captura de la ventana (gráfica + texto explicativo).
   - Inserta la imagen en la sección correspondiente de `Trabajo individual.pdf`.
   - Redacta un párrafo breve con el resultado (por ejemplo: “La serie usa solo armónicos impares y muestra Gibbs en los saltos”; “F(s) = (2/s²)(1 − e^{-s}), ROC Re(s) > 0”).
3. En el informe menciona que la implementación se realizó en Python (`main.py`) como evidencia del punto 4.

### Subir el proyecto a GitHub
1. Abre una terminal en `C:\Users\joseo\OneDrive\Documents\Mate`.
2. Inicializa o verifica el repositorio:
   ```bash
   git init
   git status
   ```
3. Configura tus datos (solo la primera vez):
   ```bash
   git config user.name "Tu Nombre"
   git config user.email "tu@correo.com"
   ```
4. Agrega los archivos relevantes:
   ```bash
   git add main.py "Trabajo individual.pdf" README.md
   ```
5. Crea el commit:
   ```bash
   git commit -m "Implementa GUI Fourier/Laplace y documenta punto 4"
   ```
6. Crea un repositorio en GitHub y copia la URL HTTPS, luego:
   ```bash
   git remote add origin https://github.com/tuusuario/tu-repo.git
   git branch -M main
   git push -u origin main
   ```
7. Verifica en GitHub que `main.py`, `Trabajo individual.pdf` y `README.md` estén presentes.

