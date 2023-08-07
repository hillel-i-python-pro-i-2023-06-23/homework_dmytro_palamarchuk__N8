"""Generate user tasks"""

import csv

from collections.abc import Iterator
from pathlib import PosixPath

from app.loggers.loggers import get_custom_logger
from app.services.faker_instance import faker
from app.config import FILES_OUTPUT_DIR
from app.entity.user import User


def generate_user() -> User:
    """Generate user

    Returns
    -------
    user : user
        The User instance
    """
    return User(
        username=faker.first_name(),
        email=faker.email(),
    )


def generate_users(count: int = 100) -> Iterator[User]:
    """Generate users

    Parameters
    ----------
    count : int
        The number of user will be generated

    Returns
    -------
    Iterator[User]
        Generated User instances
    """
    for _ in range(1, count + 1):
        yield generate_user()


def save_user_to_csv(file_path: PosixPath, data: Iterator[User]) -> None:
    """Save data to CSV.

    Parameters
    ----------
    file_path : PosixPath
        Path to CSV.
    data :Iterator[user]
        List of User entities.
    """
    with open(file_path, "w", newline="", encoding="UTF-8") as csv_file:
        try:
            first_item = next(data)
        except StopIteration:
            return

        fieldnames = first_item.as_dict().keys()
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerow(first_item.as_dict())

        for user in data:
            csv_writer.writerow(user.as_dict())


def generate_users_task(user_count: int = 100) -> None:
    """
    Generates a list of users task

    Parameters
    ----------
    user_count : int
        The count of user will be generated
    """
    logger = get_custom_logger("generate_users")

    logger.debug("Generate users task started")

    file_path = FILES_OUTPUT_DIR.joinpath("user_list.csv")
    save_user_to_csv(file_path, generate_users(user_count))

    print("=====================Generate users task========================")
    logger.info("Result of generate_users you can see in files_output folder")
    print("================================================================")

    logger.debug("Generate users task finished")
