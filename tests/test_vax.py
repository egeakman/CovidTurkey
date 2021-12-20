import sys
from pathlib import Path

sys.path.append(str(Path("..").absolute().parent))
from src import CovidTurkey

vax = CovidTurkey.covid_turkey.vaccination()


def test_vax():
    for func in vax.__dir__():
        if func.startswith("get_"):
            print(f"{func}: {getattr(vax, func)()}")
