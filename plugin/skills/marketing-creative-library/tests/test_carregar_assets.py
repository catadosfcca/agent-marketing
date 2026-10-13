"""Testes do carregamento com arquivos reais e falhas de acesso."""
import hashlib
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from carregar_assets import carregar_assets
from preparar_referencias import SKILL


class CarregamentoTests(unittest.TestCase):
    def test_diretorio_atual_diferente(self):
        with tempfile.TemporaryDirectory() as folder:
            previous = Path.cwd()
            try:
                os.chdir(folder)
                result = carregar_assets(Path(folder) / "saida")
            finally:
                os.chdir(previous)
            self.assertEqual(result["patrocinadores"], 11)
            self.assertEqual(len(result["referenced_image_paths"]), 2)
            for path in result["referenced_image_paths"]:
                self.assertTrue(Path(path).is_absolute())
                self.assertTrue(Path(path).is_file())
            manifest = json.loads((Path(folder) / "saida/manifesto.json").read_text(encoding="utf-8"))
            self.assertEqual(len(manifest["sha256"]), 12)
            self.assertEqual(len(manifest["topo"]), 6)
            self.assertEqual(len(manifest["base"]), 5)
            self.assertEqual(hashlib.sha256((SKILL / "assets/escudos/catados-fcca.jpeg").read_bytes()).hexdigest(),
                             hashlib.sha256(Path(result["referenced_image_paths"][0]).read_bytes()).hexdigest())

    def test_skill_realocada(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "plugin-instalado/skills/marketing-creative-library"
            shutil.copytree(SKILL / "assets", root / "assets")
            shutil.copytree(SKILL / "references", root / "references")
            result = carregar_assets(Path(folder) / "saida", root)
            self.assertEqual(result["skill_root"], str(root.resolve()))
            self.assertEqual(result["patrocinadores"], 11)

    def test_apenas_escudo_sem_patrocinadores(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "skill"
            crest = root / "assets/escudos/catados-fcca.jpeg"
            crest.parent.mkdir(parents=True)
            shutil.copyfile(SKILL / "assets/escudos/catados-fcca.jpeg", crest)
            result = carregar_assets(Path(folder) / "saida", root, True)
            self.assertEqual(result["patrocinadores"], 0)
            self.assertEqual(len(result["referenced_image_paths"]), 1)
            self.assertEqual(result["faixas"], {})

    def test_arquivo_ausente_nao_produz_saida(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(FileNotFoundError):
                carregar_assets(Path(folder) / "saida", Path(folder) / "inexistente")
            self.assertFalse((Path(folder) / "saida").exists())

    def test_logo_corrompida_nao_produz_saida(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "skill"
            shutil.copytree(SKILL / "assets", root / "assets")
            shutil.copytree(SKILL / "references", root / "references")
            (root / "assets/patrocinadores/yuam.jpg").write_bytes(b"nao e uma imagem")
            with self.assertRaises(OSError):
                carregar_assets(Path(folder) / "saida", root)
            self.assertFalse((Path(folder) / "saida").exists())

    def test_protege_skill_instalada(self):
        with self.assertRaises(ValueError):
            carregar_assets(SKILL / "assets/saida")


if __name__ == "__main__":
    unittest.main()
