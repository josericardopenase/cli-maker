from abc import ABC, abstractmethod
from os import path
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

    def validate(self, value, transform : Callable = float):
        if(transform):
            return (transform(value) < self.maxv)
        return (value < self.maxv)


@dataclass
class IsDirectory(Validator):
    def __post_init__(self):
        self.error_message=f"Value is not a directory"

    def validate(self, value):
        return path.isdir(value)

@dataclass
class IsFile(Validator):
    def __post_init__(self):
        self.error_message=f"Value is not a file"

    def validate(self, value):
        return path.isfile(value)
@dataclass
class Min(Validator):
    minv: float

    def __post_init__(self):
        self.error_message=f"Value is less than {self.minv}"

    def validate(self, value, transform : Callable = float):
        if(transform):
            return (transform(value) > self.minv)
        return (value > self.minv)

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
