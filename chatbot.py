"""
College Enquiry Chatbot - Core ML Engine
Uses TF-IDF vectorization + Cosine Similarity for intent matching
"""

import json
import random
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CollegeChatbot:
    def __init__(self, intents_path="Dataset/intents.json"):
        self.intents_path = intents_path
        self.intents = []
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
        self.pattern_matrix = None
        self.pattern_tags = []
        self.all_patterns = []
        self.confidence_threshold = 0.2

        self._load_intents()
        self._train()

    def _load_intents(self):
        """Load intents from JSON file."""
        with open(self.intents_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.intents = data["intents"]

    def _train(self):
        """Build TF-IDF matrix from all patterns."""
        for intent in self.intents:
            # Skip fallback intent if it exists
            if intent.get("intent") == "fallback" or intent.get("tag") == "fallback":
                continue
            # Support both "text" and "patterns" keys
            patterns = intent.get("text", intent.get("patterns", []))
            intent_name = intent.get("intent", intent.get("tag", "unknown"))
            for pattern in patterns:
                self.all_patterns.append(self._preprocess(pattern))
                self.pattern_tags.append(intent_name)

        if self.all_patterns:
            self.pattern_matrix = self.vectorizer.fit_transform(self.all_patterns)

    def _preprocess(self, text: str) -> str:
        """Lowercase, strip punctuation, normalize whitespace."""
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def _get_response(self, tag: str) -> str:
        """Return a random response for the matched intent tag."""
        for intent in self.intents:
            intent_name = intent.get("intent", intent.get("tag", ""))
            if intent_name == tag:
                return random.choice(intent["responses"])
        return self._fallback_response()

    def _fallback_response(self) -> str:
        """Return a fallback response."""
        for intent in self.intents:
            intent_name = intent.get("intent", intent.get("tag", ""))
            if intent_name == "fallback":
                return random.choice(intent["responses"])
        return "I'm not sure how to help with that. Please contact the college office for more information."

    def get_response(self, user_input: str) -> dict:
        """
        Process user input and return a response dict with:
        - response: str
        - tag: str
        - confidence: float
        """
        if not user_input or not user_input.strip():
            return {
                "response": "Please type a message so I can help you!",
                "tag": "empty",
                "confidence": 0.0,
            }

        cleaned = self._preprocess(user_input)

        # Rule-based shortcuts for very short inputs
        greetings = {"hi", "hello", "hey", "hii", "helo"}
        farewells = {"bye", "goodbye", "exit", "quit"}
        thanks = {"thanks", "thank you", "ty", "thx"}

        if cleaned in greetings:
            return {"response": self._get_response("greeting"), "tag": "greeting", "confidence": 1.0}
        if cleaned in farewells:
            return {"response": self._get_response("goodbye"), "tag": "goodbye", "confidence": 1.0}
        if cleaned in thanks:
            return {"response": self._get_response("thanks"), "tag": "thanks", "confidence": 1.0}

        # ML-based matching via TF-IDF cosine similarity
        if self.pattern_matrix is not None:
            try:
                user_vec = self.vectorizer.transform([cleaned])
                similarities = cosine_similarity(user_vec, self.pattern_matrix).flatten()
                best_idx = int(np.argmax(similarities))
                best_score = float(similarities[best_idx])

                if best_score >= self.confidence_threshold:
                    matched_tag = self.pattern_tags[best_idx]
                    return {
                        "response": self._get_response(matched_tag),
                        "tag": matched_tag,
                        "confidence": round(best_score, 4),
                    }
            except Exception:
                pass

        # Fallback
        return {
            "response": self._fallback_response(),
            "tag": "fallback",
            "confidence": 0.0,
        }
