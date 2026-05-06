"""
Claude Design — Brand Poster v2
Paleta: BLUE / NAVY / BLACK / GRAY / WHITE (sin acento neon)
Output: 01_brand_poster.png (A3 @ 300 dpi)
"""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = "/sessions/festive-magical-knuth/mnt/.claude/skills/canvas-design/canvas-fonts"
OUT = "/sessions/festive-magical-knuth/mnt/outputs/claude-design-repo/assets/brand/01_brand_poster.png"

# A3 @ 300 dpi
W, H = 3508, 4961

# Paleta v2
BLUE  = (28, 64, 224)    # #1C40E0
NAVY  = (10, 23, 66)     # #0A1742
BLACK = (0, 0, 0)        # #000000
GRAY  = (232, 233, 236)  # #E8E9EC
WHITE = (255, 255, 255)
GRAY_INK = (138, 138, 149)  # gray for meta text on light bg

def f(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

img = Image.new("RGB", (W, H), GRAY)
d = ImageDraw.Draw(img)

M = 220

# Top meta
mono = f("DMMono-Regular.ttf", 26)
d.text((M, M-30), "CLAUDE_DESIGN_BRAND_BOOK_v01  ·  2026  ·  SPORTS_SECTOR", fill=BLACK, font=mono)
d.line([(M, M+30), (W-M, M+30)], fill=BLACK, width=3)

# ----------------------------------------------------------------------
# IDENTITY BLOCK
# ----------------------------------------------------------------------
y = M + 120
mono_s = f("DMMono-Regular.ttf", 32)
d.text((M, y), "001 / IDENTIDAD", fill=GRAY_INK, font=mono_s)

# CD monogram block (blue square)
box_x, box_y = M, y + 90
box_w, box_h = 1300, 1300
d.rectangle([box_x, box_y, box_x+box_w, box_y+box_h], fill=BLUE)
cd = f("BigShoulders-Bold.ttf", 1100)
bbox = d.textbbox((0,0), "CD", font=cd)
tw = bbox[2]-bbox[0]; th = bbox[3]-bbox[1]
d.text((box_x + (box_w - tw)/2 - bbox[0], box_y + (box_h - th)/2 - bbox[1] - 40), "CD", fill=GRAY, font=cd)
d.text((box_x + 30, box_y + 30), "01", fill=GRAY, font=f("DMMono-Regular.ttf", 24))
d.text((box_x + box_w - 90, box_y + box_h - 60), "®", fill=GRAY, font=f("DMMono-Regular.ttf", 36))

# Right side: full name + blurb
right_x = M + 1450
name_big = f("BigShoulders-Bold.ttf", 360)
d.text((right_x, box_y - 30), "CLAUDE", fill=BLACK, font=name_big)
d.text((right_x, box_y + 320), "DESIGN.", fill=BLUE, font=name_big)
sub_b = f("InstrumentSans-Bold.ttf", 60)
sub   = f("InstrumentSans-Regular.ttf", 60)
d.text((right_x, box_y + 760), "Diseño visual para el deporte.", fill=BLACK, font=sub_b)
d.text((right_x, box_y + 840), "Carruseles, identidad y web", fill=BLACK, font=sub)
d.text((right_x, box_y + 910), "para clubes, atletas y marcas", fill=BLACK, font=sub)
d.text((right_x, box_y + 980), "que compiten al máximo nivel.", fill=BLACK, font=sub)
d.text((right_x, box_y + 1140), "EST. 2026  ·  ESP  ·  ALL-SPORTS", fill=GRAY_INK, font=f("DMMono-Regular.ttf", 28))

# ----------------------------------------------------------------------
# COLOR SYSTEM
# ----------------------------------------------------------------------
y2 = box_y + box_h + 220
d.line([(M, y2), (W-M, y2)], fill=BLACK, width=3)
y3 = y2 + 80
d.text((M, y3), "002 / PALETA", fill=GRAY_INK, font=mono_s)
label_big = f("BigShoulders-Bold.ttf", 110)
d.text((M, y3 + 60), "COLOR SYSTEM — 5 BRAND COLORS", fill=BLACK, font=label_big)

cols = [
    ("BLUE/01",  "#1C40E0", "PRIMARY",     BLUE,  GRAY),
    ("NAVY/02",  "#0A1742", "BACKGROUND",  NAVY,  GRAY),
    ("BLACK/03", "#000000", "EDITORIAL",   BLACK, GRAY),
    ("GRAY/04",  "#E8E9EC", "SURFACE",     GRAY,  BLACK),
    ("WHITE/05", "#FFFFFF", "ON DARK",     WHITE, BLACK),
]
palette_y = y3 + 230
palette_h = 720
GUTTER = 60
col_w = (W - 2*M - 4*GUTTER) // 5
for i, (code, hexv, role, col, txtcol) in enumerate(cols):
    cx = M + i*(col_w + GUTTER)
    d.rectangle([cx, palette_y, cx+col_w, palette_y + palette_h], fill=col,
                outline=BLACK if col == WHITE or col == GRAY else None,
                width=2 if col == WHITE or col == GRAY else 0)
    # corner marks
    d.line([(cx + 20, palette_y + 20), (cx + 50, palette_y + 20)], fill=txtcol, width=3)
    d.line([(cx + 20, palette_y + 20), (cx + 20, palette_y + 50)], fill=txtcol, width=3)
    d.text((cx + 30, palette_y + palette_h - 220), code, fill=txtcol, font=f("DMMono-Regular.ttf", 30))
    d.text((cx + 30, palette_y + palette_h - 170), hexv, fill=txtcol, font=f("BigShoulders-Bold.ttf", 90))
    d.text((cx + 30, palette_y + palette_h - 65), role, fill=txtcol, font=f("DMMono-Regular.ttf", 26))

# ----------------------------------------------------------------------
# TYPE SYSTEM
# ----------------------------------------------------------------------
y4 = palette_y + palette_h + 180
d.line([(M, y4), (W-M, y4)], fill=BLACK, width=3)
y5 = y4 + 80
d.text((M, y5), "003 / TIPOGRAFÍA", fill=GRAY_INK, font=mono_s)
d.text((M, y5 + 60), "TYPE SYSTEM", fill=BLACK, font=label_big)

# Big Shoulders
type_y = y5 + 220
d.text((M, type_y), "BIG SHOULDERS BOLD", fill=BLACK, font=f("DMMono-Regular.ttf", 30))
d.text((M, type_y + 50), "DISPLAY · HEADLINES · NÚMEROS GIGANTES", fill=GRAY_INK, font=f("DMMono-Regular.ttf", 26))
d.text((M, type_y + 100), "OFF SEASON", fill=BLACK, font=f("BigShoulders-Bold.ttf", 280))

# Instrument Sans
type_y2 = type_y + 460
d.text((M, type_y2), "INSTRUMENT SANS", fill=BLACK, font=f("DMMono-Regular.ttf", 30))
d.text((M, type_y2 + 50), "BODY · SUBTÍTULOS · TEXTO LARGO", fill=GRAY_INK, font=f("DMMono-Regular.ttf", 26))
d.text((M, type_y2 + 100), "Diseño que entrena, compite y gana.", fill=BLACK, font=f("InstrumentSans-Bold.ttf", 96))
d.text((M, type_y2 + 220), "Cada carrusel, cada web, cada pieza con", fill=BLACK, font=f("InstrumentSans-Regular.ttf", 60))
d.text((M, type_y2 + 290), "la precisión de un plan de entrenamiento.", fill=BLACK, font=f("InstrumentSans-Regular.ttf", 60))

# DM Mono
type_y3 = type_y2 + 460
d.text((M, type_y3), "DM MONO", fill=BLACK, font=f("DMMono-Regular.ttf", 30))
d.text((M, type_y3 + 50), "DATA · CÓDIGOS · STATS", fill=GRAY_INK, font=f("DMMono-Regular.ttf", 26))
d.text((M, type_y3 + 100), "01 / SPRINT  ·  10.42s  ·  +0.18 PB", fill=BLUE, font=f("DMMono-Regular.ttf", 66))

# Footer
fy = H - M - 40
d.line([(M, fy - 60), (W-M, fy - 60)], fill=BLACK, width=3)
d.text((M, fy - 30), "CLAUDE DESIGN  ·  BRAND BOOK 01  ·  PALETTE & TYPE", fill=BLACK, font=mono_s)
d.text((W - M - 200, fy - 30), "PAGE 01/01", fill=BLACK, font=mono_s)

# Outer corner marks
def corner4(x, y, sz=60, color=BLACK, w=5):
    # 4 marcas externas como tickmarks
    d.line([(x, y), (x+sz, y)], fill=color, width=w)
    d.line([(x, y), (x, y+sz)], fill=color, width=w)
corner4(M-90, M-90, 60)                  # top-left
# top-right
d.line([(W-M+30, M-90), (W-M+90, M-90)], fill=BLACK, width=5)
d.line([(W-M+90, M-90), (W-M+90, M-30)], fill=BLACK, width=5)
# bottom-left
d.line([(M-90, H-M+30), (M-30, H-M+30)], fill=BLACK, width=5)
d.line([(M-90, H-M-30), (M-90, H-M+30)], fill=BLACK, width=5)
# bottom-right
d.line([(W-M+30, H-M+30), (W-M+90, H-M+30)], fill=BLACK, width=5)
d.line([(W-M+90, H-M-30), (W-M+90, H-M+30)], fill=BLACK, width=5)

img.save(OUT, dpi=(300, 300), optimize=True)
print(f"Saved: {OUT}")
