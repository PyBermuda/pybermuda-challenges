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
import re
import random

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

    candidates = [_ for _ in WORDS]
    guess = initial_guess
    regex = "....."
    attempt = 0
    while True:
        attempt += 1
        clue = wordle.guess(guess).replace(" ", "")
        print(f"Attempt {attempt}, Guess: {guess}, Clue: {clue}")

        if "🟩" * 5 in clue:
            return guess

        required_letters = []
        prohibited_letters = []

        for j in range(5):
            if clue[j] == "🟨":
                required_letters.append(guess[j])
            if clue[j] == "🟩":
                regex = regex[:j] + guess[j] + regex[j+1:]
            if clue[j] == "⬜":
                prohibited_letters.append(guess[j])

        new_candidates = []
        for word in candidates:
            if (re.match(regex, word) 
                and all(letter in word for letter in required_letters) 
                and not any(letter in word for letter in prohibited_letters)
                and not word == guess):
                new_candidates.append(word)

        candidates = new_candidates
        
        if len(candidates) == 0:
            raise Exception("No solution found")
        guess = random.choice(candidates)
        


if __name__ == "__main__":
    game = Wordle()
    solution = solve_wordle(game, "HELLO")
    print(f"The solution is {solution}")
