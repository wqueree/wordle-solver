# Wordle Solver

Simple python script I developed to solve [wordle](https://www.nytimes.com/games/wordle/index.html) puzzles.

## Strategy
The solution is built up from two scripts, one (`generate_fives.py`) which preprocesses a word list to be passed in as a text file, and another (`solver.py`) which actually uses this data in conjunction with user input to arrive at a solution.

### Preprocessing
The preprocessing step takes in a list of words as a text file, then sorts them according to how common they are in a Pandas DataFrame. The input files provided are `words.txt` and `frequency.csv`.

### Solver
`solver.py` loads an input file (`fives.csv`) as a Pandas DataFrame, and in each iteration takes element at the top of the DataFrame as its guess for that round.

The user then needs to input a pattern of states for each character based on the output of the game as a five character string, where the inputs can be `G`(reen), `Y`(ellow) or `B`(lack). So, the string for a partially correct guess could be `GBBYB`.

The DataFrame is then filtered according to this output. My solution uses regular expressions for each character to apply this filtering.

Each index has its own set of possible charcters that are used to build up a filtering regular expression at the end of a round. Clearly, at the start of the game, each index has the full alphabet in this set. Indices that receive the output `G` have their sets reduced to only containing that character. Those that result in `Y` have that character removed only for that index, as well as reducing the input set only to those that contain that character. Those that receive output `B` have the character removed from the sets at every index.

From here, we are able to build a regular expression string to filter by.

## Improvements

Sorting the wordle answer set, which is what `words.txt` contains, by how common those words are is bogus, as each of those words is (in theory) equally likely. 

An improvement I propose to fix this is one that allows us to eliminate as many words as possible. So, first sorting by words that only contain unique letters, and then by those that contain the most common characters in the english language.