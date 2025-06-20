import datetime
from datetime import timezone

from typing import Final

BASE_DIR: Final = "data"

META_DIR: Final = "metadata"

DATE_FORMAT: Final = "%Y-%m-%d %H:%M:%S"

UTC_NOW: Final = datetime.datetime.now(timezone.utc)

OBJ_LIST: Final = ["Journal", "Publisher"]