## Development setup

Config .env

```
cp .env.example .env
```

Add PYTHONPATH

```
echo PYTHONPATH="$(pwd)" >> .env
```


[Install pre-commit](https://pre-commit.com/)

```
pip install pre-commit
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
