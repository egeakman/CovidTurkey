from datetime import date
from src import functions


class covid_turkey:
    class vaccination:
        def get_first_dose_count(self):
            return functions.update_vaccination_data(data_arg="doz1asisayisi")

        def get_first_dose_percent(self):
            return functions.update_vaccination_data(data_arg="dozturkiyeortalamasi")

        def get_second_dose_count(self):
            return functions.update_vaccination_data(data_arg="doz2asisayisi")

        def get_second_dose_percent(self):
            return functions.update_vaccination_data(data_arg="doz2turkiyeortalamasi")

        def get_third_dose_count(self):
            return functions.update_vaccination_data(data_arg="doz3asisayisi")

        def get_third_dose_percent(self):
            return functions.update_vaccination_data(data_arg="doz3turkiyeortalamasi")

        def get_fourth_dose_count(self):
            return functions.update_vaccination_data(data_arg="doz4asisayisi")

        def get_fourth_dose_percent(self):
            return functions.update_vaccination_data(data_arg="doz4turkiyeortalamasi")

        def get_total_dose_count(self):
            return functions.update_vaccination_data(data_arg="toplamasidozusayisi")

        def get_daily_dose_count(self):
            return functions.update_vaccination_data(data_arg="gunluksidozusayisi")

        def get_last_update(self):
            return functions.update_vaccination_data(data_arg="asidozuguncellemesaati")

    class cases:
        def get_daily_case(self):
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=5T7CBZG02TEYNMS1"
            )

        def get_average_cases_per_day(self):
            data = functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=ABOIJZXZDK7FTWVC",
                "html",
            )
            return data[0].text

    class deaths_and_recovered:
        def get_average_deaths_per_day(self):
            total_deaths = functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=VJR862TXLHUT52JE"
            )
            total_deaths = total_deaths.replace(",", "")
            today = date.today()
            corona_started = date(2020, 3, 11)
            delta = today - corona_started
            return round(int(total_deaths) / int(delta.days))

        def get_daily_death(self):
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=JN6N1R2OSFU5LGO7"
            )

        def get_total_death(self):
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=VJR862TXLHUT52JE"
            )

        def get_daily_recovered(self):
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=R2550VKLU915XLZ6"
            )
