# Codename-CV-API
The RESTful API that provides services to the "Codename CV" React web app.

## Run with Docker
- To run for development, navigate to the top level directory of the repo and run the command:
```bash
docker compose up
```

## Website and Docs
- Open a web browser and type in:
```
http://localhost:8000
```

## PGAdmin website
- Open a web browser and type in:
```
http://localhost:5050/browser/
```

### NOTE: Disregard this, only applies to running locally / specifying the CMD to run in Docker
 - To run for development, run the command:
 ```bash
 fastapi dev api.py
 ```

- To run for production, run the command:
```bash
fastapi run api.py
```
