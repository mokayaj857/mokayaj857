"""Raster identity art for GitHub README (PNG; GitHub often drops custom SVG)."""
from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
W, H = 1400, 420
INK = (8, 9, 11)
PHOS = (110, 255, 196)
DIM = (70, 120, 108)
BONE = (232, 236, 232)
MUTED = (140, 158, 154)
TRACE = (42, 58, 54)
GOLD = (232, 196, 92)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    names = [
        "consola.ttf",
        "consolab.ttf" if bold else "consola.ttf",
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/consolab.ttf" if bold else "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
        "C:/Windows/Fonts/courbd.ttf" if bold else "C:/Windows/Fonts/cour.ttf",
        "C:/Windows/Fonts/lucon.ttf",
    ]
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            continue
    return ImageFont.load_default()


def hex_grid(draw: ImageDraw.ImageDraw, rng: random.Random) -> None:
    r = 18
    dx = r * 1.5
    dy = r * math.sqrt(3)
    y = -r
    row = 0
    while y < H + r:
        x = -r if row % 2 == 0 else dx / 2
        while x < W + r:
            if rng.random() > 0.72:
                pts = []
                for i in range(6):
                    a = math.radians(60 * i - 30)
                    pts.append((x + r * 0.55 * math.cos(a), y + r * 0.55 * math.sin(a)))
                draw.polygon(pts, outline=TRACE)
            x += dx
        y += dy * 0.5
        row += 1


def draw_chip(draw: ImageDraw.ImageDraw, x: int, y: int, label: str, on: bool) -> None:
    w, h = 88, 54
    col = PHOS if on else MUTED
    draw.rounded_rectangle((x, y, x + w, y + h), 4, outline=col, width=2)
    for i in range(5):
        py = y + 8 + i * 9
        draw.line((x - 8, py, x, py), fill=col, width=1)
        draw.line((x + w, py, x + w + 8, py), fill=col, width=1)
    draw.text((x + w / 2, y + h / 2), label, font=font(14, True), fill=col, anchor="mm")


def banner() -> None:
    rng = random.Random(857)
    im = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(im)
    hex_grid(d, rng)

    # scanlines
    for y in range(0, H, 3):
        d.line((0, y, W, y), fill=(10, 14, 13))

    # left meridian
    d.rectangle((0, 0, 8, H), fill=PHOS)
    d.text((28, 28), "NODE  //  1.2921 S   36.8219 E   //  NBO", font=font(16), fill=DIM)

    d.text((28, 88), "JOHN MOKAYA", font=font(64, True), fill=BONE)
    d.text((32, 168), "FULL-STACK ENGINEER   /   PROTOCOL NERD", font=font(22), fill=PHOS)

    d.text((32, 230), "runtime    typescript  ·  solidity  ·  python", font=font(18), fill=MUTED)
    d.text((32, 262), "isa        evm  ·  substrate  ·  eUTxO  ·  move", font=font(18), fill=MUTED)
    d.text((32, 294), "lab        zk  ·  xcm  ·  foundry  ·  next", font=font(18), fill=MUTED)

    d.text((32, 360), "open stdin   collaboration@interesting.problems", font=font(16), fill=GOLD)

    # right: die shot
    cx, cy = 1120, 210
    d.ellipse((cx - 92, cy - 92, cx + 92, cy + 92), outline=TRACE, width=1)
    d.ellipse((cx - 60, cy - 60, cx + 60, cy + 60), outline=DIM, width=1)
    d.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=PHOS)
    for i in range(8):
        a = i * (math.pi / 4)
        d.line(
            (cx + 16 * math.cos(a), cy + 16 * math.sin(a), cx + 88 * math.cos(a), cy + 88 * math.sin(a)),
            fill=TRACE,
            width=1,
        )
    labels = ["ETH", "AVAX", "DOT", "ADA", "SUI", "ZK", "XCM", "TS"]
    for i, lab in enumerate(labels):
        a = i * (math.pi / 4) - math.pi / 2
        lx = cx + 118 * math.cos(a)
        ly = cy + 118 * math.sin(a)
        d.text((lx, ly), lab, font=font(13, True), fill=PHOS, anchor="mm")

    d.rectangle((0, H - 6, W, H), fill=PHOS)
    im.save(ROOT / "banner.png", optimize=True)


def board() -> None:
    im = Image.new("RGB", (1400, 220), INK)
    d = ImageDraw.Draw(im)
    d.text((24, 18), "INSTRUCTION DECODE  /  multi-vm", font=font(14), fill=DIM)
    chips = [
        (40, "ETH", True),
        (180, "AVAX", True),
        (320, "DOT", True),
        (460, "ADA", True),
        (600, "SUI", True),
        (740, "EVM", True),
        (880, "MOVE", True),
        (1020, "ZK", False),
        (1160, "XCM", True),
    ]
    y = 70
    for x, lab, on in chips:
        draw_chip(d, x, y, lab, on)
        if x < 1160:
            d.line((x + 96, y + 27, x + 140, y + 27), fill=TRACE, width=2)
    d.text((40, 170), "clk  foundry/hardhat   bus  graphql+sql   cache  next   irq  currently: substrate, move, zk", font=font(15), fill=MUTED)
    d.rectangle((0, 214, 1400, 220), fill=PHOS)
    im.save(ROOT / "board.png", optimize=True)


def panel(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, title: str, lines: list[str]) -> None:
    draw.rounded_rectangle((x, y, x + w, y + h), 10, outline=PHOS, width=2)
    draw.text((x + 22, y + 22), title, font=font(15, True), fill=GOLD)
    yy = y + 56
    for line in lines:
        draw.text((x + 22, yy), line, font=font(18), fill=BONE)
        yy += 32


def lab() -> None:
    im = Image.new("RGB", (1400, 280), INK)
    d = ImageDraw.Draw(im)
    for y in range(0, 280, 3):
        d.line((0, y, 1400, y), fill=(10, 14, 13))
    d.rectangle((0, 0, 8, 280), fill=PHOS)
    d.text((28, 18), "PIPELINE  /  product speaks vm without lying", font=font(14), fill=DIM)

    panel(d, 28, 48, 300, 196, "SURFACE", ["React  Next  TypeScript", "the part people touch"])
    panel(d, 360, 48, 300, 196, "KERNEL", ["Node  GraphQL  SQL", "Python  Docker  Git"])
    panel(d, 692, 48, 300, 196, "ISA", ["EVM  Substrate  eUTxO", "Move  Foundry  Aiken"])
    panel(d, 1024, 48, 348, 196, "QUEUE", ["Substrate   Move   ZK", "stdin open"])

    for x in (336, 668, 1000):
        d.polygon([(x, 140), (x + 16, 148), (x, 156)], fill=PHOS)

    d.rectangle((0, 274, 1400, 280), fill=PHOS)
    im.save(ROOT / "lab.png", optimize=True)


if __name__ == "__main__":
    banner()
    board()
    lab()
    print("wrote banner.png board.png lab.png")
