"""Prepara referencias visuais usando os arquivos originais, sem gerar logos."""
import argparse
import hashlib
import json
import re
from pathlib import Path

from PIL import Image, ImageOps


SKILL = Path(__file__).resolve().parents[1]


def carregar(path):
    with Image.open(path) as source:
        image = ImageOps.exif_transpose(source).convert("RGBA")
        background = Image.new("RGBA", image.size, "white")
        background.alpha_composite(image)
        return background.convert("RGB")


def inserir(canvas, path, box):
    image = carregar(path)
    x, y, width, height = box
    image.thumbnail((width, height), Image.Resampling.LANCZOS)
    canvas.paste(image, (x + (width - image.width) // 2,
                        y + (height - image.height) // 2))


def preparar(output, skill_root=SKILL):
    output = Path(output).resolve()
    skill_root = Path(skill_root).resolve()
    text = (skill_root / "references/patrocinadores-oficiais.md").read_text(encoding="utf-8")
    entries = re.findall(r"^\| (\d+) \| ([^|]+) \| \[[^\]]+\]\(([^)]+)\)", text, re.M)
    if [int(e[0]) for e in entries] != list(range(1, 12)):
        raise ValueError("A biblioteca deve conter exatamente os itens 1 a 11 em ordem.")
    sponsors = [(name.strip(), (skill_root / "references" / rel).resolve())
                for _, name, rel in entries]
    crest = skill_root / "assets/escudos/catados-fcca.jpeg"
    for path in [crest, *(path for _, path in sponsors)]:
        if not path.is_file():
            raise FileNotFoundError(path)
        carregar(path)  # Valida todos os inputs antes de escrever as saidas.
    output.mkdir(parents=True, exist_ok=True)
    strips = []
    for filename, group in [("patrocinadores-topo.png", sponsors[:6]),
                            ("patrocinadores-base.png", sponsors[6:])]:
        canvas = Image.new("RGB", (2400, 400), "white")
        offset = (2400 - 400 * len(group)) // 2
        for index, (_, path) in enumerate(group):
            inserir(canvas, path, (offset + index * 400 + 24, 24, 352, 352))
        canvas.save(output / filename)
        strips.append(canvas)
    kit = Image.new("RGB", (2400, 1240), "white")
    inserir(kit, crest, (1000, 20, 400, 400))
    kit.paste(strips[0], (0, 440))
    kit.paste(strips[1], (0, 840))
    kit.save(output / "referencias-oficiais.png")
    manifest = {
        "prancha": "referencias-oficiais.png",
        "escudo": str(crest.relative_to(skill_root)),
        "topo": [name for name, _ in sponsors[:6]],
        "base": [name for name, _ in sponsors[6:]],
        "sha256": {str(path.relative_to(skill_root)): hashlib.sha256(path.read_bytes()).hexdigest()
                   for path in [crest, *(path for _, path in sponsors)]},
        "nota": "Prancha de referencia, nao e banner final. Originais sem recorte; escala proporcional."
    }
    (output / "manifesto.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return (output / "referencias-oficiais.png").resolve()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(preparar(args.output))
