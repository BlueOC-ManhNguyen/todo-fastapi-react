## Development setup

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
