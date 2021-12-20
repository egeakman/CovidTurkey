import sys
from pathlib import Path

sys.path.append(str(Path("..").absolute().parent))
from src import CovidTurkey

cases = CovidTurkey.covid_turkey.cases()

for func in cases.__dir__():
    if func.startswith("get_"):
        print(f"{func}: {getattr(cases, func)()}")
