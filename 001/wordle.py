"""
WORDLE SOLVER

https://www.nytimes.com/games/wordle/index.html

Your task is to create a `solve_wordle` function that takes in a wordle puzzle
and an initial guess, solves the puzzle, and returns the word.

A `Wordle` class has been provided for you, which has a `guess` method that
takes in a word and returns a clue. The clue is a string of 5 characters,
where each character is one of:
- 🟩: The letter is in the correct position
- 🟨: The letter is in the word, but not in the correct position
- ⬜: The letter is not in the word

With 'proper' Wordle, you would have 6 guesses to solve the puzzle. However,
this restriction has not been implemented here. You can make as many guesses as
you like (though in all likelihood, your `solve_wordle` function won't need
more than 6).

Obviously, your `solve_wordle` function should not access the `Wordle` object's
`.secret` attribute directly. That would be cheating. You should only use the 
`.guess` method to get clues.

BONUS:
At the moment, initialising a `Wordle` object with a word results in one being
chosen at random from `WORDS`. You could change this behaviour to use the 
NY Times API to pull today's word, add it to `WORDS` if it isn't already there,
and *then* solve the puzzle.

The API URL is:
https://www.nytimes.com/svc/wordle/v2/YYYY-MM-DD.json
(replacing YYYY-MM-DD with today's date)
"""
from urllib.request import urlopen
from random import choice

WORD_LIST_URL = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"

with urlopen(WORD_LIST_URL) as f:
    WORDS = f.read().decode("utf-8").upper().splitlines()


class Wordle:
    def __init__(self, word: str | None = None) -> None:
        self._secret = word or choice(WORDS)
        self.clues: list[str] = []

    def guess(self, word: str) -> str:
        word = word.upper()
        assert len(word) == 5, "Word must be 5 letters long"

        clue: str = ["⬜"] * 5

        for i, letter in enumerate(word):
            if letter in self._secret:
                if letter == self._secret[i]:
                    clue[i] = "🟩"
                else:
                    clue[i] = "🟨"

        self.clues.append(" ".join(clue))

        return self.clues[-1]


def solve_wordle(wordle: Wordle, initial_guess: str) -> str:
    """
    Solves a wordle puzzle using the given initial guess
    """
    """
    Solves a wordle puzzle using the given initial guess
    """
    # write your code here 👇👇
    # letter_list = list(initial_guess)
    # initial_clue = list(Wordle().guess("HELLO"))
    # initial_clue = [x for x in initial_clue if x!=' ']
    
    
    letter_range = range(0,5)
    word_list = [ "-"  for i in letter_range ]
    contains_list = []
    doesnt_contain_list = []


    ## Code to filter list of words
    full_word_dict = [{"L"+str(i) : list(word)[i] for i in  letter_range} for word in WORDS]
    full_word_df = pd.DataFrame(full_word_dict)

    filtered_word_df = full_word_df

    filtered_word_count = len(filtered_word_df)
    attempt_num =1
    
    guess = initial_guess
    clue_string=""
    while clue_string != '🟩🟩🟩🟩🟩' and attempt_num<200:
        word = guess
        letter_list = list(word)
        clue = list(wordle.guess(word))
        clue_list = [x for x in clue if x!=' ']
        clue_string = ''.join(clue_list)
        
        for i, letter in enumerate(clue_list):
            if letter=='🟩': 
                word_list[i]= letter_list[i]
            elif letter=='🟨': 
                contains_list.append(letter_list[i])
            else:
                doesnt_contain_list.append(letter_list[i])
            

        print(word, clue_list, word_list)
        # check_letters = lambda row:any(letter in row for letter in contains_list)

        # green_filter = df.apply(lambda row:all(row[col]==letter and col==index for index, (col,letter) in enumerate(zip(df.columns,letters_list)),axis=1)

        # Filter from green list
        for i, word_guess in enumerate(word_list):
            if clue_list[i]=="🟩":
                df_index = "L"+str(i)
                filtered_word_df = filtered_word_df[filtered_word_df[df_index] == word_guess]
            else:
                filtered_word_df= filtered_word_df
            # filtered_word_df = filtered_word_df.copy()


        # Filter from yellow list
        yellow_clue = lambda row:any(letter in row for letter in contains_list)
        filtered_word_df = filtered_word_df[filtered_word_df.map(yellow_clue).any(axis=1)]
        # filtered_word_df = filtered_word_df.copy()
        
        # Remaining list
        filtered_word_count=len(filtered_word_df)
        print(filtered_word_count)
        # clue_string = ''.join(clue_list)
        ##clue_list = ''.join(clue_list.values[0])
        if clue_string == '🟩🟩🟩🟩🟩':
            pass
        elif filtered_word_count>1:
            attempt_num+=1
            sampled_row = filtered_word_df.sample(n=1, replace=False)
            guess = ''.join(sampled_row.values[0])
        else:
            attempt_num+=1
            sampled_row = filtered_word_df
            guess = ''.join(sampled_row.values)

    return guess


if __name__ == "__main__":
    game = Wordle()
    solution = solve_wordle(game, "HELLO")
    print(f"The solution is {solution}")
