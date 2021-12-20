import sys
from pathlib import Path

sys.path.append(str(Path("..").absolute().parent))
from src import CovidTurkey

dr = CovidTurkey.covid_turkey.deaths_and_recovered()


def test_dr():
    for func in dr.__dir__():
        if func.startswith("get_"):
            print(f"{func}: {getattr(dr, func)()}")


test_dr()
