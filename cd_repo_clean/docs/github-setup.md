# Cómo subir este repo a GitHub y conectarlo a Claude Design

Pasos en orden, exactos. **Tiempo estimado: 8-10 minutos.**

---

## 1 · Crear cuenta de GitHub (si no la tienes)

1. Abre [https://github.com/signup](https://github.com/signup).
2. Usa tu email `lbauelos12@gmail.com`.
3. Elige un username — sugerencia: `claudedesign-es` o `lbanuelos-cd`.
4. Verifica el email.

> Si ya tienes cuenta, salta este paso.

---

## 2 · Crear el repo (web, sin terminal)

1. Una vez dentro de GitHub, pulsa **"+"** arriba a la derecha → **"New repository"**.
2. Configura así:
   - **Repository name:** `claude-design-brand`
   - **Description:** `Brand book + design system de Claude Design — estudio visual para el deporte`
   - **Public** (necesario para que Claude Design pueda leerlo)
   - **NO** marques "Add a README" (ya tenemos uno)
   - **NO** añadas .gitignore ni licencia (los añadimos nosotros)
3. Pulsa **"Create repository"**.

GitHub te llevará a una página con instrucciones. Anota la URL del repo —
algo como `https://github.com/TU_USUARIO/claude-design-brand`.

---

## 3 · Subir los archivos

Tienes dos formas. Elige la que más te guste.

### Opción A — Web (más fácil, sin terminal)

1. En la página del repo recién creado, pulsa **"uploading an existing file"**
   (el enlace está en el bloque de texto "...or upload an existing file").
2. Abre la carpeta `claude-design-repo` en tu Finder y **arrástrala entera**
   al área de upload de GitHub.
3. Espera a que suban todos los archivos (verás progreso por archivo).
4. Más abajo, en **Commit changes**:
   - Title: `Initial commit — Claude Design brand v1.0`
   - Pulsa **"Commit changes"**.

**Nota:** GitHub web no sube carpetas vacías. Si la carpeta `assets/fonts/`
está vacía, no aparecerá. No pasa nada.

### Opción B — Terminal (si prefieres git)

Abre Terminal y ejecuta:

```bash
cd ~/Documents   # o donde quieras tener el repo en local
mv "/ruta/a/claude-design-repo" .
cd claude-design-brand
git init
git add .
git commit -m "Initial commit — Claude Design brand v1.0"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/claude-design-brand.git
git push -u origin main
```

Sustituye `TU_USUARIO` por tu username real. Si te pide credenciales,
GitHub usa **personal access tokens** en vez de contraseña — sigue las
instrucciones que te aparezcan o usa GitHub Desktop como alternativa
gráfica.

---

## 4 · Conectar el repo a Claude Design

1. Vuelve al formulario de **"Set up your design system"** en Claude
   (donde estabas antes, [ver pantalla del enunciado](#)).
2. En el campo **"Link code on GitHub"**, pega la URL del repo:
   `https://github.com/TU_USUARIO/claude-design-brand`
3. Pulsa **"Add"**.
4. En **"Company name and blurb"** pega:

   > Claude Design: estudio visual para el deporte. Diseñamos carruseles
   > de Instagram, identidad de marca y webs para clubes, atletas y marcas
   > de performance. Estética deportiva con base minimalista, dominada
   > por azul eléctrico (#1C40E0), negro, gris y blanco. Sin acento neon.

5. En **"Add fonts, logos and assets"** sube los archivos:
   - `assets/brand/01_brand_poster.png`
   - `assets/logo/cd-monogram.svg`
   - `assets/logo/cd-monogram-mono.svg`

6. En **"Any other notes?"** pega el contenido completo de
   `docs/voice.md` + `docs/dos-and-donts.md`.

7. Guarda los cambios.

A partir de ahí, cuando Claude Design genere nuevas piezas leerá los
tokens, componentes y plantillas del repo y respetará la línea visual.

---

## 5 · Mantener el repo vivo

Cuando cambies algo de marca (añadas un componente, ajustes un color):

1. Edita el archivo correspondiente.
2. Si usaste **opción A**, ve al archivo en GitHub web, pulsa el lápiz
   para editar, escribe el cambio, commit.
3. Si usaste **opción B**:

   ```bash
   cd claude-design-brand
   git add .
   git commit -m "Ajuste: descripción corta del cambio"
   git push
   ```

Claude Design leerá la última versión la próxima vez que la uses.

---

## Problemas comunes

| Problema                                 | Solución                                              |
| ---------------------------------------- | ----------------------------------------------------- |
| GitHub me pide contraseña y no funciona  | Usa **personal access token** o GitHub Desktop        |
| No sube las carpetas vacías              | Normal. Sólo sube las que tienen archivos             |
| Claude Design no lee bien el repo        | Asegúrate de que está **Public**, no Private          |
| Quiero cambiar algo del nombre del repo  | Settings → General → Repository name                  |
