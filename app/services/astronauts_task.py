"""Astronauts mini task"""

import json
import requests

from app.loggers.loggers import get_custom_logger


def show_astronauts(data: dict):
    """
    Show the astronauts data

    Parameters
    ----------
    data : dict
        Data from the astros json file

    Returns
    -------
    None
    """
    print("========================Astronauts task=========================")
    print(f"Number of astronauts in space: { data['number'] }")
    print("================================================================")

    # Print space stations astronauts
    show_astronauts_in_spacestations(get_station_astronauts(data["people"]))


def show_astronauts_in_spacestations(stations: dict) -> None:
    """
    Print the astronauts by space stations

    Parameters
    ----------
    stations : dict
        The dictionary containing space stations with austronauts

    Returns
    -------
    None
    """
    for name in stations:
        print("=============================================================")
        print(f"Astronauts who are on the {name} space station:")
        print(*stations[name], sep="\n")


def get_station_astronauts(astronauts_list: list) -> dict:
    """
    Sort astronauts by space stations

    Parameters
    ----------
    astronauts_list: list
        list astronauts

    Returns
    -------
    spacestation_list : dict
        The space stations list
    """
    spacestation_list = {}
    for astronauts in astronauts_list:
        craft = astronauts["craft"]
        name = astronauts["name"]
        if craft in spacestation_list:
            spacestation_list[craft].append(name)
        else:
            spacestation_list[craft] = [name]

    return spacestation_list


def get_astronauts() -> dict | None:
    """
    Get the astronauts data

    Returns
    -------
    Dictionary of astronauts | None
    """
    logger = get_custom_logger("astronauts")
    url = "http://api.open-notify.org/astros.json"

    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return json.loads(response.content)

        logger.warning(
            f"Failed to get astronauts. Error: status code {response.status_code}"
        )
    except requests.exceptions.RequestException as ex:
        logger.error(str(ex))

    return None


def astronauts_task():
    """Astronauts task endpoint"""
    logger = get_custom_logger("astronauts")
    logger.debug("Astronauts task started")

    astronauts = get_astronauts()
    if astronauts:
        show_astronauts(astronauts)

    logger.debug("Astronauts task finished")
