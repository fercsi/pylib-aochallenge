from .grid import Grid2D as Grid2D, T as T
from .solution import Solution as Solution

def print_condensed(data: Grid2D[T]) -> None: ...
def print_csv(data: Grid2D[T]) -> None: ...
def print_arranged(data: Grid2D[T]) -> None: ...
def print_solution(solution: Solution, *, indent: str = ...) -> None: ...
