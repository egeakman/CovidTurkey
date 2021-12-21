from datetime import date
from src import functions


class covid_turkey:
    class vaccination:
        def get_first_dose_count(self, formatted=False):
            return functions.update_vaccination_data(
                data_arg="doz1asisayisi", formatted=formatted
            )

        def get_first_dose_percent(self):
            return functions.update_vaccination_data(data_arg="dozturkiyeortalamasi")

        def get_second_dose_count(self, formatted=False):
            return functions.update_vaccination_data(
                data_arg="doz2asisayisi", formatted=formatted
            )

        def get_second_dose_percent(self):
            return functions.update_vaccination_data(data_arg="doz2turkiyeortalamasi")

        def get_third_dose_count(self, formatted=False):
            return functions.update_vaccination_data(
                data_arg="doz3asisayisi", formatted=formatted
            )

        def get_third_dose_percent(self):
            return functions.update_vaccination_data(data_arg="doz3turkiyeortalamasi")

        def get_fourth_dose_count(self, formatted=False):
            return functions.update_vaccination_data(
                data_arg="doz4asisayisi", formatted=formatted
            )

        def get_fourth_dose_percent(self):
            return functions.update_vaccination_data(data_arg="doz4turkiyeortalamasi")

        def get_total_dose_count(self, formatted=False):
            return functions.update_vaccination_data(
                data_arg="toplamasidozusayisi", formatted=formatted
            )

        def get_daily_dose_count(self, formatted=False):
            return functions.update_vaccination_data(
                data_arg="gunluksidozusayisi", formatted=formatted
            )

        def get_last_update(self):
            return functions.update_vaccination_data(data_arg="asidozuguncellemesaati")

    class cases:
        def get_daily_case(self, formatted=False):
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=5T7CBZG02TEYNMS1",
                formatted=formatted,
            )

        def get_average_cases_per_day(self, formatted=False):
            data = functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=ABOIJZXZDK7FTWVC",
                "html",
                formatted=formatted,
                index_for_list=0,
            )
            if formatted:
                return data
            return data[0].text

    class deaths_and_recovered:
        def get_daily_death(self, formatted=False):
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=JN6N1R2OSFU5LGO7",
                formatted=formatted,
            )

        def get_total_death(self, formatted=False):
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=VJR862TXLHUT52JE",
                formatted=formatted,
            )

        def get_average_deaths_per_day(self):
            today = date.today()
            corona_started = date(2020, 3, 11)
            delta = today - corona_started
            total_deaths = covid_turkey.deaths_and_recovered.get_total_death(
                self, formatted=True
            )
            if total_deaths.isdigit():
                total_deaths = int(total_deaths)
                return round(total_deaths / delta.days)
            return None

        def get_daily_recovered(self, formatted=False):
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=R2550VKLU915XLZ6",
                formatted=formatted,
            )
