## 📌 List of Allowed Values

1. MSZoning (categorical)

- RL
- RM
- RH
- C
- FV

2. HouseStyle (categorical)

- 1Story
- 2Story
- SLvl
- SFoyer

3. Neighborhood (categorical)

- CollgCr
- Crawfor
- OldTown
- NrdgHt
- NoRidge
- Veenker

4. Numerical features

| Feature        | Type | Range       |
| -------------- | ---- | ----------- |
| `LotArea`      | int  | 500 – 50000 |
| `OverallQual`  | int  | 1–10        |
| `OverallCond`  | int  | 1–10        |
| `YearBuilt`    | int  | 1870–2030   |
| `BedroomAbvGr` | int  | 1–10        |
| `FullBath`     | int  | 1–5         |
| `GrLivArea`    | int  | 300–6000    |
| `GarageCars`   | int  | 0–5         |


## Output Format

```json
{
  "predicted_price": 198858.01
}
```
Just a single number — easy for UI rendering.

## Sample Input

```json
{
        "MSZoning": "RL",
        "LotArea": 9000,
        "OverallQual": 6,
        "OverallCond": 5,
        "YearBuilt": 2010,
        "HouseStyle": "2Story",
        "BedroomAbvGr": 3,
        "FullBath": 2,
        "GrLivArea": 1800,
        "Neighborhood": "CollgCr",
        "GarageCars": 2
}
```

## Steps to start the FastAPI

1. Navigate to the `/app` directory:
```bash
cd housing_price_llm/app
```

2. Execute the command
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

Now the API is active.

### API Endpoint Description

| Endpoint   | Method | Description                   |
| ---------- | ------ | ----------------------------- |
| `/predict` | POST   | Returns predicted house price |


### Execution of API

```bash
POST http://yourserver:8000/predict
Content-Type: application/json
```

Example curl command:

```bash
curl -X POST \
  http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "MSZoning": "RL",
    "LotArea": 9000,
    "OverallQual": 6,
    "OverallCond": 5,
    "YearBuilt": 2010,
    "HouseStyle": "2Story",
    "BedroomAbvGr": 3,
    "FullBath": 2,
    "GrLivArea": 1800,
    "Neighborhood": "CollgCr",
    "GarageCars": 2
  }'
```

### HTTP Status Codes & Meaning

```bash
200 OK → Successful prediction  
400 Bad Request → Missing field / invalid value  
422 Validation Error → Wrong data format  
500 Internal Server Error → Model or server issue  
```