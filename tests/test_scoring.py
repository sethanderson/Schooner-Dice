from unittest import TestCase
from services.scoring import Scoring
from services.category import Category


# FULL HOUSE - 25 points if valid
class test_full_house(TestCase):
    def test_score_category_1(self):
        category = Category.FULL_HOUSE
        dice_roll = [1, 1, 1, 7, 7]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 25
        assert score == expected_score

    def test_score_category_2(self):
        category = Category.FULL_HOUSE
        dice_roll = [1, 1, 2, 7, 7]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_3(self):
        category = Category.FULL_HOUSE
        dice_roll = [1, 1, 2, 1, 1]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score


# singles (ONES, TWOS, THREES...) - sum of just those numbers
class test_singles(TestCase):
    def test_score_category_ones_1(self):
        category = Category.ONES
        dice_roll = [1, 1, 2, 7, 7]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 2
        assert score == expected_score

    def test_score_category_twos_1(self):
        category = Category.TWOS
        dice_roll = [2, 1, 2, 7, 7]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 4
        assert score == expected_score

    def test_score_category_threes_1(self):
        category = Category.THREES
        dice_roll = [1, 1, 2, 7, 7]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_fours_1(self):
        category = Category.FOURS
        dice_roll = [4, 4, 2, 4, 7]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 12
        assert score == expected_score

    def test_score_category_fives_1(self):
        category = Category.FIVES
        dice_roll = [1, 1, 2, 5, 7]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 5
        assert score == expected_score

    def test_score_category_sixes_1(self):
        category = Category.SIXES
        dice_roll = [1, 6, 6, 7, 6]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 18
        assert score == expected_score

    def test_score_category_sevens_1(self):
        category = Category.SEVENS
        dice_roll = [1, 1, 2, 7, 7]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 14
        assert score == expected_score

    def test_score_category_eights_1(self):
        category = Category.EIGHTS
        dice_roll = [8, 1, 2, 7, 7]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 8
        assert score == expected_score


# THREE OF A KIND - sum of all dice
class test_three_of_a_kind(TestCase):
    def test_score_category_1(self):
        category = Category.THREE_OF_A_KIND
        dice_roll = [1, 1, 2, 1, 1]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 6
        assert score == expected_score

    def test_score_category_2(self):
        category = Category.THREE_OF_A_KIND
        dice_roll = [3, 4, 2, 1, 1]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_3(self):
        category = Category.THREE_OF_A_KIND
        dice_roll = [8, 8, 8, 8, 8]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 40
        assert score == expected_score


# FOUR OF A KIND - sum of all dice
class test_four_of_a_kind(TestCase):
    def test_score_category_1(self):
        category = Category.FOUR_OF_A_KIND
        dice_roll = [1, 1, 2, 1, 1]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 6
        assert score == expected_score

    def test_score_category_2(self):
        category = Category.FOUR_OF_A_KIND
        dice_roll = [3, 4, 2, 1, 1]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_3(self):
        category = Category.FOUR_OF_A_KIND
        dice_roll = [8, 8, 8, 8, 8]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 40
        assert score == expected_score

    def test_score_category_4(self):
        category = Category.FOUR_OF_A_KIND
        dice_roll = [1, 1, 8, 8, 8]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score


# SMALL STRAIGHT - 30 if 4 in a sequence
class test_small_straight(TestCase):
    def test_score_category_1(self):
        category = Category.SMALL_STRAIGHT
        dice_roll = [1, 1, 2, 1, 1]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_2(self):
        category = Category.SMALL_STRAIGHT
        dice_roll = [1, 4, 2, 1, 3]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 30
        assert score == expected_score

    def test_score_category_3(self):
        category = Category.SMALL_STRAIGHT
        dice_roll = [5, 4, 2, 1, 3]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 30
        assert score == expected_score


# LARGE STRAIGHT - 40 if 5 in a sequence
class test_large_straight(TestCase):
    def test_score_category_1(self):
        category = Category.LARGE_STRAIGHT
        dice_roll = [1, 1, 2, 1, 1]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_2(self):
        category = Category.LARGE_STRAIGHT
        dice_roll = [1, 4, 2, 1, 3]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_3(self):
        category = Category.LARGE_STRAIGHT
        dice_roll = [5, 4, 2, 1, 3]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 40
        assert score == expected_score


# ALL DIFFERENT - 35 points if all different
class test_all_different(TestCase):
    def test_score_category_1(self):
        category = Category.ALL_DIFFERENT
        dice_roll = [1, 1, 2, 1, 1]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_2(self):
        category = Category.ALL_DIFFERENT
        dice_roll = [1, 4, 2, 1, 3]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_3(self):
        category = Category.ALL_DIFFERENT
        dice_roll = [5, 4, 2, 1, 3]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 35
        assert score == expected_score


# SCHOONER - 50 points if all 5 are the same
class test_schooner(TestCase):
    def test_score_category_1(self):
        category = Category.SCHOONER
        dice_roll = [1, 1, 2, 1, 1]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_2(self):
        category = Category.SCHOONER
        dice_roll = [1, 4, 2, 1, 3]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_3(self):
        category = Category.SCHOONER
        dice_roll = [5, 4, 2, 1, 3]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 0
        assert score == expected_score

    def test_score_category_4(self):
        category = Category.SCHOONER
        dice_roll = [8, 8, 8, 8, 8]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 50
        assert score == expected_score


# CHANCE - always give sume of dice
class test_chance(TestCase):
    def test_score_category_1(self):
        category = Category.CHANCE
        dice_roll = [1, 1, 2, 1, 1]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 6
        assert score == expected_score

    def test_score_category_2(self):
        category = Category.CHANCE
        dice_roll = [1, 4, 2, 1, 3]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 11
        assert score == expected_score

    def test_score_category_3(self):
        category = Category.CHANCE
        dice_roll = [5, 4, 2, 1, 3]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 15
        assert score == expected_score

    def test_score_category_4(self):
        category = Category.CHANCE
        dice_roll = [8, 8, 8, 8, 8]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 40
        assert score == expected_score

    def test_score_category_5(self):
        category = Category.CHANCE
        dice_roll = [1, 1, 1, 1, 8]
        scoring = Scoring(dice_roll)
        score = scoring.score_category(category)

        expected_score = 12
        assert score == expected_score


class test_get_top_categories(TestCase):
    def test_1(self):
        dice_roll = [3, 3, 3, 6, 7]
        scoring = Scoring(dice_roll)
        top_categories = sorted(scoring.get_top_categories())

        expected_top_categories = sorted([Category.THREE_OF_A_KIND, Category.CHANCE])
        assert top_categories == expected_top_categories

    def test_2(self):
        dice_roll = [3, 3, 3, 3, 3]
        scoring = Scoring(dice_roll)
        top_categories = sorted(scoring.get_top_categories())

        expected_top_categories = sorted([Category.SCHOONER])
        assert top_categories == expected_top_categories

    def test_3(self):
        dice_roll = [2, 3, 1, 6, 4]
        scoring = Scoring(dice_roll)
        top_categories = sorted(scoring.get_top_categories())

        expected_top_categories = sorted([Category.ALL_DIFFERENT])
        assert top_categories == expected_top_categories

    def test_4(self):
        dice_roll = [2, 3, 1, 5, 4]
        scoring = Scoring(dice_roll)
        top_categories = sorted(scoring.get_top_categories())

        expected_top_categories = sorted([Category.LARGE_STRAIGHT])
        assert top_categories == expected_top_categories

    def test_5(self):
        dice_roll = [8, 8, 8, 8, 8]
        scoring = Scoring(dice_roll)
        top_categories = sorted(scoring.get_top_categories())

        expected_top_categories = sorted([Category.SCHOONER])
        assert top_categories == expected_top_categories

    def test_6(self):
        dice_roll = [1, 1, 1, 1, 8]
        scoring = Scoring(dice_roll)
        top_categories = sorted(scoring.get_top_categories())

        expected_top_categories = sorted(
            [Category.FOUR_OF_A_KIND, Category.THREE_OF_A_KIND, Category.CHANCE]
        )
        assert top_categories == expected_top_categories
