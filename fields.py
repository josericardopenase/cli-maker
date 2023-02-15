from dataclasses import dataclass
from typing import Optional
from abc import ABC

@dataclass
class BaseField(ABC):
    name : str
    error_message : str

    def is_valid(self, value, throw_exception=True):
        pass

@dataclass
class StringField(BaseField):
    max_length : int
    regexp : Optional[str] = ""

    def is_valid(self, value, throw_exception=True):
        if(len(value) > self.max_length):
            print(self.error_message)
            return False
        return True

