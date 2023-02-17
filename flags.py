from dataclasses import dataclass
from fields import BaseField
from typing import Optional

class Flag:
    flag : str
    field : BaseField
    short_flag : Optional[str]


