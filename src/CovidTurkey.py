import requests
from bs4 import BeautifulSoup


class covid_turkey:
    def __init__(self):
        self.dose_data = {
            "first_dose_data": {"count": 0, "percent": 0},
            "second_dose_data": {"count": 0, "percent": 0},
            "third_dose_data": {"count": 0, "percent": 0},
            "fourth_dose_data": {"count": 0, "percent": 0},
            "total_dose_count": 0,
            "daily_dose_count": 0,
            "last_update": "",
        }

    def request(self, url, source="number"):
        response = requests.get(url)
        source_content = response.content.decode("utf-8")
        if source == "html":
            source_content = self.parse_html(source_content)
        elif source == "js":
            source_content = self.parse_js(source_content)
        return source_content

    def parse_html(self, html_source):
        soup = BeautifulSoup(html_source, "html.parser")
        return soup.find_all()

    def update_vaccination_data(self):
        data = self.request(
            "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=FERNZ2C4JZDC8HV9",
            "js",
        )
        for line in data:
            if line.startswith("var doz1asisayisi"):
                first_dose_count = (
                    line.split("=")[1].replace(";", "").replace("'", "")[1:]
                )

            if line.startswith("var doz2asisayisi"):
                second_dose_count = (
                    line.split("=")[1].replace(";", "").replace("'", "")[1:]
                )

            if line.startswith("var doz3asisayisi"):
                third_dose_count = (
                    line.split("=")[1].replace(";", "").replace("'", "")[1:]
                )

            if line.startswith("var doz4asisayisi"):
                fourth_dose_count = (
                    line.split("=")[1].replace(";", "").replace("'", "")[1:]
                )

            if line.startswith("var toplamasidozusayisi"):
                total_dose_count = (
                    line.split("=")[1].replace(";", "").replace("'", "")[1:]
                )

            if line.startswith("var gunluksidozusayisi"):
                daily_dose_count = (
                    line.split("=")[1].replace(";", "").replace("'", "")[1:]
                )

            if line.startswith("var dozturkiyeortalamasi"):
                first_dose_percent = (
                    line.split("=")[1].replace(";", "").replace("'", "")[1:]
                )

            if line.startswith("var doz2turkiyeortalamasi"):
                second_dose_percent = (
                    line.split("=")[1].replace(";", "").replace("'", "")[1:]
                )

            if line.startswith("var doz3turkiyeortalamasi"):
                third_dose_percent = (
                    line.split("=")[1].replace(";", "").replace("'", "")[1:]
                )

            if line.startswith("var doz4turkiyeortalamasi"):
                fourth_dose_percent = (
                    line.split("=")[1].replace(";", "").replace("'", "")[1:]
                )

            if line.startswith("var asidozuguncellemesaati"):
                last_update = line.split("=")[1].replace(";", "").replace("'", "")

        self.dose_data = {
            "first_dose_data": {
                "count": first_dose_count,
                "percent": first_dose_percent,
            },
            "second_dose_data": {
                "count": second_dose_count,
                "percent": second_dose_percent,
            },
            "third_dose_data": {
                "count": third_dose_count,
                "percent": third_dose_percent,
            },
            "fourth_dose_data": {
                "count": fourth_dose_count,
                "percent": fourth_dose_percent,
            },
            "total_dose_count": total_dose_count,
            "daily_dose_count": daily_dose_count,
            "lastUpdate": last_update,
        }

    def parse_js(self, js_source):
        return js_source.split("\n")

    def get_daily_case(self):
        return self.request(
            "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=5T7CBZG02TEYNMS1"
        )

    def get_average_case(self):
        data = self.request(
            "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=ABOIJZXZDK7FTWVC",
            "html",
        )
        return data[0].text

    def get_first_dose_count(self):
        self.update_vaccination_data()
        return self.dose_data["first_dose_data"]["count"]

    def get_first_dose_percent(self):
        self.update_vaccination_data()
        return self.dose_data["first_dose_data"]["percent"]

    def get_second_dose_count(self):
        self.update_vaccination_data()
        return self.dose_data["second_dose_data"]["count"]

    def get_second_dose_percent(self):
        self.update_vaccination_data()
        return self.dose_data["second_dose_data"]["percent"]

    def get_third_dose_count(self):
        self.update_vaccination_data()
        return self.dose_data["third_dose_data"]["count"]

    def get_third_dose_percent(self):
        self.update_vaccination_data()
        return self.dose_data["third_dose_data"]["percent"]

    def get_fourth_dose_count(self):
        self.update_vaccination_data()
        return self.dose_data["fourth_dose_data"]["count"]

    def get_fourth_dose_percent(self):
        self.update_vaccination_data()
        return self.dose_data["fourth_dose_data"]["percent"]

    def get_total_dose_count(self):
        self.update_vaccination_data()
        return self.dose_data["total_dose_count"]

    def get_daily_dose_count(self):
        self.update_vaccination_data()
        return self.dose_data["daily_dose_count"]

    def get_last_update(self):
        self.update_vaccination_data()
        return self.dose_data["last_update"]
