"""Writing several functions to help organize a cozy tea party"""

__author__: str = "730652013"


def tea_bags(people: int) -> int:
    """returns number of tea bags needed based on number of guests"""
    return people * 2  # assuming 2 bags of tea per guest


def treats(people: int) -> int:
    """returns number of treats needed based on number of guests"""
    return int(
        tea_bags(people=people) * 1.5
    )  # returns 1.5 times the teabags result, converted to int to match return type


def cost(tea_count: int, treat_count: int) -> float:
    """returns total cost of tea bags and treats"""
    return (
        tea_count * 0.50 + treat_count * 0.75
    )  # multiplies tea bags and treats by their respective price, then sums all costs


def main_planner(guests: int) -> None:
    """prints number of tea bags, treats, and total cost based on guests"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # introduces the prompt and displays how many guests will be attending
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # obtains and prints number of tea bags by calling tea_bags function
    print(
        "Treats: " + str(treats(people=guests))
    )  # obtains and prints number of treats by calling treats function
    print(
        "Cost:  $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # obtains and prints total cost of tea bags and treats by calling cost function
    # calls both tea_bags function and treats function to get values for cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
