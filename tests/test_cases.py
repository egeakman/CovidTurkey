import sys
from pathlib import Path

sys.path.append(str(Path("..").absolute().parent))
from src import CovidTurkey

cases = CovidTurkey.covid_turkey.cases()


def test_cases():
    for func in cases.__dir__():
        if func.startswith("get_"):
            print(f"{func}: {getattr(cases, func)()}")


test_cases()
