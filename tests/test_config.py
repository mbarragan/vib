from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from mouse_jiggler.config import load_config


class TestConfig(unittest.TestCase):
    def test_load_valid_config(self) -> None:
        config_text = """
interval_seconds = 1.5
""".strip()

        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.toml"
            config_path.write_text(config_text, encoding="ascii")
            config = load_config(config_path)

        self.assertEqual(config.interval_seconds, 1.5)

    def test_invalid_interval(self) -> None:
        config_text = """
interval_seconds = 0
""".strip()

        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.toml"
            config_path.write_text(config_text, encoding="ascii")
            with self.assertRaises(ValueError):
                load_config(config_path)


if __name__ == "__main__":
    unittest.main()

