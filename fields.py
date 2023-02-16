from dataclasses import dataclass
from typing import Optional
from abc import ABC
import math

@dataclass
class BaseField(ABC):
    name : str = ""
    error_message : str = ""
    description : str = ""

    def is_valid(self, value, throw_exception=True):
        pass

    def __str__(self):
        return self.__class__.__name__

@dataclass
class StringField(BaseField):
    max_length : int = math.inf
    regexp : Optional[str] = ""

    def is_valid(self, value, throw_exception=True):
        if(len(value) > self.max_length):
            print(self.error_message)
            return False
        return True

@dataclass
class NumberField(BaseField):
    maxn : int = math.inf
    minn: int = -math.inf

    def is_valid(self, value, throw_exception=True):
        value = int(value)
        if(value > self.maxn):
            print("{} argument greater than max".format(self.name))
            return False
        if(value > self.maxn):
            print("{} argument less than min".format(self.name))
            return False
        return True
