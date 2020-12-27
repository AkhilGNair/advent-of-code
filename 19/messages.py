from pathlib import Path
import re

test = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""


PTN_UNSOLVED = r"[0-9]"


def squish(s):
    return "".join(s.split())


def parse(text):

    text = text.strip()
    rules, messages = text.split("\n\n")

    rules = dict(x.split(": ") for x in rules.replace('"', "").split("\n"))
    sentinels = {k: v for k, v in rules.items() if not re.search(PTN_UNSOLVED, v)}

    rules = {k: f"( {v} )" for k, v in rules.items() if re.search(PTN_UNSOLVED, v)}
    rules.update(sentinels)

    # For part 2
    rules.pop("8")
    rules.pop("11")

    return rules, messages.split("\n")


def get_rule(r):
    got = rules.get(r)
    return got if got else r


def substitute(subrules):
    return " ".join(get_rule(r) for r in subrules)


def valid(rule):
    while re.search(PTN_UNSOLVED, rule):
        subrules = rule.split(" ")
        rule = substitute(subrules)
    return rule


text = Path("input.txt").read_text()
rules, messages = parse(text)
rule0 = rules["0"]

# 0:  8 | 11
# 8:  42 | 42 8
# 11: 42 31 | 42 11 31

# From the hint, rules 31 and 42 are deterministic
r31 = squish(f"{valid(rules['31'])}")
r42 = squish(f"{valid(rules['42'])}")

rule0 = f"^({r42}+){r42}{{n}}{r31}{{n}}$"

msgs = set()
for i in range(1, 200):
    msgs.update({m for m in messages if re.search(rule0.replace("n", str(i)), m)})

print("total:", len(messages))
print("valid:", len(msgs))
