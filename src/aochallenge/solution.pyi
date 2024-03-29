from typing import Any, Generator

class Solution:
    basename: str
    def __init__(self) -> None: ...
    def load(self, splitlines: bool = ..., splitrecords: Union[str, None] = ..., recordtype: Union[list, tuple, type, None] = ..., *, lut: Union[dict[Union[str, None], Any], None] = ...) -> Union[list[Union[str, int, list]], Any]: ...
    def convert_records(self, content, recordtype: Union[list, tuple, type]) -> list: ...
    def solve_more(self) -> Generator[Union[int, str], None, None]: ...
    def print_condensed(self, data: list[list[Union[int, str]]]): ...
    def print_csv(self, data: list[list[Union[int, str]]]): ...
    def print_arranged(self, data: list[list[Union[int, str]]]): ...
    def main(self) -> None: ...
