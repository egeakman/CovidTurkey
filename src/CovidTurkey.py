from bs4 import BeautifulSoup
import requests


url = "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=FERNZ2C4JZDC8HV9"

page = requests.get(url).text

parsed = BeautifulSoup(page, features="lxml")

js = parsed.find_all()[0].text

js_parsed = js.split("\n")

for line in js_parsed:
    
    match line:
        case _ if line.startswith("var doz1asisayisi"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))

        case _ if line.startswith("var doz2asisayisi"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))

        case _ if line.startswith("var doz3asisayisi"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))

        case _ if line.startswith("var doz4asisayisi"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))

        case _ if line.startswith("var toplamasidozusayisi"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))

        case _ if line.startswith("var gunluksidozusayisi"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))

        case _ if line.startswith("var dozturkiyeortalamasi"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))

        case _ if line.startswith("var doz2turkiyeortalamasi"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))

        case _ if line.startswith("var doz3turkiyeortalamasi"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))

        case _ if line.startswith("var doz4turkiyeortalamasi"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))

        case _ if line.startswith("var asidozuguncellemesaati"):
            print(line.split("=")[1].replace(";", "").replace("'", ""))
