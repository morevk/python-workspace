# Jupyter Notebooks

Python learning notebooks and a local Jupyter Lab environment.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `List.ipynb` | Python lists — creation, indexing, and common operations |
| `String.ipynb` | Python strings — basics and manipulation |

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
cd jupyter-notebooks
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Start Jupyter Lab

Use the helper script (activates `.venv` and starts Lab without opening a browser):

```bash
./start-jupyter-lab.sh
```

Or run the steps manually:

```bash
source .venv/bin/activate
jupyter lab --no-browser
```

Jupyter prints a URL with an access token in the terminal. Open that URL in your browser to connect.

To stop the server, press `Ctrl+C` in the terminal where it is running.

## Project layout

```
jupyter-notebooks/
├── List.ipynb
├── String.ipynb
├── requirements.txt
├── start-jupyter-lab.sh
└── .venv/              # local virtual environment (not committed)
```
