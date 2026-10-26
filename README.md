# vib - right clicker basico

Aplicacion simple para hacer click derecho automaticamente cada cierto tiempo en Windows.

## Configuracion

Edita `config.toml`:

```toml
interval_seconds = 2.0
```

- `interval_seconds`: tiempo entre clicks.

## Ejecutar

Desde la raiz del proyecto:

```powershell
python -m mouse_jiggler.main --config config.toml
```

Detener con `Ctrl+C`.

En Windows tambien puedes lanzarlo con el archivo por lotes:

```powershell
.\run_mouse_jiggler.bat
```

Si quieres pasar argumentos manuales:

```powershell
.\run_mouse_jiggler.bat --config .\config.toml
```

## Test rapido

```powershell
python -m unittest discover -s tests -v
```

