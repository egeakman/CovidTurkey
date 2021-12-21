from datetime import date
from src import functions


class covid_turkey:
    class vaccination:
        def get_first_dose_count(self, formatted = False):
            if formatted:
                return functions.remove_dots_and_commas(functions.update_vaccination_data(data_arg="doz1asisayisi"))
            return functions.update_vaccination_data(data_arg="doz1asisayisi")

        def get_first_dose_percent(self):
            return functions.update_vaccination_data(data_arg="dozturkiyeortalamasi")

        def get_second_dose_count(self, formatted = False):
            if formatted:
                return functions.remove_dots_and_commas(functions.update_vaccination_data(data_arg="doz2asisayisi"))
            return functions.update_vaccination_data(data_arg="doz2asisayisi")

        def get_second_dose_percent(self):
            return functions.update_vaccination_data(data_arg="doz2turkiyeortalamasi")

        def get_third_dose_count(self, formatted = False):
            if formatted:
                return functions.remove_dots_and_commas(functions.update_vaccination_data(data_arg="doz3asisayisi"))
            return functions.update_vaccination_data(data_arg="doz3asisayisi")

        def get_third_dose_percent(self):
            return functions.update_vaccination_data(data_arg="doz3turkiyeortalamasi")

        def get_fourth_dose_count(self, formatted = False):
            if formatted:
                return functions.remove_dots_and_commas(functions.update_vaccination_data(data_arg="doz4asisayisi"))
            return functions.update_vaccination_data(data_arg="doz4asisayisi")

        def get_fourth_dose_percent(self):
            return functions.update_vaccination_data(data_arg="doz4turkiyeortalamasi")

        def get_total_dose_count(self, formatted = False):
            if formatted:
                return functions.remove_dots_and_commas(functions.update_vaccination_data(data_arg="toplamasidozusayisi"))
            return functions.update_vaccination_data(data_arg="toplamasidozusayisi")

        def get_daily_dose_count(self, formatted = False):
            if formatted:
                return functions.remove_dots_and_commas(functions.update_vaccination_data(data_arg="gunluksidozusayisi"))
            return functions.update_vaccination_data(data_arg="gunluksidozusayisi")

        def get_last_update(self):
            return functions.update_vaccination_data(data_arg="asidozuguncellemesaati")

    class cases:
        def get_daily_case(self, formatted = False):
            if(formatted):
                return functions.remove_dots_and_commas(functions.request(
                    "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=5T7CBZG02TEYNMS1"
                ))
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=5T7CBZG02TEYNMS1"
            )

        def get_average_cases_per_day(self, formatted = False):
            data = functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=ABOIJZXZDK7FTWVC",
                "html",
            )
            if formatted:
                return functions.remove_dots_and_commas(data[0].text)
            return data[0].text

    class deaths_and_recovered:
        def get_daily_death(self, formatted = False):
            if formatted:
                return functions.remove_dots_and_commas(functions.request(
                    "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=JN6N1R2OSFU5LGO7"
                ))
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=JN6N1R2OSFU5LGO7"
            )

        def get_total_death(self, formatted = False):
            if formatted:
                return functions.remove_dots_and_commas(functions.request(
                    "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=VJR862TXLHUT52JE"
                ))
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=VJR862TXLHUT52JE"
            )
         
        def get_average_deaths_per_day(self):
            today = date.today()
            corona_started = date(2020, 3, 11)
            delta = today - corona_started
            total_deaths = covid_turkey.deaths_and_recovered.get_total_death(self)
            total_deaths = total_deaths.replace(",", "")
            if total_deaths.isdigit():
                total_deaths = int(total_deaths)
                return round(total_deaths / delta.days)
            return None

        def get_daily_recovered(self, formatted = False):
            if formatted:
                return functions.remove_dots_and_commas(functions.request(
                    "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=R2550VKLU915XLZ6"
                ))
            return functions.request(
                "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=R2550VKLU915XLZ6"
            )
