from fastapi import FastAPI, Query
from typing import List
from services.category import Category
import services.schooner as schooner


app = FastAPI()


@app.get("/score/")
async def score(
    category: Category, diceRoll: List[int] = Query(min_length=5, max_length=5)
):
    return {"score": schooner.score(category, dice_roll=diceRoll)}


@app.get("/topCategories/")
async def top_categories(diceRoll: List[int] = Query(min_length=5, max_length=5)):
    return {"topCategories": schooner.topCategory(dice_roll=diceRoll)}
