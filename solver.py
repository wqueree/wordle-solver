"""Solves Wordle"""

from pathlib import Path
from typing import List, Set
import pandas as pd


def solve():
    """Solves Wordle"""
    fives: pd.DataFrame = pd.DataFrame(pd.read_csv(Path("fives.csv")))
    attempts: int = 6
    pattern_sets: List[Set[str]] = [{chr(i) for i in range(65, 91)} for i in range(5)]
    pattern_strings: List[str] = [0, 0, 0, 0, 0]
    while attempts > 0:
        attempt_valid = set()
        test_word = fives.iloc[0]["word"]
        test_word_chars: List[str] = list(test_word)
        print(f"ATTEMPT: {test_word}")
        colours: str = input("Enter character colours: ").upper()
        if colours == "GGGGG":
            return "WIN"
        colours_chars: List[str] = list(colours)
        global_invalid = set()
        for i, (letter, state) in enumerate(zip(test_word_chars, colours_chars)):
            if state == "B" and letter not in attempt_valid:
                global_invalid.add(letter)
            if state == "Y":
                fives = fives[fives.word.str.contains(letter)]
                attempt_valid.add(letter)
                pattern_sets[i].remove(letter)
            elif state == "G":
                fives = fives[fives.word.str[i] == letter]
                pattern_sets[i] = {letter}
        for i, elem in enumerate(pattern_sets):
            if len(elem) > 1:
                pattern_sets[i] -= global_invalid
            pattern_strings[i] = f"[{''.join(list(pattern_sets[i]))}]"
        reduction_pattern = "".join(pattern_strings)
        fives = fives[fives.word.str.contains(reduction_pattern)]
        attempts -= 1
    return "LOSS"


if __name__ == "__main__":
    print(f"RESULT: {solve()}")
