import sys
from pathlib import Path

sys.path.append(str(Path("..").absolute().parent))
from src import CovidTurkey

cases = CovidTurkey.covid_turkey.cases()


def test_cases_formatted():
    for func in cases.__dir__():
        if func.startswith("get_"):
            try:
                print(f"{func} (Formatted): {getattr(cases, func)(formatted=True)}")
            except TypeError:
                print(f"{func} (Couldn't format): {getattr(cases, func)()}")


def test_cases_unformatted():
    for func in cases.__dir__():
        if func.startswith("get_"):
            print(f"{func} (Unformatted): {getattr(cases, func)()}")


test_cases_formatted()
test_cases_unformatted()
