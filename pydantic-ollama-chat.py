import json
import re
from typing import Optional
from pprint import pprint
from pydantic import BaseModel, Field
from openai import OpenAI
from loguru import logger

# Client for Ollama
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def extract_json_block(generate_fn, max_retries: int = 3) -> Optional[dict]:
    """Retry model response until a valid JSON object is extracted."""
    for attempt in range(1, max_retries + 1):
        text = generate_fn()
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError as e:
                logger.warning(f"[Attempt {attempt}] JSON decode error: {e}")
        else:
            logger.warning(f"[Attempt {attempt}] No JSON object found in response.")

    logger.error("❌ Failed to extract valid JSON after retries.")
    return None

def coa(inci: str):
    class SimpleToxReport(BaseModel):
        inci_name: str = Field(..., description="INCI 名稱")
        synonyms: Optional[str] = Field(None, description="其他名稱（如 IUPAC 名、俗名）")
        molecular_formula: Optional[str] = Field(None, description="分子式")
        molecular_weight: Optional[float] = Field(None, description="分子量（g/mol）")
        melting_point: Optional[str] = Field(None, description="熔點")
        boiling_point: Optional[str] = Field(None, description="沸點")
        vapor_pressure: Optional[str] = Field(None, description="蒸氣壓")
        solubility: Optional[str] = Field(None, description="溶解度")

    prompt = f"""
    Please provide the chemical information about "{inci}".
    STRICTLY return the output as JSON only, using the exact format below.
    Use only double quotes, no units in numeric fields, and don't include explanations.

    Format:
    {{
    "inci_name": "{inci}",
    "synonyms": "string",
    "molecular_formula": "string",
    "molecular_weight": float,
    "melting_point": "string",
    "boiling_point": "string",
    "vapor_pressure": "string",
    "solubility": "string"
    }}
    """
    def generate_response():
        response = client.chat.completions.create(
            model="llama3.2",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

    parsed = extract_json_block(generate_response)
    logger.info(f"Querying CoA for: {inci}")
    response = client.chat.completions.create(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    #content = response.choices[0].message.content.strip()
    #parsed = extract_json_block(content)

    if parsed:
        try:
            result = SimpleToxReport(**parsed)
            pprint(result.model_dump())
            return result
        except Exception as e:
            logger.error(f"❌ Failed to parse JSON output: {e}")
            pprint(parsed)
    else:
        logger.error("❌ No valid JSON found in response.")
        #print("Raw model output:\n", content)

    return "No result."

# Example usage
if __name__ == "__main__":
    coa("Cyclohexanone")