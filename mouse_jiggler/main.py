from __future__ import annotations

import argparse
import time
from pathlib import Path

from mouse_jiggler.config import load_config
from mouse_jiggler.mouse import right_click


def run(config_path: Path) -> None:
    config = load_config(config_path)

    print(f"Configuracion cargada desde: {config_path}")
    print(f"Haciendo click derecho cada {config.interval_seconds}s.")
    print("Pulsa Ctrl+C para detener.")

    while True:
        right_click()
        print("+", end="", flush=True)
        time.sleep(config.interval_seconds)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Hace click derecho automaticamente cada cierto tiempo"
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.toml"),
        help="Ruta al fichero de configuracion TOML",
    )
    args = parser.parse_args()

    run(args.config)


if __name__ == "__main__":
    main()


