from transformers import pipeline
import re
import json

extractor = pipeline("text2text-generation", model="google/flan-t5-small")

def extract_features(user_input: str):
    prompt = f"""
You are an assistant that extracts house features for price prediction.
Return valid JSON with these keys only:
MSZoning, LotArea, OverallQual, OverallCond, YearBuilt, HouseStyle, BedroomAbvGr, FullBath, GrLivArea, Neighborhood, GarageCars.

Rules:
- LotArea and GrLivArea must be in square feet (numeric)
- OverallQual and OverallCond between 1 and 10
- YearBuilt four digits
- MSZoning one of ['RL','RM','RH','FV','C']
- Neighborhood must be one from: CollgCr, OldTown, NridgHt, Sawyer, Gilbert, Timber
- HouseStyle one of ['1Story','2Story','1.5Fin','SLvl','SFoyer']

Text: "{user_input}"
"""


    response = extractor(prompt, max_new_tokens=150)[0]['generated_text']
    
    # Clean up and enforce valid JSON structure
    try:
        json_data = re.search(r'\{.*\}', response, re.DOTALL)
        if json_data:
            return json.loads(json_data.group(0))
        else:
            return {}
    except:
        return {}
