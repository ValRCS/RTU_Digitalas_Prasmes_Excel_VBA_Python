# Notebook Setup for VS Code

This folder contains notebooks that can be run locally in Visual Studio Code with a project virtual environment such as `.venv`.

## Notebook covered

- `python_vizualizacija_teacher_lv.ipynb`

## Libraries used by this notebook

The notebook imports these Python packages:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `plotly`

To run the notebook in VS Code, install `ipykernel` as well so the `.venv` can be used as a notebook kernel.

## Install in `.venv`

From the repository root in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas numpy matplotlib seaborn plotly ipykernel
```

## Run in Visual Studio Code

1. Open the repository in VS Code.
2. Select the Python interpreter from `.venv`.
3. Open `notebooks\python_vizualizacija_teacher_lv.ipynb`.
4. In the notebook, choose the kernel that points to `.venv`.
5. Run all cells.

## CSV file note

The notebook first tries to read:

- `python_vizualizacija_dati.csv`

If that local file is not found from the current working directory, the notebook falls back to loading the CSV from GitHub. Because of that:

- local run with internet access should still work even if the file is not resolved locally;
- if you want the CSV to be read locally, keep `python_vizualizacija_dati.csv` in this `notebooks` folder and run the notebook with this folder as the working directory.
