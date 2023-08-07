"""User entity file"""

from typing import NamedTuple


class User(NamedTuple):
    """User entity"""

    username: str
    email: str

    def as_dict(self) -> dict:
        """
        Return dictionary with user objects properties

        Returns
        -------
        dict
            A dictionary containing 'username' and 'email' properties.
        """
        # pylint: disable=no-member
        return self._asdict()
