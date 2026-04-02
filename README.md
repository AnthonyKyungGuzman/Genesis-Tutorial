# Tutorial de Genesis

## Estructura del Proyecto

```
Genesis-Tutorial/
├─ src/
│  ├─ 1_hello_genesis.py
├─ pyproject.toml     # Dependencias del proyecto
└─ README.md
```

## Dependencias:
- PyTorch >=2.11
- genesis-world >=0.4

## Instalar dependencias:

Hay dos maneras de instalar las dependencias.
1. Utilizando el comando pip install para cualquier dependencia.
2. Utilizando un administrador de archivos (recomendado).

### Pip Install
PyTorch puede descargarse desde la página web para ver que versión es compatible con su ordenador:
https://pytorch.org/get-started/previous-versions/
```
pip install torch==####
``` 
Cambiar #### por la versión compatible con su ordenador.

Genesis se puede instalar con el siguiente comando:
```
pip install genesis-world
```

### UV Install
El administrador de archivos utilizado y recomendado es UV y puede descargarse en la siguiente dirección:
https://docs.astral.sh/uv/getting-started/installation/

Una vez instalado el administrador de archivos se pueden instalar las dependencias con el siguiente comando:
```
uv sync 
```
Al sincronizar las dependencias se carga el ambiente utilizando el siguiente comando:
```
source .venv/bin/activate
```

## Ejecución de programas del tutorial

Para ejecutar cualquier ejemplo.
En la linea de comando se ejecuta el siguuiente comando:
```
python src/[####].py
```
Cambiar [####] por el ejemplo que se quiere ejecutar.




