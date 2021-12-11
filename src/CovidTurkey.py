import requests
from bs4 import BeautifulSoup


class covid_turkey:
    def __init__(self):
        self.VALID_ARGS = {
            "doz1asisayisi",
            "doz2asisayisi",
            "doz3asisayisi",
            "doz4asisayisi",
            "toplamasidozusayisi",
            "gunluksidozusayisi",
            "dozturkiyeortalamasi",
            "doz2turkiyeortalamasi",
            "doz3turkiyeortalamasi",
            "doz4turkiyeortalamasi",
            "asidozuguncellemesaati",
        }

    def parse_js(self, js_source):
        return js_source.split("\n")

    def parse_html(self, html_source):
        soup = BeautifulSoup(html_source, "lxml")
        return soup.find_all()

    def request(self, url, source="number"):
        response = requests.get(url)
        source_content = response.content.decode("utf-8")
        if source == "html":
            source_content = self.parse_html(source_content)
        elif source == "js":
            source_content = self.parse_js(source_content)
        return source_content

    def update_vaccination_data(self, data_arg):
        latest = self.request(
            "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=FERNZ2C4JZDC8HV9",
            "js",
        )
        self.__init__()
        if data_arg not in self.VALID_ARGS:
            raise ValueError("Invalid argument")
        for line in latest:
            if line.startswith(f"var {data_arg}"):
                data = line.split("=")[1].replace(";", "").replace("'", "")[1:]

        return data

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
        return self.update_vaccination_data(data_arg="doz1asisayisi")

    def get_first_dose_percent(self):
        return self.update_vaccination_data(data_arg="dozturkiyeortalamasi")

    def get_second_dose_count(self):
        return self.update_vaccination_data(data_arg="doz2asisayisi")

    def get_second_dose_percent(self):
        return self.update_vaccination_data(data_arg="doz2turkiyeortalamasi")

    def get_third_dose_count(self):
        return self.update_vaccination_data(data_arg="doz3asisayisi")

    def get_third_dose_percent(self):
        return self.update_vaccination_data(data_arg="doz3turkiyeortalamasi")

    def get_fourth_dose_count(self):
        return self.update_vaccination_data(data_arg="doz4asisayisi")

    def get_fourth_dose_percent(self):
        return self.update_vaccination_data(data_arg="doz4turkiyeortalamasi")

    def get_total_dose_count(self):
        return self.update_vaccination_data(data_arg="toplamasidozusayisi")

    def get_daily_dose_count(self):
        return self.update_vaccination_data(data_arg="gunluksidozusayisi")

    def get_last_update(self):
        return self.update_vaccination_data(data_arg="asidozuguncellemesaati")
