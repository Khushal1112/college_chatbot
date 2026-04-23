"""
Quick smoke tests for the chatbot engine (no Flask needed).
Run: python test_chatbot.py
"""

from chatbot import CollegeChatbot

bot = CollegeChatbot()

test_cases = [
    ("hello",                    "greeting"),
    ("how to apply for admission","admission"),
    ("what courses do you offer", "course"),
    ("fee structure",             "fees"),
    ("scholarship details",       "scholarship"),
    ("hostel facility",           "hostel"),
    ("placement record",          "placement"),
    ("contact number",            "number"),
    ("campus facilities",         "facilities"),
    ("exam schedule",             "exam"),
    ("bye",                       "goodbye"),
    ("xyzabc random gibberish",   "fallback"),
]

print(f"{'Input':<35} {'Expected':<15} {'Got':<15} {'Conf':>6}  {'Pass'}")
print("-" * 85)

passed = 0
for user_input, expected_tag in test_cases:
    result = bot.get_response(user_input)
    ok = result["tag"] == expected_tag
    passed += ok
    status = "✅" if ok else "❌"
    print(f"{user_input:<35} {expected_tag:<15} {result['tag']:<15} {result['confidence']:>6.3f}  {status}")

print(f"\n{passed}/{len(test_cases)} tests passed.")
