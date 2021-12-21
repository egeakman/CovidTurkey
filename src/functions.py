# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from cachetools import cached, TTLCache


VALID_VAX_ARGS = {
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


def remove_dots_and_commas(string, index):
    if not isinstance(string, str):
        if isinstance(string, list):
            string = string[index].text
        string = str(string)
    return string.replace(".", "").replace(",", "")


def parse_js(js_source):
    return js_source.split("\n")


def parse_html(html_source):
    try:
        soup = BeautifulSoup(html_source, "lxml")
    except Exception:
        raise ImportError('Could not import lxml\nInstall with "pip install lxml"')
    return soup.find_all()


def request(url, source="number", formatted=False, index_for_list=0):
    response = requests.get(url)
    source_content = response.content.decode("utf-8")
    if source == "html":
        source_content = parse_html(source_content)
    elif source == "js":
        source_content = parse_js(source_content)
    if formatted:
        return remove_dots_and_commas(source_content, index_for_list)
    return source_content


@cached(cache=TTLCache(maxsize=1024, ttl=6000))
def update_vaccination_data(data_arg, formatted=False, index_for_list=0):
    data = None
    latest = request(
        "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=FERNZ2C4JZDC8HV9",
        "js",
    )
    if data_arg not in VALID_VAX_ARGS:
        raise ValueError("Invalid argument")
    for line in latest:
        if line.startswith(f"var {data_arg}"):
            data = line.split("=")[1].replace(";", "").replace("'", "")[1:]
    if formatted:
        return remove_dots_and_commas(data, index_for_list)
    return data
