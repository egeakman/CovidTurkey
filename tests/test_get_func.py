import sys
from pathlib import Path

sys.path.append(str(Path("..").absolute().parent))
from src import CovidTurkey


vaccination = CovidTurkey.vaccination()
cases = CovidTurkey.cases()
deaths_and_recovered = CovidTurkey.deaths_and_recovered()

for func in vaccination.__dir__():
    if func.startswith("get_"):
        print(func, getattr(vaccination, func)())

for func in cases.__dir__():
    if func.startswith("get_"):
        print(func, getattr(cases, func)())

for func in deaths_and_recovered.__dir__():
    if func.startswith("get_"):
        print(func, getattr(deaths_and_recovered, func)())
