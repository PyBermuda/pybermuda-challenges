# PyBermuda Challenges

This repository contains scripts for small Python challenges to try, and subsequently discuss, at PyBermuda meetups.

It is recommended that you [fork this repository](https://github.com/PyBermuda/pybermuda-challenges/fork) and keep a the copy on your own GitHub account. [harrymunro](https://github.com/harrymunro) kindly [shared a guide](https://jarv.is/notes/how-to-pull-request-fork-github/) on how to do this 😊

## Environment

It is strongly recommended to use a virtual environment to run these challenges. To create a new virtual environment, run the following command:

```bash
python -m venv venv
```

To activate the virtual environment, run the following command:

```bash
source venv/bin/activate
```

To deactivate the virtual environment, run the following command:

```bash
deactivate
```

There are other ways to create and manage virtual environments, but this is the simplest way to get started. Check out `pyenv`, `conda`, or `poetry` to learn more.

## Installing dependencies

To install the dependencies for all challenges, run the following command:

```bash
pip install -r requirements.txt
```

If, on the way through, you add a new dependency, you can update the `requirements.txt` file by running:

```bash
pip freeze > requirements.txt
```

## Links

|Meetup|Challenge|Description|
|------|---------|-----------|
|`0.0.1`|[Wordle](001/wordle.py)|Write a function which solves a [Wordle](https://www.nytimes.com/games/wordle/index.html) puzzle.|
|`0.0.2`|[Fibonacci](002/fibonacci.py)|Write a function which returns the _n_th number in the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)|
|`0.0.3`|[Sorting](003/sort.py)|Implement a sorting algorithm without using in-built Python sorting functions / methods|
|`0.0.4`|[Zombie outbreak simulations](004/zombie_outbreak_sim.py)|The objective is to simulate the spread of a zombie outbreak in a grid-based city.|

## Participants

If you want to out yourself as a participant, open a PR and add your name (and a link to your repo) to the list below:

- [gtm19](https://github.com/gtm19/pybermuda-challenges)
