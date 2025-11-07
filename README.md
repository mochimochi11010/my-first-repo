# my-first-repo

# Set-Up
Clone repo from Github and download it onto Desktop
Navigate to the repo using the command line:
```sh
cd /Users/karen/Documents/GitHub/my-first-repo
```

Create a virtual environment:

```sh
conda create -n my-first-env-fall-2025 python=3.11
```

Activate the virtual environment:

```sh
conda activate my-first-env-fall-2025
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

# Usage

Game rock paper scissors

```sh
python app/rps.py

# alternative "modular style" command:
python -m app.rps
```

Stocks Dashboard
```sh
python -m app.stocks
```

## Testing

Run tests:

```sh
pytest
```
