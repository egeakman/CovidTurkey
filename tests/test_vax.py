# -*- coding: utf-8 -*-

import sys
from pathlib import Path

sys.path.append(str(Path("..").absolute().parent))
from src import CovidTurkey

vax = CovidTurkey.covid_turkey.vaccination()


def test_vax_formatted():
    for func in vax.__dir__():
        if func.startswith("get_"):
            try:
                print(f"{func} (Formatted): {getattr(vax, func)(formatted=True)}")
            except TypeError:
                print(f"{func} (Couldn't format): {getattr(vax, func)()}")


def test_vax_unformatted():
    for func in vax.__dir__():
        if func.startswith("get_"):
            print(f"{func} (Unformatted): {getattr(vax, func)()}")


# test_vax_formatted()
test_vax_unformatted()
