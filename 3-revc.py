COMPLIMENTS = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

def revc(s: str) -> str:
    return "".join(list(map(lambda char: COMPLIMENTS[char], s[::-1])))
