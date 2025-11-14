import json
import re
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "microsoft/phi-2"

extractor = pipeline(
    "text-generation",
    model=model_name,
    device_map="auto",
    max_new_tokens=200,
    temperature=0.2,
)

def truncate(text, max_chars=500):
    """Avoids token overflow by safely truncating input."""
    return text[:max_chars]

def repair_json(text):
    text = text.strip()
    start = text.find("{")
    end = text.rfind("}") + 1

    if start == -1 or end == -1:
        return {}

    text = text[start:end]

    text = re.sub(r",\s*}", "}", text)
    text = re.sub(r"(\w+):", r'"\1":', text)

    try:
        return json.loads(text)
    except:
        return {}

def extract_features_with_llm(description):
    description = truncate(description)  # ←★ Fix token overflow

    prompt = f"""
Extract ONLY the following fields as JSON:
MSZoning, LotArea, OverallQual, OverallCond, YearBuilt, HouseStyle,
BedroomAbvGr, FullBath, GrLivArea, Neighborhood, GarageCars.

Return JSON only.

Description: {description}

JSON:
"""

    raw = extractor(prompt)[0]["generated_text"]
    cleaned = repair_json(raw)

    return cleaned
