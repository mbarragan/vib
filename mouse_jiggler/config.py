from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import tomllib


@dataclass(frozen=True)
class AppConfig:
    interval_seconds: float


def load_config(config_path: Path) -> AppConfig:
    with config_path.open("rb") as file:
        data = tomllib.load(file)

    interval_seconds = float(data.get("interval_seconds", 2.0))

    if interval_seconds <= 0:
        raise ValueError("interval_seconds debe ser mayor que 0")

    return AppConfig(interval_seconds=interval_seconds)


