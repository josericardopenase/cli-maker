from abc import ABC, abstractmethod
from dataclasses import dataclass
import re
from typing import Callable

class Validator(ABC):
    error_message: str = ""

    @abstractmethod
    def validate(self, value):
        pass

@dataclass
class Max(Validator):
    maxv : float

    def __post_init__(self):
        self.error_message=f"Value is greater than {self.maxv}"

    def validate(self, value, transform : Callable = None):
        if(transform):
            return (transform(value) < self.maxv)
        return (value < self.maxv)

@dataclass
class Min(Validator):
    minv: float

    def __post_init__(self):
        self.error_message=f"Value is less than {self.minv}"

    def validate(self, value, transform : Callable = None):
        if(transform):
            return (transform(value) < self.minv)
        return (value < self.minv)

class MaxStr(Max):
    def __post_init__(self):
        self.error_message=f"String length is greater than {self.maxv}"

    def validate(self, value):
        return super().validate(value, len)


class MinStr(Min):
    def __post_init__(self):
        self.error_message=f"String length is less than {self.minv}"

    def validate(self, value):
        return super().validate(value, len)


@dataclass
class Regexp(Validator):
    regexp: str

    def __post_init__(self):
        self.error_message=f"Value does not match {self.regexp}"

    def validate(self, value):
        return re.match(self.regexp, value)
