import sys
from pathlib import Path

sys.path.append(str(Path("..").absolute().parent))
from src import CovidTurkey

dr = CovidTurkey.covid_turkey.deaths_and_recovered()


def test_dr_formatted():
    for func in dr.__dir__():
        if func.startswith("get_"):
            try:
                print(f"{func} (Formatted): {getattr(dr, func)(formatted=True)}")
            except TypeError:
                print(f"{func} (Couldn't format): {getattr(dr, func)()}")


def test_dr_unformatted():
    for func in dr.__dir__():
        if func.startswith("get_"):
            print(f"{func} (Unformatted): {getattr(dr, func)()}")


test_dr_formatted()
test_dr_unformatted()
