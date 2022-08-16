"""Solve the Crazy Turtle Card Game."""
from itertools import chain, permutations
from multiprocessing import Pool
from os import cpu_count
from sys import stdout
from time import perf_counter_ns
from typing import Iterator, List

Card = List[str]
Deck = List[Card]

# Represent the turtle cards, using the letters
# The first letter is the color: Orange, Green, Brown, Red
# The second letter is the body part: Head, Tail
# The order in each row is top, left, botton, right
default_deck: Deck = [
    ["RT", "OT", "GH", "BH"],
    ["OH", "RT", "BT", "RH"],
    ["BH", "OT", "GT", "RH"],
    ["GT", "OT", "GH", "BH"],
    ["GH", "BT", "OT", "RH"],
    ["GT", "BT", "RH", "OH"],
    ["RH", "OH", "GT", "BT"],
    ["RH", "OT", "BT", "GH"],
    ["BT", "GH", "OH", "RT"],
]


def search(deck: Deck) -> List[Deck]:
    """Find a solution in this permutation of cards in the grid.

    Args:
        deck (Deck): the state of the deck

    Returns:
        List[Deck]: A list of decks found
    """
    results = []
    for a in card_rotations(deck[0]):
        for b in card_rotations(deck[1]):
            if not match(a[1], b[3]):
                continue
            for c in card_rotations(deck[2]):
                if not match(b[1], c[3]):
                    continue
                for d in card_rotations(deck[3]):
                    if not match(a[2], d[0]):
                        continue
                    for e in card_rotations(deck[4]):
                        if not match(b[2], e[0]) or not match(d[1], e[3]):
                            continue
                        for f in card_rotations(deck[5]):
                            if not match(c[2], f[0]) or not match(e[1], f[3]):
                                continue
                            for g in card_rotations(deck[6]):
                                if not match(d[2], g[0]):
                                    continue
                                for h in card_rotations(deck[7]):
                                    if not match(e[2], h[0]) or not match(g[1], h[3]):
                                        continue
                                    for i in card_rotations(deck[8]):
                                        if not match(f[2], i[0]) or not match(
                                            h[1], i[3]
                                        ):
                                            continue
                                        result = [a, b, c, d, e, f, g, h, i]
                                        results.append(result)
                                        stdout.write(".")
                                        stdout.flush()
    return results


def find_solutions(deck: Deck, processors: int = 1) -> List[Deck]:
    """Find all the possible solutions to the game.

    Args:
        deck (Deck): the deck of cards to solve
        processors (int): The number of processes in the pool. Defaults to 1.

    Returns:
        List[Deck]: the solutions
    """
    # setup the processing pool to do it's work
    with Pool(processes=processors) as pool:
        results = pool.starmap_async(
            search, [(x,) for x in permutations(deck, len(deck))]
        )
        results.wait()

        # filter out empty results, and flatten the lists
        return list(chain.from_iterable(filter(lambda x: x, results.get())))


def filter_duplictates(solutions: List[Deck]) -> List[Deck]:
    """Filter out the duplicate grids.

        The solver finds all solutions, which include viewing the same
        grid from each of the four angles, plus the doubling effect of
        having two identical cards in the deck.

    Args:
        solutions (List[Deck]): the input solutions

    Returns:
        List[Deck]: the filtered results
    """
    unique = []
    for solution in solutions:
        rotated_90 = rotate_grid(solution)
        rotated_180 = rotate_grid(rotated_90)
        rotated_270 = rotate_grid(rotated_180)
        if (
            solution not in unique
            and rotated_90 not in unique
            and rotated_180 not in unique
            and rotated_270 not in unique
        ):
            unique.append(solution)
    return unique


def rotate_card(card: Card) -> Card:
    """Return a view of the card, rotated 90 degrees clockwise.

    Args:
        card (Card): the input card

    Returns:
        Card: the rotated card
    """
    return card[3:4] + card[0:3]


def card_rotations(card: Card) -> Iterator[Card]:
    """Return a list of the 4 rotations of a card.

    Args:
        card (Card): the input card

    Yields:
        List[Card]: a list of cards
    """
    yield card
    for _ in range(3):
        card = rotate_card(card)
        yield card


def rotate_grid(deck: Deck) -> Deck:
    """Rotate the grid 90 degrees clockwise.

    Args:
        deck (Deck): The input grid

    Returns:
        Deck: A view of the deck, rotated
    """
    return [
        rotate_card(deck[6]),
        rotate_card(deck[3]),
        rotate_card(deck[0]),
        rotate_card(deck[7]),
        rotate_card(deck[4]),
        rotate_card(deck[1]),
        rotate_card(deck[8]),
        rotate_card(deck[5]),
        rotate_card(deck[2]),
    ]


def match(a: str, b: str) -> bool:
    """Check if the two turtle parts are matching.

    Args:
        a (str): first turtle part
        b (str): second turtle part

    Returns:
        bool: True if matching, otherwise false
    """
    return (a[0] == b[0]) and (
        (a[1] == "H" and b[1] == "T") or (a[1] == "T" and b[1] == "H")
    )


def main() -> None:  # pragma: no cover
    """Solves the Crazy Turtle Game."""
    print("Solving The 'Crazy Turle' Game")

    # find the solutions, using multiprocessing if possible
    start_time = perf_counter_ns()
    if processors := cpu_count():
        solutions = find_solutions(default_deck, processors=processors)
    else:
        solutions = find_solutions(default_deck)
    solutions = filter_duplictates(solutions)
    end_time = perf_counter_ns()

    # print the results
    print(
        f"\nFound {len(solutions)} unique solutions in "
        f"{(end_time - start_time)/1000000000:.2f}s."
    )
    for i, solution in enumerate(solutions):
        print()
        print(f"Solution {i + 1}")
        print(f"{solution[0]} : {solution[1]} : {solution[2]}")
        print(f"{solution[3]} : {solution[4]} : {solution[5]}")
        print(f"{solution[6]} : {solution[7]} : {solution[8]}")

    print("key:")
    print("colours   - Orange, Green, Brown, Red")
    print("body part - Head, Tail")


if __name__ == "__main__":  # pragma: no cover
    main()
