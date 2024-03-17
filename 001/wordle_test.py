import pytest
import wordle as w

def make_display_string(text: str):
    return " ".join(list(text.replace("Y", "🟩").replace("M", "🟨").replace("N", "⬜")))

def test_implementation_matches_on_correct_match():
    wordle = w.Wordle("APPLE")
    assert wordle.guess("APPLE") == make_display_string("YYYYY")

def test_how_implementation_marks_second_letter_when_only_one():
    wordle = w.Wordle("APPLE")
    assert wordle.guess("BAAED") == make_display_string("NMMMN")
    # If following official wordle rules, the above test would fail because the second A should be marked as not present.

def test_how_implementation_marks_second_letter_when_there_are_two():
    wordle = w.Wordle("APPLE")
    assert wordle.guess("CUPPA") == make_display_string("NNYMM")

def test_how_implementation_handles_false_words():
    wordle = w.Wordle("APPLE")
    assert wordle.guess("XXYZZ") == make_display_string("NNNNN")
    # If following official wordle rules, we would expect some sort of error since the word is invalid.

def test_call_limit():
    wordle = w.Wordle("APPLE")
    wordle.guess("CUPPA")
    wordle.guess("CUPPA")
    wordle.guess("CUPPA")
    wordle.guess("CUPPA")
    wordle.guess("CUPPA")
    wordle.guess("CUPPA")
    # If following official wordle rules, the above test would fail because the call limit has been exceeded.
    wordle.guess("CUPPA")
    wordle.guess("CUPPA")
    wordle.guess("CUPPA")
    wordle.guess("CUPPA")