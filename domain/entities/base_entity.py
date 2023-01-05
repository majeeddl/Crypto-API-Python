
from datetime import datetime


class BaseEntity:

    _id: str
    createdAt: datetime
    updatedAt: datetime

    def __init__(self) -> None:
        self.updatedAt: datetime = datetime.now()
        pass
        # self._id = _id
