import pytest

from aochallenge.grid import *

########## Coord2D ####################

@pytest.mark.parametrize(
    "a, b, expected, should_fail",
    [
        (Coord2D(2, 3), Coord2D(1, -1), Coord2D(3, 2), False),
        (Coord2D(2, 3), (4, 5), Coord2D(6, 8), False),
        (Coord2D(2, 3), 10, Coord2D(12, 13), False),
        (Coord2D(2, 3), "invalid", None, True),
        (Coord2D(2, 3), [1, 2], None, True),
        (Coord2D(2, 3), None, None, True),
    ]
)
def test_add_2d(a, b, expected, should_fail):
    if should_fail:
        with pytest.raises(TypeError):
            _ = a + b
    else:
        assert a + b == expected


@pytest.mark.parametrize(
    "a, b, expected, should_fail",
    [
        (Coord2D(5, 7), Coord2D(2, 3), Coord2D(3, 4), False),
        (Coord2D(5, 7), (1, 2), Coord2D(4, 5), False),
        (Coord2D(5, 7), 3, Coord2D(2, 4), False),
        (Coord2D(5, 7), "wrong", None, True),
        (Coord2D(5, 7), [1, 2], None, True),
        (Coord2D(5, 7), {}, None, True),
    ]
)
def test_sub_2d(a, b, expected, should_fail):
    if should_fail:
        with pytest.raises(TypeError):
            _ = a - b
    else:
        assert a - b == expected

########## Coord3D ####################

@pytest.mark.parametrize(
    "a, b, expected, should_fail",
    [
        (Coord3D(1, 2, 3), Coord3D(4, 5, 6), Coord3D(5, 7, 9), False),
        (Coord3D(1, 2, 3), (4, 5, 6), Coord3D(5, 7, 9), False),
        (Coord3D(1, 2, 3), 10, Coord3D(11, 12, 13), False),
        (Coord3D(1, 2, 3), "invalid", None, True),
        (Coord3D(1, 2, 3), (1, 2), None, True),
        (Coord3D(1, 2, 3), None, None, True),
    ]
)
def test_add_3d(a, b, expected, should_fail):
    if should_fail:
        with pytest.raises(TypeError):
            _ = a + b
    else:
        assert a + b == expected

@pytest.mark.parametrize(
    "a, b, expected, should_fail",
    [
        (Coord3D(10, 10, 10), Coord3D(3, 4, 5), Coord3D(7, 6, 5), False),
        (Coord3D(10, 10, 10), (1, 2, 3), Coord3D(9, 8, 7), False),
        (Coord3D(10, 10, 10), 5, Coord3D(5, 5, 5), False),
        (Coord3D(10, 10, 10), [1, 2, 3], None, True),
        (Coord3D(10, 10, 10), (1, 2), None, True),
        (Coord3D(10, 10, 10), {}, None, True),
    ]
)
def test_sub_3d(a, b, expected, should_fail):
    if should_fail:
        with pytest.raises(TypeError):
            _ = a - b
    else:
        assert a - b == expected

########## is_within ####################

@pytest.mark.parametrize(
    "coord, corner1, corner2, expected",
    [
        (Coord2D(5, 5), Coord2D(0, 0), Coord2D(10, 10), True),
        ((5, 5), (0, 0), (10, 10), True),
        ((0, 0), (0, 0), (0, 0), True),
        ((-1, -1), (0, 0), (10, 10), False),
        ((11, 11), (0, 0), (10, 10), False),
        ((5, 11), (0, 0), (10, 10), False),
    ]
)
def test_is_within_2d(coord, corner1, corner2, expected):
    assert is_within_2d(coord, corner1, corner2) == expected


@pytest.mark.parametrize(
    "coord, corner1, corner2, expected",
    [
        (Coord3D(5, 5, 5), Coord3D(0, 0, 0), Coord3D(10, 10, 10), True),
        ((5, 5, 5), (0, 0, 0), (10, 10, 10), True),
        ((0, 0, 0), (0, 0, 0), (0, 0, 0), True),
        ((-1, -1, -1), (0, 0, 0), (10, 10, 10), False),
        ((5, 5, 11), (0, 0, 0), (10, 10, 10), False),
    ]
)
def test_is_within_3d(coord, corner1, corner2, expected):
    assert is_within_3d(coord, corner1, corner2) == expected

########## neighbours 2D ####################

@pytest.mark.parametrize(
    "coord, expected",
    [
        (Coord2D(0, 0), [Coord2D(0, 1), Coord2D(1, 0), Coord2D(0, -1), Coord2D(-1, 0)]),
        (Coord2D(2, 2), [Coord2D(2, 3), Coord2D(3, 2), Coord2D(2, 1), Coord2D(1, 2)]),
    ]
)
def test_neighbours_2d(coord, expected):
    assert sorted(neighbours_2d(coord)) == sorted(expected)


@pytest.mark.parametrize(
    "coord, corner1, corner2, expected",
    [
        (Coord2D(0, 0), Coord2D(0, 0), Coord2D(1, 1), [Coord2D(1, 0), Coord2D(0, 1)]),
        (Coord2D(1, 1), Coord2D(0, 0), Coord2D(1, 1), [Coord2D(0, 1), Coord2D(1, 0)]),
        (Coord2D(0, 0), Coord2D(5, 5), Coord2D(10, 10), []),
    ]
)
def test_bounded_neighbours_2d(coord, corner1, corner2, expected):
    assert sorted(bounded_neighbours_2d(coord, corner1, corner2)) == sorted(expected)


@pytest.mark.parametrize(
    "coord, expected",
    [
        (Coord2D(0, 0), [
            Coord2D(-1, -1), Coord2D(0, -1), Coord2D(1, -1),
            Coord2D(-1, 0),                  Coord2D(1, 0),
            Coord2D(-1, 1),  Coord2D(0, 1),  Coord2D(1, 1),
        ]),
        (Coord2D(1, 1), [
            Coord2D(0, 0), Coord2D(1, 0), Coord2D(2, 0),
            Coord2D(0, 1),                Coord2D(2, 1),
            Coord2D(0, 2), Coord2D(1, 2), Coord2D(2, 2),
        ]),
    ]
)
def test_neighbours_full_2d(coord, expected):
    assert sorted(neighbours_full_2d(coord)) == sorted(expected)


@pytest.mark.parametrize(
    "coord, corner1, corner2, expected",
    [
        (Coord2D(0, 0), Coord2D(0, 0), Coord2D(0, 0), []),
        (Coord2D(0, 2), Coord2D(0, 0), Coord2D(2, 2), [
            Coord2D(0, 1), Coord2D(1, 1),
                           Coord2D(1, 2),
        ]),
        (Coord2D(1, 0), Coord2D(0, 0), Coord2D(2, 2), [
            Coord2D(0, 0),                Coord2D(2, 0),
            Coord2D(0, 1), Coord2D(1, 1), Coord2D(2, 1),
        ]),
        (Coord2D(1, 1), Coord2D(0, 0), Coord2D(2, 2), [
            Coord2D(0, 0), Coord2D(1, 0), Coord2D(2, 0),
            Coord2D(0, 1),                Coord2D(2, 1),
            Coord2D(0, 2), Coord2D(1, 2), Coord2D(2, 2),
        ]),
        (Coord2D(1, 1), Coord2D(5, 5), Coord2D(10, 10), []),
    ]
)
def test_bounded_neighbours_full_2d(coord, corner1, corner2, expected):
    assert sorted(bounded_neighbours_full_2d(coord, corner1, corner2)) == sorted(expected)

########## neighbours 3D 5####################

@pytest.mark.parametrize(
    "coord, expected",
    [
        (Coord3D(0, 0, 0), [
            Coord3D(1, 0, 0), Coord3D(-1, 0, 0),
            Coord3D(0, 1, 0), Coord3D(0, -1, 0),
            Coord3D(0, 0, 1), Coord3D(0, 0, -1),
        ]),
        (Coord3D(1, 1, 1), [
            Coord3D(2, 1, 1), Coord3D(0, 1, 1),
            Coord3D(1, 2, 1), Coord3D(1, 0, 1),
            Coord3D(1, 1, 2), Coord3D(1, 1, 0),
        ]),
    ]
)
def test_neighbours_3d(coord, expected):
    assert sorted(neighbours_3d(coord)) == sorted(expected)


@pytest.mark.parametrize(
    "coord, corner1, corner2, expected",
    [
        (Coord3D(0, 0, 0), Coord3D(-1, -1, -1), Coord3D(0, 0, 0), [
            Coord3D(-1, 0, 0), Coord3D(0, -1, 0), Coord3D(0, 0, -1),
        ]),
        (Coord3D(5, 5, 5), Coord3D(0, 0, 0), Coord3D(4, 4, 4), []),
    ]
)
def test_bounded_neighbours_3d(coord, corner1, corner2, expected):
    assert sorted(bounded_neighbours_3d(coord, corner1, corner2)) == sorted(expected)


@pytest.mark.parametrize(
    "coord, expected",
    [
        (Coord3D(0, 0, 0), [
            Coord3D(1, 0, 0), Coord3D(-1, 0, 0),
            Coord3D(0, 1, 0), Coord3D(0, -1, 0),
            Coord3D(0, 0, 1), Coord3D(0, 0, -1),

            Coord3D(0,1,1),   Coord3D(1,0,1),   Coord3D(1,1,0),
            Coord3D(0,1,-1),  Coord3D(1,0,-1),  Coord3D(1,-1,0),
            Coord3D(0,-1,1),  Coord3D(-1,0,1),  Coord3D(-1,1,0),
            Coord3D(0,-1,-1), Coord3D(-1,0,-1), Coord3D(-1,-1,0),
        ]),
    ]
)
def test_neighbours_edge_3d(coord, expected):
    assert sorted(neighbours_edge_3d(coord)) == sorted(expected)


@pytest.mark.parametrize(
    "coord, corner1, corner2, expected",
    [
        (Coord3D(0, 0, 0), Coord3D(0, 0, 0), Coord3D(0, 0, 0), []),
        (Coord3D(0, 0, 1), Coord3D(0, 0, 0), Coord3D(2, 2, 2), [
            Coord3D(1, 0, 1),
            Coord3D(0, 1, 1),
            Coord3D(0, 0, 2), Coord3D(0, 0, 0),

            Coord3D(0,1,2),  Coord3D(1,0,2),  Coord3D(1,1,1),
            Coord3D(0,1,0),  Coord3D(1,0,0),
        ]),
    ]
)
def test_bounded_neighbours_edge_3d(coord, corner1, corner2, expected):
    assert sorted(bounded_neighbours_edge_3d(coord, corner1, corner2)) == sorted(expected)


@pytest.mark.parametrize(
    "coord, expected_count",
    [
        (Coord3D(0, 0, 0), 26),
        (Coord3D(5, 5, 5), 26),
    ]
)
def test_neighbours_full_3d(coord, expected_count):
    result = neighbours_full_3d(coord)
    assert len(result) == expected_count
    assert Coord3D(0, 0, 0) not in result


@pytest.mark.parametrize(
    "coord, corner1, corner2, expected",
    [
        (Coord3D(0, 0, 0), Coord3D(0, 0, 0), Coord3D(0, 0, 0), []),
        (Coord3D(1, 1, 1), Coord3D(0, 0, 0), Coord3D(2, 2, 2), [
            Coord3D(0, 0, 0), Coord3D(0, 0, 1), Coord3D(0, 0, 2),
            Coord3D(0, 1, 0), Coord3D(0, 1, 1), Coord3D(0, 1, 2),
            Coord3D(0, 2, 0), Coord3D(0, 2, 1), Coord3D(0, 2, 2),
            Coord3D(1, 0, 0), Coord3D(1, 0, 1), Coord3D(1, 0, 2),
            Coord3D(1, 1, 0),                 Coord3D(1, 1, 2),
            Coord3D(1, 2, 0), Coord3D(1, 2, 1), Coord3D(1, 2, 2),
            Coord3D(2, 0, 0), Coord3D(2, 0, 1), Coord3D(2, 0, 2),
            Coord3D(2, 1, 0), Coord3D(2, 1, 1), Coord3D(2, 1, 2),
            Coord3D(2, 2, 0), Coord3D(2, 2, 1), Coord3D(2, 2, 2),
        ]),
    ]
)
def test_bounded_neighbours_full_3d(coord, corner1, corner2, expected):
    assert sorted(bounded_neighbours_full_3d(coord, corner1, corner2)) == sorted(expected)

########## Grid setters and getters 5####################

@pytest.mark.parametrize(
    "grid, pos, value, expected",
    [
        ([[0, 0], [0, 0]], Coord2D(0, 0), 1, [[1, 0], [0, 0]]),
        ([[9, 9], [9, 9]], Coord2D(1, 1), 5, [[9, 9], [9, 5]]),
    ]
)
def test_set_element_2d(grid, pos, value, expected):
    set_element_2d(grid, pos, value)
    assert grid == expected


@pytest.mark.parametrize(
    "grid, pos, expected",
    [
        ([[1, 2], [3, 4]], Coord2D(0, 0), 1),
        ([[1, 2], [3, 4]], Coord2D(1, 1), 4),
    ]
)
def test_get_element_2d(grid, pos, expected):
    assert get_element_2d(grid, pos) == expected


@pytest.mark.parametrize(
    "grid, pos, value, expected",
    [
        ([[[0, 0], [0, 0]], [[0, 0], [0, 0]]], Coord3D(0, 0, 0), 7,
         [[[7, 0], [0, 0]], [[0, 0], [0, 0]]]),
        ([[[1, 1], [1, 1]], [[1, 1], [1, 1]]], Coord3D(1, 1, 1), 9,
         [[[1, 1], [1, 1]], [[1, 1], [1, 9]]]),
    ]
)
def test_set_element_3d(grid, pos, value, expected):
    set_element_3d(grid, pos, value)
    assert grid == expected


@pytest.mark.parametrize(
    "grid, pos, expected",
    [
        ([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], Coord3D(0, 0, 0), 1),
        ([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], Coord3D(1, 1, 1), 8),
    ]
)
def test_get_element_3d(grid, pos, expected):
    assert get_element_3d(grid, pos) == expected

########## iterators ####################

@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [[1, 2], [3, 4]],
            [
                (Coord2D(0, 0), 1), (Coord2D(1, 0), 2),
                (Coord2D(0, 1), 3), (Coord2D(1, 1), 4)
            ]
        ),
        (
            [[5]],
            [(Coord2D(0, 0), 5)]
        ),
        (
            [],
            []
        ),
        (
            [[], []],
            []
        ),
    ]
)
def test_iter_grid_2d(grid, expected):
    result = list(iter_grid_2d(grid))
    assert result == expected

@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [[[1, 2], [3, 4]],[[5, 6], [7, 8]]],
            [
                (Coord3D(0, 0, 0), 1), (Coord3D(1, 0, 0), 2),
                (Coord3D(0, 1, 0), 3), (Coord3D(1, 1, 0), 4),
                (Coord3D(0, 0, 1), 5), (Coord3D(1, 0, 1), 6),
                (Coord3D(0, 1, 1), 7), (Coord3D(1, 1, 1), 8),
            ]
        ),
        (
            [[[5]]],
            [(Coord3D(0, 0, 0), 5)]
        ),
        (
            [],
            []
        ),
        (
            [[], []],
            []
        ),
    ]
)
def test_iter_grid_3d(grid, expected):
    result = list(iter_grid_3d(grid))
    assert result == expected
