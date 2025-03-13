from typing import List
from services.category import Category
import more_itertools as mit


class Scoring:
    FULL_HOUSE_SCORE = 25
    SMALL_STRAIGHT_SCORE = 30
    LARGE_STRAIGHT_SCORE = 40
    ALL_DIFFERENT_SCORE = 35
    SCHOONER_SCORE = 50

    def __init__(self, dice_roll: List[int]):
        counts = [
            dice_roll.count(1),
            dice_roll.count(2),
            dice_roll.count(3),
            dice_roll.count(4),
            dice_roll.count(5),
            dice_roll.count(6),
            dice_roll.count(7),
            dice_roll.count(8),
        ]
        sorted_set = list(set(sorted(dice_roll)))
        list_of_straights = [
            list(group) for group in mit.consecutive_groups(sorted_set)
        ]
        longest_straight = max(list_of_straights, key=len)

        self.counts = counts
        self.longest_straight = longest_straight
        self.roll_sum = sum(dice_roll)

    def __qualifies(self, category: Category) -> bool:
        roll_qualifies = False

        match category:
            case Category.ONES:
                roll_qualifies = True
            case Category.TWOS:
                roll_qualifies = True
            case Category.THREES:
                roll_qualifies = True
            case Category.FOURS:
                roll_qualifies = True
            case Category.FIVES:
                roll_qualifies = True
            case Category.SIXES:
                roll_qualifies = True
            case Category.SEVENS:
                roll_qualifies = True
            case Category.EIGHTS:
                roll_qualifies = True
            case Category.THREE_OF_A_KIND:
                if 5 in self.counts or 4 in self.counts or 3 in self.counts:
                    roll_qualifies = True
            case Category.FOUR_OF_A_KIND:
                if 5 in self.counts or 4 in self.counts:
                    roll_qualifies = True
            case Category.FULL_HOUSE:
                if 3 in self.counts and 2 in self.counts:
                    roll_qualifies = True
            case Category.SMALL_STRAIGHT:
                if len(self.longest_straight) >= 4:
                    roll_qualifies = True
            case Category.LARGE_STRAIGHT:
                if len(self.longest_straight) >= 5:
                    roll_qualifies = True
            case Category.ALL_DIFFERENT:
                if self.counts.count(1) == 5:
                    roll_qualifies = True
            case Category.SCHOONER:
                if 5 in self.counts:
                    roll_qualifies = True
            case Category.CHANCE:
                roll_qualifies = True

        return roll_qualifies

    def score_category(self, category: Category) -> int:
        # kicked back with 0 if the category isn't valid for the roll
        if not self.__qualifies(category):
            return 0

        match category:
            case Category.ONES:
                return self.counts[0] * 1
            case Category.TWOS:
                return self.counts[1] * 2
            case Category.THREES:
                return self.counts[2] * 3
            case Category.FOURS:
                return self.counts[3] * 4
            case Category.FIVES:
                return self.counts[4] * 5
            case Category.SIXES:
                return self.counts[5] * 6
            case Category.SEVENS:
                return self.counts[6] * 7
            case Category.EIGHTS:
                return self.counts[7] * 8
            case Category.THREE_OF_A_KIND:
                return self.roll_sum
            case Category.FOUR_OF_A_KIND:
                return self.roll_sum
            case Category.FULL_HOUSE:
                return self.FULL_HOUSE_SCORE
            case Category.SMALL_STRAIGHT:
                return self.SMALL_STRAIGHT_SCORE
            case Category.LARGE_STRAIGHT:
                return self.LARGE_STRAIGHT_SCORE
            case Category.ALL_DIFFERENT:
                return self.ALL_DIFFERENT_SCORE
            case Category.SCHOONER:
                return self.SCHOONER_SCORE
            case Category.CHANCE:
                return self.roll_sum
            case _:
                return 0

    def get_top_categories(self) -> List[Category]:
        # get all category and score pairs of the dice roll and sort them descending
        category_values = [(c.value, self.score_category(c.value)) for c in Category]
        sorted_category_values = sorted(
            category_values, key=lambda x: x[1], reverse=True
        )

        # grab only the scores and see if there are multiple of the top value
        score_values = [x[1] for x in sorted_category_values]
        count_of_highest_value = score_values.count(score_values[0])

        # grab that number off the top of just the list of categories
        sorted_categories = [x[0] for x in sorted_category_values]
        return sorted_categories[:count_of_highest_value]
