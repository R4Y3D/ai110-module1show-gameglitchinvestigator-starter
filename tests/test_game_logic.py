from logic_utils import check_guess, get_range_for_difficulty


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests targeting the difficulty range bug (Hard was 1-50, easier than Normal 1-100)
def test_hard_range_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, "Hard range should be larger than Normal range"


def test_hard_range_is_not_50():
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high != 50, "Hard range was bugged at 50 (easier than Normal's 100)"


def test_easy_range_is_smallest():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high
