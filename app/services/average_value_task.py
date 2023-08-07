"""Average value task"""

import csv
import codecs
import requests

from app.services import utils

from app.loggers.loggers import get_custom_logger


def get_data_from_google_drive(
    file_id: str = "13nk_FYpcayUck2Ctrela5Tjt9JQbjznt",
) -> csv.DictReader | None:
    """Get csv data from Google Drive file

    Parameters
    ----------
    file_id : str
        Id of the Google Drive file

    Returns
    -------
    csv.DictReader | None
        CSV dictionary reader
    """
    logger = get_custom_logger("average_value")
    url = "https://drive.google.com/uc"

    try:
        response = requests.get(
            url,
            params={
                "export": "download",
                "id": file_id,
            },
            timeout=30,
        )
        if response.status_code == 200:
            lines_iterator = response.iter_lines()
            return csv.DictReader(
                codecs.iterdecode(lines_iterator, encoding="utf-8"), delimiter=","
            )

        logger.warning(
            f"Failed to get people data. Error: status code {response.status_code}"
        )
    except requests.exceptions.RequestException as ex:
        logger.error(str(ex))

    return None


def calculate_avg_value_from_people_csv_data(
    data: csv.DictReader,
) -> tuple[float, float]:
    """Calculates the average height and weight from CSV data.

    Parameters
    ----------
    data : csv.DictReader
        A CSV dictionary reader containing data with 'Height(Inches)' and 'Weight(Pounds)' columns.

    Returns
    -------
    tuple[float, float]
        A tuple containing the average height and average weight as floats.
        If the data is empty (None), the function returns (0.0, 0.0).
    """
    sum_height = 0.0
    sum_weight = 0.0

    if data is None:
        return sum_height, sum_weight

    index = None
    for index, row in enumerate(data, start=1):
        sum_height += float(row["Height(Inches)"])
        sum_weight += float(row["Weight(Pounds)"])

    if (index is not None) and (index > 0):
        return sum_height / index, sum_weight / index

    return sum_height, sum_weight


def output_avg_height_weight(height: float, weight: float) -> None:
    """Prints the average height and weight of people.

    Parameters
    ----------
    height : float
        Average height value in inches.
    weight : float
        Average weight value in pounds.

    Returns
    -------
    None
        This function does not return anything.
    """
    print("==============Average height and weight of people===============")
    print(f"Average value of people height: {round(utils.inches_to_cm(height), 2)} cm")
    print(f"Average value of people weight: {round(utils.pounds_to_kg(weight), 3)} kg")
    print("================================================================")


def average_value_task() -> None:
    """Average value task entry point"""
    logger = get_custom_logger("average_value")

    logger.debug("Average value task started")

    height, weight = calculate_avg_value_from_people_csv_data(
        get_data_from_google_drive()
    )
    output_avg_height_weight(height, weight)

    logger.debug("Average value task finished")
