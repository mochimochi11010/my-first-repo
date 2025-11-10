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

## STOCKS EXTRA CREDIT

## Configuration

The stocks functionality requires an AlphaVantage API key. Obtain a premium AlphaVantage API Key (using the [form](https://www.alphavantage.co/support/#api-key) or shared by the prof).

Create a local ".env" file and store your environment variable in there:


```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"
```