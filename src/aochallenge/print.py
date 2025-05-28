#!/usr/bin/python3


def print_condensed(data: list[list[int | str]]):
    for row in data:
        print(*row, sep="")


def print_csv(data: list[list[int | str]]):
    for row in data:
        print(*row, sep=",")


def print_arranged(data: list[list[int | str]]):
    col_widths: list[int] = []
    for r, row in enumerate(data):
        for c, value in enumerate(row):
            data_width = len(str(value))
            if c >= len(col_widths):
                col_widths.append(data_width)
            elif data_width > col_widths[c]:
                col_widths[c] = data_width
    for r, row in enumerate(data):
        for c, value in enumerate(row):
            if c:
                print(" ", end="")
            if type(value) == int:
                print(str(value).rjust(col_widths[c]), end="")
            else:
                print(str(value).ljust(col_widths[c]), end="")
        print("")
