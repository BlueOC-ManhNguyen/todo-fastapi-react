## Development setup

Virtualenv

```
python3 -m venv venv
pip install -r requirements.txt
```

Config .env

```
cp .env.example .env
```

Add PYTHONPATH

```
export PYTHONPATH=`pwd`
```


[Install pre-commit](https://pre-commit.com/)

```
pre-commit install
```

Start database

```
docker compose up -d
```


Start server
```
uvicorn app.main:app --reload
```
