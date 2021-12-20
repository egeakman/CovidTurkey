import sys
from pathlib import Path

sys.path.append(str(Path("..").absolute().parent))
from src import CovidTurkey

covid = CovidTurkey.covid_turkey()

for func in covid.cases.__dir__():
    if func.startswith("get_"):
        print(func, getattr(covid.cases, func)())

for func in covid.vaccination.__dir__():
    if func.startswith("get_"):
        print(func, getattr(covid.vaccination, func)())

for func in covid.deaths_and_recovered.__dir__():
    if func.startswith("get_"):
        print(func, getattr(covid.deaths_and_recovered, func)())
