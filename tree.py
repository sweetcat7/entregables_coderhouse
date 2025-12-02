import os
import sys

EXCLUIR_CARPETAS = {"__pycache__", "node_modules", "venv", ".git", ".idea", ".mypy_cache"}
EXCLUIR_EXT = {".json", ".pyc", ".log"}

def imprimir_estructura(directorio, prefijo=""):
    try:
        elementos = sorted(os.listdir(directorio))
    except PermissionError:
        return
    except FileNotFoundError:
        print(f"❌ Ruta no encontrada: {directorio}")
        return

    for elemento in elementos:
        ruta = os.path.join(directorio, elemento)

        if os.path.isdir(ruta):
            if elemento not in EXCLUIR_CARPETAS:
                print(f"{prefijo}📁 {elemento}/")
                imprimir_estructura(ruta, prefijo + "│   ")
        else:
            if not any(elemento.endswith(ext) for ext in EXCLUIR_EXT):
                print(f"{prefijo}📄 {elemento}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) < 2:
        ruta_relativa = "."
    else:
        ruta_relativa = sys.argv[1]

    if os.path.isabs(ruta_relativa):
        print("❌ Solo se permiten rutas relativas.")
        sys.exit(1)

    ruta_absoluta = os.path.normpath(os.path.join(base_dir, ruta_relativa))
    imprimir_estructura(ruta_absoluta)
