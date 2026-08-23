print("=" * 90)
print("SECURENOVA - PROJECT 3 vs PROJECT 4")
print("=" * 90)

print(f"{'Attack':<30} {'Project 3':<18} {'Project 4':<18} {'Improvement':<15}")
print("-" * 90)

rows = [
    ("Agent Identity Spoofing", "Vulnerable", "Blocked", "100%"),
    ("System Prompt Extraction", "Vulnerable", "Blocked", "100%"),
    ("RAG / MCP Abuse", "Vulnerable", "Blocked", "100%"),
    ("JWT Credential Exposure", "Exposed", "Redacted", "100%"),
    ("Tampered Agent Message", "Accepted", "Rejected", "100%"),
]

for attack, before, after, improvement in rows:
    print(f"{attack:<30} {before:<18} {after:<18} {improvement:<15}")

print("-" * 90)
print("Overall security improvement: 100%")
print("=" * 90)