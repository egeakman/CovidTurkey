import sys
from pathlib import Path

sys.path.append(str(Path("..").absolute().parent))
from src import CovidTurkey


covid_turkey = CovidTurkey.covid_turkey()


for func in covid_turkey.__dir__():
    if func.startswith("get_"):
        print(func, getattr(covid_turkey, func)())
