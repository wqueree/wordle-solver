from pathlib import Path
from typing import List, Set
import pandas as pd


def solve():
    """Solves Wordle"""
    fives: pd.DataFrame = pd.DataFrame(pd.read_csv(Path("fives.csv")))
    attempts: int = 6
    valid: Set[str] = {chr(i) for i in range(65, 91)}
    pattern = ["[ABCDEFGHIJKLMNOPQRSTUVWXYZ]"] * 5
    while attempts > 0:
        attempt_valid = set()
        test_word = fives.iloc[0]["word"]
        test_word_chars: List[str] = list(test_word)
        print(f"ATTEMPT: {test_word}")
        colours: str = input("Enter character colours: ").upper()
        if colours == "GGGGG":
            return "WIN"
        colours_chars: List[str] = list(colours)
        invalid = set()
        for i, (letter, state) in enumerate(zip(test_word_chars, colours_chars)):
            if state == "B" and letter not in attempt_valid:
                invalid.add(letter)
            if state == "Y":
                fives = fives[fives.word.str.contains(letter)]
                attempt_valid.add(letter)
            elif state == "G":
                fives = fives[fives.word.str[i] == letter]
                pattern[i] = letter
        valid -= invalid
        new_pattern = f"[{''.join(list(valid))}]"
        for j, elem in enumerate(pattern):
            if len(elem) > 1:
                pattern[j] = new_pattern
        fives = fives[fives.word.str.contains("".join(pattern))]
        attempts -= 1
    return "LOSS"


if __name__ == "__main__":
    print(f"RESULT: {solve()}")
