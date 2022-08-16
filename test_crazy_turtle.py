"""Tests for the Crazy Turtle Game."""
from crazy_turtle import (
    card_rotations,
    default_deck,
    filter_duplictates,
    find_solutions,
    match,
    rotate_card,
    rotate_grid,
    search,
)


def test_find_solutions() -> None:
    """Test for find_solutions."""
    assert all_solutions == find_solutions(default_deck, processors=1)


def test_filter_duplicates() -> None:
    """Test for filter_duplicates."""
    assert filtered_solutions == filter_duplictates(all_solutions)


def test_rotate_card() -> None:
    """Test for rotate_card."""
    assert rotate_card(list("abcd")) == list("dabc")


def test_card_rotations() -> None:
    """Test for card_rotations."""
    rotations = list(card_rotations(list("abcd")))

    assert len(rotations) == 4
    assert rotations[0] == list("abcd")
    assert rotations[1] == list("dabc")
    assert rotations[2] == list("cdab")
    assert rotations[3] == list("bcda")


def test_match() -> None:
    """Test for match."""
    assert match("RH", "RT")
    assert match("OH", "OT")
    assert match("GH", "GT")
    assert match("BH", "BT")
    assert not match("RH", "RH")
    assert not match("RT", "RT")
    assert not match("GT", "RH")


def test_rotate_grid() -> None:
    """Test rotate_grid."""
    deck = [[x] for x in list("abcdefghi")]
    assert rotate_grid(deck) == [[x] for x in list("gdahebifc")]


def test_search() -> None:
    """Test for search."""
    deck_with_no_solution = [
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
    deck_with_solution = [
        ["RH", "OH", "GT", "BT"],
        ["BT", "GH", "OH", "RT"],
        ["GT", "OT", "GH", "BH"],
        ["RH", "OT", "BT", "GH"],
        ["BH", "OT", "GT", "RH"],
        ["GH", "BT", "OT", "RH"],
        ["GT", "BT", "RH", "OH"],
        ["RT", "OT", "GH", "BH"],
        ["OH", "RT", "BT", "RH"],
    ]

    result = [
        [
            ["BT", "RH", "OH", "GT"],
            ["BT", "GH", "OH", "RT"],
            ["OT", "GH", "BH", "GT"],
            ["OT", "BT", "GH", "RH"],
            ["OT", "GT", "RH", "BH"],
            ["BT", "OT", "RH", "GH"],
            ["GT", "BT", "RH", "OH"],
            ["RT", "OT", "GH", "BH"],
            ["RT", "BT", "RH", "OH"],
        ]
    ]

    assert search(deck_with_no_solution) == []
    assert search(deck_with_solution) == result


all_solutions = [
    [
        ["RH", "OH", "RT", "BT"],
        ["GH", "BH", "RT", "OT"],
        ["RH", "OH", "GT", "BT"],
        ["RH", "GH", "BT", "OT"],
        ["RH", "BH", "OT", "GT"],
        ["GH", "RH", "OT", "BT"],
        ["BH", "GT", "OT", "GH"],
        ["OH", "RT", "BT", "GH"],
        ["OH", "GT", "BT", "RH"],
    ],
    [
        ["RH", "OH", "RT", "BT"],
        ["GH", "BH", "RT", "OT"],
        ["RH", "OH", "GT", "BT"],
        ["RH", "GH", "BT", "OT"],
        ["RH", "BH", "OT", "GT"],
        ["GH", "RH", "OT", "BT"],
        ["BH", "GT", "OT", "GH"],
        ["OH", "RT", "BT", "GH"],
        ["OH", "GT", "BT", "RH"],
    ],
    [
        ["OH", "RT", "BT", "RH"],
        ["OH", "GT", "BT", "RH"],
        ["RH", "OT", "BT", "GH"],
        ["BH", "GT", "OT", "GH"],
        ["BH", "RT", "OT", "GH"],
        ["BH", "OT", "GT", "RH"],
        ["OH", "GT", "BT", "RH"],
        ["OH", "RT", "BT", "GH"],
        ["GH", "BT", "OT", "RH"],
    ],
    [
        ["OH", "RT", "BT", "RH"],
        ["OH", "GT", "BT", "RH"],
        ["RH", "OT", "BT", "GH"],
        ["BH", "GT", "OT", "GH"],
        ["BH", "RT", "OT", "GH"],
        ["BH", "OT", "GT", "RH"],
        ["OH", "GT", "BT", "RH"],
        ["OH", "RT", "BT", "GH"],
        ["GH", "BT", "OT", "RH"],
    ],
    [
        ["GH", "BH", "GT", "OT"],
        ["OT", "RH", "GH", "BT"],
        ["BT", "RH", "OH", "RT"],
        ["GH", "OH", "RT", "BT"],
        ["GT", "RH", "BH", "OT"],
        ["OT", "GH", "BH", "RT"],
        ["RH", "OH", "GT", "BT"],
        ["BT", "GH", "RH", "OT"],
        ["BT", "RH", "OH", "GT"],
    ],
    [
        ["GH", "BH", "GT", "OT"],
        ["OT", "RH", "GH", "BT"],
        ["BT", "RH", "OH", "RT"],
        ["GH", "OH", "RT", "BT"],
        ["GT", "RH", "BH", "OT"],
        ["OT", "GH", "BH", "RT"],
        ["RH", "OH", "GT", "BT"],
        ["BT", "GH", "RH", "OT"],
        ["BT", "RH", "OH", "GT"],
    ],
    [
        ["OT", "RH", "GH", "BT"],
        ["BT", "GH", "OH", "RT"],
        ["BT", "RH", "OH", "GT"],
        ["GT", "RH", "BH", "OT"],
        ["OT", "GH", "BH", "RT"],
        ["OT", "GH", "BH", "GT"],
        ["BT", "GH", "RH", "OT"],
        ["BT", "RH", "OH", "GT"],
        ["BT", "RH", "OH", "RT"],
    ],
    [
        ["OT", "RH", "GH", "BT"],
        ["BT", "GH", "OH", "RT"],
        ["BT", "RH", "OH", "GT"],
        ["GT", "RH", "BH", "OT"],
        ["OT", "GH", "BH", "RT"],
        ["OT", "GH", "BH", "GT"],
        ["BT", "GH", "RH", "OT"],
        ["BT", "RH", "OH", "GT"],
        ["BT", "RH", "OH", "RT"],
    ],
    [
        ["RH", "OH", "GT", "BT"],
        ["GH", "BH", "GT", "OT"],
        ["RH", "OH", "RT", "BT"],
        ["GH", "OH", "RT", "BT"],
        ["GH", "BH", "RT", "OT"],
        ["RH", "OH", "GT", "BT"],
        ["RH", "GH", "BT", "OT"],
        ["RH", "BH", "OT", "GT"],
        ["GH", "RH", "OT", "BT"],
    ],
    [
        ["OH", "GT", "BT", "RH"],
        ["RH", "OT", "BT", "GH"],
        ["GT", "BT", "RH", "OH"],
        ["BH", "RT", "OT", "GH"],
        ["BH", "OT", "GT", "RH"],
        ["RT", "BT", "GH", "OH"],
        ["OH", "RT", "BT", "RH"],
        ["GH", "BT", "OT", "RH"],
        ["GT", "OT", "GH", "BH"],
    ],
    [
        ["BT", "RH", "OH", "GT"],
        ["BT", "GH", "OH", "RT"],
        ["OT", "GH", "BH", "GT"],
        ["OT", "BT", "GH", "RH"],
        ["OT", "GT", "RH", "BH"],
        ["BT", "OT", "RH", "GH"],
        ["GT", "BT", "RH", "OH"],
        ["RT", "OT", "GH", "BH"],
        ["RT", "BT", "RH", "OH"],
    ],
    [
        ["RH", "OH", "GT", "BT"],
        ["GH", "BH", "GT", "OT"],
        ["RH", "OH", "RT", "BT"],
        ["GH", "OH", "RT", "BT"],
        ["GH", "BH", "RT", "OT"],
        ["RH", "OH", "GT", "BT"],
        ["RH", "GH", "BT", "OT"],
        ["RH", "BH", "OT", "GT"],
        ["GH", "RH", "OT", "BT"],
    ],
    [
        ["OH", "GT", "BT", "RH"],
        ["RH", "OT", "BT", "GH"],
        ["GT", "BT", "RH", "OH"],
        ["BH", "RT", "OT", "GH"],
        ["BH", "OT", "GT", "RH"],
        ["RT", "BT", "GH", "OH"],
        ["OH", "RT", "BT", "RH"],
        ["GH", "BT", "OT", "RH"],
        ["GT", "OT", "GH", "BH"],
    ],
    [
        ["BT", "RH", "OH", "GT"],
        ["BT", "GH", "OH", "RT"],
        ["OT", "GH", "BH", "GT"],
        ["OT", "BT", "GH", "RH"],
        ["OT", "GT", "RH", "BH"],
        ["BT", "OT", "RH", "GH"],
        ["GT", "BT", "RH", "OH"],
        ["RT", "OT", "GH", "BH"],
        ["RT", "BT", "RH", "OH"],
    ],
    [
        ["OT", "BT", "GH", "RH"],
        ["OT", "GT", "RH", "BH"],
        ["BT", "OT", "RH", "GH"],
        ["GT", "BT", "RH", "OH"],
        ["RT", "OT", "GH", "BH"],
        ["RT", "BT", "GH", "OH"],
        ["RT", "BT", "RH", "OH"],
        ["GT", "OT", "GH", "BH"],
        ["GT", "BT", "RH", "OH"],
    ],
    [
        ["OT", "BT", "GH", "RH"],
        ["OT", "GT", "RH", "BH"],
        ["BT", "OT", "RH", "GH"],
        ["GT", "BT", "RH", "OH"],
        ["RT", "OT", "GH", "BH"],
        ["RT", "BT", "GH", "OH"],
        ["RT", "BT", "RH", "OH"],
        ["GT", "OT", "GH", "BH"],
        ["GT", "BT", "RH", "OH"],
    ],
]

filtered_solutions = [
    [
        ["RH", "OH", "RT", "BT"],
        ["GH", "BH", "RT", "OT"],
        ["RH", "OH", "GT", "BT"],
        ["RH", "GH", "BT", "OT"],
        ["RH", "BH", "OT", "GT"],
        ["GH", "RH", "OT", "BT"],
        ["BH", "GT", "OT", "GH"],
        ["OH", "RT", "BT", "GH"],
        ["OH", "GT", "BT", "RH"],
    ],
    [
        ["OH", "RT", "BT", "RH"],
        ["OH", "GT", "BT", "RH"],
        ["RH", "OT", "BT", "GH"],
        ["BH", "GT", "OT", "GH"],
        ["BH", "RT", "OT", "GH"],
        ["BH", "OT", "GT", "RH"],
        ["OH", "GT", "BT", "RH"],
        ["OH", "RT", "BT", "GH"],
        ["GH", "BT", "OT", "RH"],
    ],
]
