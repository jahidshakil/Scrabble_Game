import pytest
from scrabble_game import calculate_score, validate_word_length, is_valid_word

def test_calculate_score():
    assert calculate_score('cabbage') == 14
    assert calculate_score('hello') == 8
    assert calculate_score('Scrabble') == 14  # Case insensitive

def test_invalid_input():
    with pytest.raises(ValueError):
        calculate_score('12345') #not an alphabet
    with pytest.raises(ValueError):
        calculate_score('cabbage123')
    with pytest.raises(ValueError):
        calculate_score('hello!')

def test_word_length_validation():
    assert not validate_word_length('hello', 6)  # Word 'hello' has 5 letters
    assert validate_word_length('hello', 5)      # Word 'hello' has 5 letters

def test_valid_word_check():
    assert is_valid_word('hello')   # Assume 'hello' is valid
    assert not is_valid_word('asdfgh') # Assume 'asdfgh' is not valid
