"""Carrega assets reais da skill para uma pasta acessivel a ferramenta de imagem."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image
from preparar_referencias import SKILL, carregar, preparar


def carregar_assets(output, skill_root=SKILL, somente_escudo=False):
    root = Path(skill_root).resolve()
    output = Path(output).resolve()
    # Nao escrever derivados nem alterar arquivos dentro da skill instalada.
    if output == root or root in output.parents:
        raise ValueError("Escolha uma pasta de saida fora da skill instalada.")
    crest = root / "assets/escudos/catados-fcca.jpeg"
    carregar(crest)  # Falha explicitamente se ausente ou invalido.
    if not somente_escudo:
        sheet = preparar(output, root)  # Valida os 12 originais e recria referencias atuais.
    else:
        output.mkdir(parents=True, exist_ok=True)
    target = output / "catados-fcca.jpeg"
    shutil.copyfile(crest, target)
    assert hashlib.sha256(crest.read_bytes()).digest() == hashlib.sha256(target.read_bytes()).digest()
    references = [target] if somente_escudo else [target, sheet]
    for path in references:
        with Image.open(path) as image:
            image.verify()
    payload = {
        "skill_root": str(root),
        "referenced_image_paths": [str(path) for path in references],
        "patrocinadores": 0 if somente_escudo else 11,
        "faixas": {} if somente_escudo else {
            "topo": str(output / "patrocinadores-topo.png"),
            "base": str(output / "patrocinadores-base.png"),
        },
        "instrucao": "Enviar referenced_image_paths no campo real da ferramenta. Este arquivo nao executa a geracao.",
    }
    (output / "assets-carregados.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--skill-root", type=Path, default=SKILL)
    parser.add_argument("--somente-escudo", action="store_true")
    args = parser.parse_args()
    try:
        payload = carregar_assets(args.output, args.skill_root, args.somente_escudo)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Falha no carregamento dos assets: {error}\n")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
