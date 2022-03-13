from pathlib import Path
from typing import List
import pandas as pd

if __name__ == "__main__":
    words_txt: Path = Path("words.txt")
    frequency_csv: Path = Path("frequency.csv")
    fives: List[str] = []
    frequency_df = pd.DataFrame(pd.read_csv(frequency_csv))
    with open(words_txt, encoding="utf-8") as words_file:
        line: str = words_file.readline().strip()
        while line:
            if len(line) == 5:
                fives.append(line.lower())
            line: str = words_file.readline().strip()
    fives_df: pd.DataFrame = pd.Series(fives, name="word").to_frame()
    wordle_df = pd.merge(frequency_df, fives_df, left_on="word", right_on="word")
    wordle_df["word"] = wordle_df.word.str.upper()
    wordle_df.to_csv("fives.csv", index=False)
