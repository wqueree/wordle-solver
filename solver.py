from pathlib import Path
from typing import List, Set
import pandas as pd


def solve():
    """Solves Wordle"""
    fives: pd.DataFrame = pd.DataFrame(pd.read_csv(Path("fives.csv")))
    attempts: int = 6
    valid: Set[str] = set()
    while attempts > 0:
        test_word = fives.sample().iloc[0]["word"]
        test_word_chars: List[str] = list(test_word)
        print(f"ATTEMPT: {test_word}")
        colours: str = input("Enter character colours: ").upper()
        if colours == "GGGGG":
            return "WIN"
        colours_chars: List[str] = list(colours)
        for i, (letter, state) in enumerate(zip(test_word_chars, colours_chars)):
            if state == "B" and letter not in valid:
                fives = fives[~fives.word.str.contains(letter)]
            if state == "Y":
                fives = fives[fives.word.str.contains(letter)]
                valid.add(letter)
            elif state == "G":
                fives = fives[fives.word.str[i] == letter]
                valid.add(letter)
        attempts -= 1
    return "LOSS"


if __name__ == "__main__":
    print(f"RESULT: {solve()}")
