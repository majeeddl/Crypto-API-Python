

from enum import Enum

class UserTypeEnum(Enum):
    def __str__(self):
        return str(self.name)

    root=1
    admin=2
    user=3     