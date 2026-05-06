import re
import unicodedata
from difflib import SequenceMatcher

# Limit input size (basic DoS protection)
MAX_INPUT_LENGTH = 5000


# --- Normalize input (handles obfuscation)
def normalize_input(text: str) -> str:
    text = text[:MAX_INPUT_LENGTH]
    text = text.lower()

    # Normalize unicode (handles tricky characters)
    text = unicodedata.normalize("NFKC", text)

    # Leetspeak replacements
    substitutions = str.maketrans({
        "0": "o",
        "1": "i",
        "3": "e",
        "4": "a",
        "5": "s",
        "7": "t"
    })
    text = text.translate(substitutions)

    # Remove spaced letters: "h a c k" → "hack"
    text = re.sub(
        r"\b(?:[a-z]\s+){2,}[a-z]\b",
        lambda m: m.group(0).replace(" ", ""),
        text
    )

    # Remove punctuation
    text = re.sub(r"[^\w\s]", " ", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


# --- Similarity check
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


# --- Known attack phrases
ATTACK_PATTERNS = [
    "ignore previous instructions",
    "ignore instructions",
    "bypass security",
    "act as a hacker",
    "give admin access",
    "execute system command"
]


# --- Keyword scoring
KEYWORDS = {
    "ignore": 1,
    "bypass": 2,
    "hack": 2,
    "admin": 2,
    "exploit": 2,
    "override": 1
}


# --- Main guardrail function
def guardrail_check(prompt: str):
    text = normalize_input(prompt)

    score = 0

    # 🔥 NEW: Track best matching phrase
    best_match = None
    best_score = 0

    # Phrase similarity scoring
    for phrase in ATTACK_PATTERNS:
        sim = similarity(text, phrase)

        # Track best match always (for explanation)
        if sim > best_score:
            best_score = sim
            best_match = phrase

        # Strong match → increase score
        if sim > 0.75:
            score += 3

    # Keyword scoring
    for word, weight in KEYWORDS.items():
        if word in text:
            score += weight

    # Decision
    if score >= 3:
        return {
            "status": "BLOCKED",
            "risk_score": score,
            "reason": best_match if best_match and best_score > 0.5 else "Suspicious pattern detected",
            "normalized_input": text  # optional but useful for debugging/demo
        }

    return {
        "status": "ALLOWED",
        "risk_score": score
    }
