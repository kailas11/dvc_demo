import pytest


class NotInRange(Exception):
    def __init__(self, message="Value not in Range"):

        self.message = message
        super().__init__(self.message)


def test_genric():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange
