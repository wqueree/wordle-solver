from pathlib import Path
from typing import List
import pandas as pd

if __name__ == "__main__":
    words_txt: Path = Path("words.txt")
    fives: List[str] = []
    with open(words_txt, encoding="utf-8") as words_file:
        line: str = words_file.readline().strip()
        while line:
            if len(line) == 5:
                fives.append(line.upper())
            line: str = words_file.readline().strip()
    fives_series: pd.Series = pd.Series(fives, name="word")
    fives_series.to_csv("fives.csv", index=False)
