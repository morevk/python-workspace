# Python Workspace

A collection of Jupyter notebooks for learning Python fundamentals and exploring common libraries. All notebooks share a single virtual environment at the repository root.

## Notebooks

### `basic-ds/` — Python basics

| Notebook | Topic |
|----------|-------|
| `List.ipynb` | Lists — creation, indexing, and common operations |
| `String.ipynb` | Strings — basics and manipulation |
| `Dict.ipynb` | Dictionaries — key-value data and common patterns |
| `Class.ipynb` | Classes — attributes, methods, and simple OOP |
| `Dataclass.ipynb` | Dataclasses — structured data with `@dataclass` |
| `Typehints.ipynb` | Type hints — lists, dicts, tuples, sets, and typing basics |

### `test-httpx-async-client/` — HTTP client

| Notebook | Topic |
|----------|-------|
| `HttpxAsyncClient.ipynb` | Async HTTP requests with `httpx.AsyncClient` |

### `test-pydentic/` — Data validation

| Notebook | Topic |
|----------|-------|
| `pydantic_demo.ipynb` | Pydantic models, nested schemas, and field validators |

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Key dependencies include Jupyter Lab, `httpx`, and `pydantic`.

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
python-workspace/
├── basic-ds/
│   ├── Class.ipynb
│   ├── Dataclass.ipynb
│   ├── Dict.ipynb
│   ├── List.ipynb
│   ├── String.ipynb
│   └── Typehints.ipynb
├── test-httpx-async-client/
│   └── HttpxAsyncClient.ipynb
├── test-pydentic/
│   └── pydantic_demo.ipynb
├── requirements.txt
├── start-jupyter-lab.sh
└── .venv/              # local virtual environment (not committed)
```
