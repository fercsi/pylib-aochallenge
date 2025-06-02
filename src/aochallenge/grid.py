#!/usr/bin/python3

from __future__ import annotations
import itertools
from typing import Iterator, NamedTuple, Self, TypeAlias, TypeVar


# Note, that we use "type: ignore[override]", because we override the default
# types of NamedTuple operators
class Coord2D(NamedTuple):
    x: int
    y: int

    def __add__(self, other: Coord2D | tuple[int, int] | int) -> Coord2D:  # type: ignore[override]
        if isinstance(other, Coord2D):
            return Coord2D(self.x + other.x, self.y + other.y)
        if isinstance(other, tuple) and len(other) == 2:
            return Coord2D(self.x + other[0], self.y + other[1])
        if isinstance(other, int):
            return Coord2D(self.x + other, self.y + other)
        return NotImplemented

    def __sub__(self, other: Coord2D | tuple[int, int] | int) -> Coord2D:  # type: ignore[override]
        if isinstance(other, Coord2D):
            return Coord2D(self.x - other.x, self.y - other.y)
        if isinstance(other, tuple) and len(other) == 2:
            return Coord2D(self.x - other[0], self.y - other[1])
        if isinstance(other, int):
            return Coord2D(self.x - other, self.y - other)
        return NotImplemented


class Coord3D(NamedTuple):
    x: int
    y: int
    z: int

    def __add__(self, other: Coord3D | tuple[int, int, int] | int) -> Coord3D:  # type: ignore[override]
        if isinstance(other, Coord3D):
            return Coord3D(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, tuple) and len(other) == 3:
            return Coord3D(self.x + other[0], self.y + other[1], self.z + other[2])
        if isinstance(other, int):
            return Coord3D(self.x + other, self.y + other, self.z + other)
        return NotImplemented

    def __sub__(self, other: Coord3D | tuple[int, int, int] | int) -> Coord3D:  # type: ignore[override]
        if isinstance(other, Coord3D):
            return Coord3D(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, tuple) and len(other) == 3:
            return Coord3D(self.x - other[0], self.y - other[1], self.z - other[2])
        if isinstance(other, int):
            return Coord3D(self.x - other, self.y - other, self.z - other)
        return NotImplemented


_Coord2D = Coord2D | tuple[int, int]
_Coord3D = Coord3D | tuple[int, int, int]

def manhattan_2d(a: _Coord2D, b: _Coord2D) -> int:
    d = _c2d(a) - b
    return abs(d.x) + abs(d.y)

def manhattan_3d(a: _Coord3D, b: _Coord3D) -> int:
    d = _c3d(a) - b
    return abs(d.x) + abs(d.y) + abs(d.z)

def is_within_2d(coord: _Coord2D, corner1: _Coord2D, corner2: _Coord2D) -> bool:
    v = _c2d(coord)
    c1 = _c2d(corner1)
    c2 = _c2d(corner2)
    return v.x >= c1.x and v.y >= c1.y and v.x <= c2.x and v.y <= c2.y


def is_within_3d(coord: _Coord3D, corner1: _Coord3D, corner2: _Coord3D) -> bool:
    v = _c3d(coord)
    c1 = _c3d(corner1)
    c2 = _c3d(corner2)
    return (
        v.x >= c1.x
        and v.y >= c1.y
        and v.z >= c1.z
        and v.x <= c2.x
        and v.y <= c2.y
        and v.z <= c2.z
    )


def neighbours_2d(coord: _Coord2D) -> list[Coord2D]:
    return [d + coord for d in _neighbour_direct_2d]


def bounded_neighbours_2d(
    coord: _Coord2D, corner1: _Coord2D, corner2: _Coord2D
) -> list[Coord2D]:
    return [
        d + coord
        for d in _neighbour_direct_2d
        if is_within_2d(d + coord, corner1, corner2)
    ]


def neighbours_full_2d(coord: _Coord2D) -> list[Coord2D]:
    return [d + coord for d in _neighbour_corner_2d]


def bounded_neighbours_full_2d(
    coord: _Coord2D, corner1: _Coord2D, corner2: _Coord2D
) -> list[Coord2D]:
    return [
        d + coord
        for d in _neighbour_corner_2d
        if is_within_2d(d + coord, corner1, corner2)
    ]


def neighbours_3d(coord: _Coord3D) -> list[Coord3D]:
    return [d + coord for d in _neighbour_direct_3d]


def bounded_neighbours_3d(
    coord: _Coord3D, corner1: _Coord3D, corner2: _Coord3D
) -> list[Coord3D]:
    return [
        d + coord
        for d in _neighbour_direct_3d
        if is_within_3d(d + coord, corner1, corner2)
    ]


def neighbours_edge_3d(coord: _Coord3D) -> list[Coord3D]:
    return [d + coord for d in _neighbour_edge_3d]


def bounded_neighbours_edge_3d(
    coord: _Coord3D, corner1: _Coord3D, corner2: _Coord3D
) -> list[Coord3D]:
    return [
        d + coord
        for d in _neighbour_edge_3d
        if is_within_3d(d + coord, corner1, corner2)
    ]


def neighbours_full_3d(coord: _Coord3D) -> list[Coord3D]:
    return [d + coord for d in _neighbour_corner_3d]


def bounded_neighbours_full_3d(
    coord: _Coord3D, corner1: _Coord3D, corner2: _Coord3D
) -> list[Coord3D]:
    return [
        d + coord
        for d in _neighbour_corner_3d
        if is_within_3d(d + coord, corner1, corner2)
    ]

########## Grids ####################

T = TypeVar("T")

# from Python 3.12 (mypy is also not prepared for this, yet)
#type MutableGrid2D[T] = list[list[T]]
#type _ImmutableDim[T] = tuple[T, ...]|str
#type _ImmutableGrid2D[T] = tuple[_immutableDim[T], ...]|list[_immutableDim[T]]
#type Grid2D[T] = MutableGrid2D[T]|_ImmutableGrid2D[T]
#type MutableGrid3D[T] = list[list[list[T]]]
#type _ImmutableGrid23[T] = tuple[_immutableGrid2D[T], ...]|list[_immutableGrid2D[T]]
#type Grid3D[T] = MutableGrid3D[T]|_ImmutableGrid3D[T]

MutableGrid2D: TypeAlias = list[list[T]]
Grid2D: TypeAlias = list[list[T]]|tuple[tuple[T, ...], ...]
MutableGrid3D: TypeAlias = list[list[list[T]]]
Grid3D: TypeAlias = list[list[list[T]]]|tuple[tuple[tuple[T, ...], ...], ...]


def set_element_2d(grid: MutableGrid2D[T], pos: _Coord2D, value: T) -> None:
    p = _c2d(pos)
    grid[p.y][p.x] = value


def get_element_2d(grid: Grid2D[T], pos: _Coord2D) -> T:
    p = _c2d(pos)
    return grid[p.y][p.x]


def set_element_3d(grid: MutableGrid3D[T], pos: _Coord3D, value: T) -> None:
    p = _c3d(pos)
    grid[p.z][p.y][p.x] = value


def get_element_3d(grid: Grid3D[T], pos: _Coord3D) -> T:
    p = _c3d(pos)
    return grid[p.z][p.y][p.x]


def iter_grid_2d(grid: Grid2D[T]) -> Iterator[tuple[Coord2D, T]]:
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            yield Coord2D(x, y), value


def iter_grid_3d(grid: Grid3D[T]) -> Iterator[tuple[Coord3D, T]]:
    for z, plane in enumerate(grid):
        for y, row in enumerate(plane):
            for x, value in enumerate(row):
                yield Coord3D(x, y, z), value


########## Simplify 2D interface ####################

Coord = Coord2D
#Grid = Grid2D
Grid: TypeAlias = list[list[T]]|tuple[tuple[T, ...], ...]
manhattan = manhattan_2d
is_within = is_within_2d
neighbours = neighbours_2d
bounded_neighbours = bounded_neighbours_2d
neighbours_full = neighbours_full_2d
bounded_neighbours_full = bounded_neighbours_full_2d
set_element = set_element_2d
get_element = get_element_2d
iter_grid = iter_grid_2d

########## private functions ####################


def _c2d(coord: _Coord2D) -> Coord2D:
    return coord if isinstance(coord, Coord2D) else Coord2D(*coord)


def _c3d(coord: _Coord3D) -> Coord3D:
    return coord if isinstance(coord, Coord3D) else Coord3D(*coord)


_neighbour_direct_2d: list[Coord2D] = []
_neighbour_corner_2d: list[Coord2D] = []
_neighbour_direct_3d: list[Coord3D] = []
_neighbour_edge_3d: list[Coord3D] = []
_neighbour_corner_3d: list[Coord3D] = []


def _initNeighbours() -> None:
    global _neighbour_direct_2d
    global _neighbour_corner_2d
    global _neighbour_direct_3d
    global _neighbour_edge_3d
    global _neighbour_corner_3d
    for x, y, z in itertools.product((-1, 0, 1), repeat=3):
        if (x, y, z) == (0, 0, 0):
            continue
        _neighbour_corner_3d.append(Coord3D(x, y, z))

        if x != 0 and y != 0 and z != 0:
            continue
        _neighbour_edge_3d.append(Coord3D(x, y, z))

        if z == 0:
            _neighbour_corner_2d.append(Coord2D(x, y))

        if (x ^ y ^ z) & 1 == 0:
            continue
        _neighbour_direct_3d.append(Coord3D(x, y, z))

        if z == 0:
            _neighbour_direct_2d.append(Coord2D(x, y))


_initNeighbours()
