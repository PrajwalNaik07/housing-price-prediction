# metadata.py

FEATURE_INFO = {
    "MSZoning": {
        "options": {
            "Residential Low Density (RL)": "RL",
            "Residential Medium Density (RM)": "RM",
            "Residential High Density (RH)": "RH",
            "Commercial (C)": "C",
            "Floating Village (FV)": "FV",
        },
        "description": "General zoning classification of the property."
    },

    "HouseStyle": {
        "options": {
            "One Story": "1Story",
            "Two Story": "2Story",
            "1.5 Story Finished": "1.5Fin",
            "Split Level": "SLvl",
            "Split Foyer": "SFoyer",
        },
        "description": "Architectural style of the home."
    },

    "Neighborhood": {
        "options": {
            "College Creek": "CollgCr",
            "Crawford": "Crawfor",
            "Old Town": "OldTown",
            "Veenker": "Veenker",
            "Northridge Heights": "NridgHt",
            "Northridge": "NoRidge",
            "Timberland": "Timber",
            "Gilbert": "Gilbert"
        },
        "description": "Neighborhood of the property."
    },

    "LotArea": {
        "description": "Total lot size in square feet."
    },
    "OverallQual": {
        "range": [1, 10],
        "description": "Material and finish quality (1 = Poor, 10 = Excellent)."
    },
    "OverallCond": {
        "range": [1, 10],
        "description": "Overall home condition rating (1 = Bad, 10 = Excellent)."
    },
    "YearBuilt": {
        "description": "Year the home was constructed."
    },
    "BedroomAbvGr": {
        "description": "Number of bedrooms above ground."
    },
    "FullBath": {
        "description": "Number of full bathrooms."
    },
    "GrLivArea": {
        "description": "Above-ground living area in square feet."
    },
    "GarageCars": {
        "description": "Number of cars the garage can hold."
    },
}
