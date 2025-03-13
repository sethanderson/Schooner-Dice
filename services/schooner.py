from services.category import Category
from services.scoring import Scoring
from typing import List


# returns the score of the dice for the specified category
def score(category: Category, dice_roll=List[int]) -> int:
    scoring = Scoring(dice_roll)
    return scoring.score_category(category)


# returns the best scoring category of all qualifying categories, or a list if there is a tie
def topCategory(dice_roll=List[int]) -> List[Category]:
    scoring = Scoring(dice_roll)
    top_categories = scoring.get_top_categories()
    return top_categories
