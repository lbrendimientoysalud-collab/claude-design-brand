# Claude Design

> Estudio visual para el deporte. Carruseles, identidad y web para clubes,
> atletas y marcas que compiten al máximo nivel.

Este repo es el **brand book vivo** de Claude Design. Aquí están los tokens,
componentes y plantillas que definen cómo se ve, se compone y se escribe la
marca. Se diseñó para ser leído por humanos **y** por herramientas como
Claude Design (Anthropic), que toma este repo como referencia para generar
nuevas piezas con la misma línea visual.

---

## TL;DR de marca

|                  |                                                       |
| ---------------- | ----------------------------------------------------- |
| **Sector**       | Deporte (fútbol, running, ciclismo, padel, CrossFit, rugby, artes marciales) |
| **Voz**          | Directa, sin floritura, deportiva. Imperativos cortos. |
| **Estilo**       | Minimalismo deportivo. Tipografía condensada bold.     |
| **Paleta**       | 5 colores: blue, navy, black, gray, white. **Sin acento neon.** |
| **Tipografía**   | Display: Big Shoulders / Impact · Body: Instrument Sans / Inter · Mono: DM Mono |
| **Sello visual** | Marcadores de esquina + meta monoespaciada estilo diagrama técnico |
| **Nunca**        | Gradientes, sombras blandas, lens flare, iconos de stock genéricos |

---

## Estructura del repo

```
claude-design-brand/
├── README.md                       ← este archivo
├── tokens/                         ← fuente de verdad de la marca
│   ├── colors.css                  ← variables CSS de color
│   ├── typography.css              ← familias, escala, tracking
│   ├── spacing.css                 ← espaciado, bordes, motion
│   └── tokens.json                 ← mismo contenido en JSON parseable
├── components/                     ← bloques reutilizables aislados
│   ├── _base.html                  ← wrapper para previsualizar componentes
│   ├── nav.html
│   ├── button.html
│   ├── card-service.html
│   ├── stat-block.html
│   ├── quote-block.html
│   └── ig-frame.html               ← marco base 1080×1080 para IG
├── templates/                      ← composiciones completas, listas para copiar
│   ├── ig-cover-hook.html
│   ├── ig-tip-numbered.html
│   ├── ig-stat-highlight.html
│   ├── ig-quote.html
│   ├── ig-cta-final.html
│   └── web-landing.html
├── assets/
│   ├── brand/01_brand_poster.png   ← brand book en una página, A3 @ 300dpi
│   ├── logo/cd-monogram.svg        ← logo CD sobre azul
│   ├── logo/cd-monogram-mono.svg   ← logo CD en negro, sin caja
│   └── fonts/                      ← (opcional) ttf/woff2 si se autohostean
├── examples/
│   ├── instagram-deck.pptx         ← 8 plantillas IG editables en PowerPoint
│   └── presentation-deck.pptx      ← 8 slides de presentación 16:9
└── docs/
    ├── github-setup.md             ← cómo subir este repo a GitHub
    ├── voice.md                    ← guía de tono y copy
    └── dos-and-donts.md            ← qué sí y qué no
```

---

## Cómo se usa este repo con Claude Design

1. Sube este repo a GitHub (ver `docs/github-setup.md`).
2. En el formulario de Claude Design, en **"Link code on GitHub"**, pega la URL
   pública del repo y pulsa "Add".
3. En **"Company name and blurb"** pega:

   > Claude Design: estudio visual para el deporte. Diseñamos carruseles
   > de Instagram, identidad de marca y webs para clubes, atletas y marcas
   > de performance. Estética deportiva con base minimalista, dominada por
   > azul eléctrico (#1C40E0), negro, gris y blanco. Sin acento neon.

4. En **"Add fonts, logos and assets"** sube:
   - `assets/brand/01_brand_poster.png`
   - `assets/logo/cd-monogram.svg`
   - `assets/logo/cd-monogram-mono.svg`

5. En **"Any other notes?"** pega el bloque de `docs/voice.md` y `docs/dos-and-donts.md`.

A partir de ahí, cuando Claude Design genere nuevas piezas leerá los
tokens, componentes y plantillas del repo y los respetará.

---

## Paleta — 5 colores, sin acento neon

| Token       | HEX        | Uso                                                  | Peso visual |
| ----------- | ---------- | ---------------------------------------------------- | ----------- |
| `--cd-blue` | `#1C40E0`  | **Primario.** Royal/eléctrico. Dominante.             | 50–60%      |
| `--cd-navy` | `#0A1742`  | Fondo profundo puntual.                              | 5–10%       |
| `--cd-black`| `#000000`  | Fondos editoriales y remarques.                      | 10–15%      |
| `--cd-gray` | `#E8E9EC`  | Superficie clara, fondo por defecto.                 | 25–30%      |
| `--cd-white`| `#FFFFFF`  | Solo sobre fondos oscuros.                           | tipografía  |

**Combinaciones permitidas** (no inventar otras):

- `gray bg` + `black text` + `blue accents`
- `blue bg` + `gray text` + detalles `gray`
- `navy bg` + `gray text` + detalles `blue`/`gray`
- `black bg` + `gray text` + acentos `blue`

---

## Tipografía

### Display — `Big Shoulders Bold`
Para titulares, números gigantes y slogans. Siempre uppercase. Tracking
ligeramente negativo (`-0.015em`). Sustitutos: Impact, Bebas Neue, Anton.

### Body — `Instrument Sans`
Para subtítulos, lede, párrafos. Pesos 400/500/700. Sustitutos: Inter,
Helvetica Neue, Calibri.

### Mono — `DM Mono`
Para meta, etiquetas técnicas, códigos, marcadores de esquina. 11px
uppercase con tracking `0.2em`.

---

## Sello visual

Cada pieza incluye al menos uno de estos:

- **Marcadores de esquina** (4 corner ticks) en el bloque principal
- **Meta superior** con monograma `CD` + código de pieza (`01 / COVER · HOOK`)
- **Meta inferior** con marca + paginación (`CLAUDE DESIGN  ·  01 / 08`)
- **Línea horizontal** separando bloques de información

Esto recuerda visualmente a un diagrama técnico / programa de
entrenamiento. Es el "DNA" de Claude Design.

---

## Voz

Lee `docs/voice.md` para el detalle. Resumen:

- Imperativo y directo. *"Entrena como los que ganan."*
- Frases cortas. Cero relleno.
- Datos con cifras y unidades, no adjetivos.
- Cero jerga corporativa. Tono de vestuario, no de oficina.

---

## Licencia y créditos

Marca, copy y composición: © 2026 Claude Design.
Fuentes utilizadas:
- Big Shoulders — Open Font License (Patric King / Production Type)
- Instrument Sans — Open Font License (Rodrigo Fuenzalida & Jen Wagner)
- DM Mono — Open Font License (Colophon Foundry)
