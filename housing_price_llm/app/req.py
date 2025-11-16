import requests

data = {
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

headers = {
    "Content-Type": "application/json"
}
req = requests.post(url="http://localhost:8000/predict", headers=headers, json=data)

print(req.content)