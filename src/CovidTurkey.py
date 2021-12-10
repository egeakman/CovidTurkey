import requests
from bs4 import BeautifulSoup

class covidTurkey():
    def __init__(self):
        self.doseDatas = {"firstDoseDatas" : {"count" : 0, "percent" : 0},
        "secondDoseDatas" : {"count" : 0, "percent" : 0},
        "thirdDoseDatas" : {"count" : 0, "percent" : 0},
        "fourthDoseDatas" : {"count" : 0, "percent" : 0},
        "totalDoseCount" : 0,
        "dailyDoseCount" : 0}
    
    def request(self, url, source="number"):
        response = requests.get(url)
        source_content = response.content.decode("utf-8")
        if(source == "html"):
            source_content = self.parse_html(source_content)
        elif(source == "js"):
            source_content = self.parse_js(source_content)
        return source_content
            

    def parse_html(self, html_source):
        soup = BeautifulSoup(html_source,"html.parser")
        return soup.find_all()

    def updateVaccinationDatas(self):
        data = self.request("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=FERNZ2C4JZDC8HV9", "js")
        for line in data:      
            match line:
                case _ if line.startswith("var doz1asisayisi"):
                    firstDoseCount = line.split("=")[1].replace(";", "").replace("'", "")[1:]

                case _ if line.startswith("var doz2asisayisi"):
                    secondDoseCount = line.split("=")[1].replace(";", "").replace("'", "")[1:]

                case _ if line.startswith("var doz3asisayisi"):
                    thirdDoseCount = line.split("=")[1].replace(";", "").replace("'", "")[1:]

                case _ if line.startswith("var doz4asisayisi"):
                    fourthDoseCount = line.split("=")[1].replace(";", "").replace("'", "")[1:]

                case _ if line.startswith("var toplamasidozusayisi"):
                    totalDoseCount = line.split("=")[1].replace(";", "").replace("'", "")[1:]

                case _ if line.startswith("var gunluksidozusayisi"):
                    dailyDoseCount = line.split("=")[1].replace(";", "").replace("'", "")[1:]

                case _ if line.startswith("var dozturkiyeortalamasi"):
                    firstDosePercent = line.split("=")[1].replace(";", "").replace("'", "")[1:]

                case _ if line.startswith("var doz2turkiyeortalamasi"):
                    secondDosePercent = line.split("=")[1].replace(";", "").replace("'", "")[1:]

                case _ if line.startswith("var doz3turkiyeortalamasi"):
                    thirdDosePercent = line.split("=")[1].replace(";", "").replace("'", "")[1:]

                case _ if line.startswith("var doz4turkiyeortalamasi"):
                    fourthDosePercent = line.split("=")[1].replace(";", "").replace("'", "")[1:]

                # case _ if line.startswith("var asidozuguncellemesaati"):
                #     line.split("=")[1].replace(";", "").replace("'", "")


            
        self.doseDatas = {"firstDoseDatas" : {"count" : firstDoseCount, "percent" : firstDosePercent},
        "secondDoseDatas" : {"count" : secondDoseCount, "percent" : secondDosePercent},
        "thirdDoseDatas" : {"count" : thirdDoseCount, "percent" : thirdDosePercent},
        "fourthDoseDatas" : {"count" : fourthDoseCount, "percent" : fourthDosePercent},
        "totalDoseCount" : totalDoseCount,
        "dailyDoseCount" : dailyDoseCount}
        
        

    def parse_js(self, js_source):
        js_parsed = js_source.split("\n")
        return js_parsed


    def getDailyCase(self):
        data = self.request("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=5T7CBZG02TEYNMS1")
        return data

    def getAverageCasesPerDay(self):
        data = self.request("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=ABOIJZXZDK7FTWVC","html")
        return data[0].text

    def getFirstDoseCount(self):
        self.updateVaccinationDatas()
        return self.doseDatas["firstDoseDatas"]["count"]
    
    def getFirstDosePercent(self):
        self.updateVaccinationDatas()
        return self.doseDatas["firstDoseDatas"]["percent"]

    def getSecondDoseCount(self):
        self.updateVaccinationDatas()
        return self.doseDatas["secondDoseDatas"]["count"]
    
    def getSecondDosePercent(self):
        self.updateVaccinationDatas()
        return self.doseDatas["secondDoseDatas"]["percent"]

    def getThirdDoseCount(self):
        self.updateVaccinationDatas()
        return self.doseDatas["thirdDoseDatas"]["count"]
    
    def getThirdDosePercent(self):
        self.updateVaccinationDatas()
        return self.doseDatas["thirdDoseDatas"]["percent"]

    def getFourthDoseCount(self):
        self.updateVaccinationDatas()
        return self.doseDatas["fourthDoseDatas"]["count"]
    
    def getFourthDosePercent(self):
        self.updateVaccinationDatas()
        return self.doseDatas["fourthDoseDatas"]["percent"]
    
    def getTotalDoseCount(self):
        self.updateVaccinationDatas()
        return self.doseDatas["totalDoseCount"]

    def getDailyDoseCount(self):
        self.updateVaccinationDatas()
        return self.doseDatas["dailyDoseCount"]
