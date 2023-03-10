from dataclasses import dataclass, field
from typing import Optional
from abc import ABC
import math
from typing import List 
from ui.colors import tint_text, Tint
from validators import Max, Min, MaxStr, MinStr, Regexp, Validator, IsFile, IsDirectory

@dataclass
class BaseField(ABC):
    name : str = ""
    description : str = ""
    validators : Optional[List[Validator]] = field(default_factory=list)

    def is_valid(self, value, throw_exception=True):
        valid = True
        for x in self.validators:
            if not x.validate(value):
                print(tint_text(f'{self.name} : {x.error_message}', Tint.FAIL))
                valid = False
        return valid

    def __str__(self):
        return self.__class__.__name__

@dataclass
class StringField(BaseField):
    maxl : int = math.inf
    minl : int = -math.inf
    regexp : Optional[str] = ""
    
    def __post_init__(self):
        self.validators = [MaxStr(self.maxl), MinStr(self.minl), Regexp(self.regexp)]

@dataclass
class EmailField(StringField):
    def __post_init__(self):
        self.validators = [Regexp('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')]

@dataclass
class DirectoryField(BaseField):
    def __post_init__(self):
        self.validators = [IsDirectory()]

@dataclass
class FileField(BaseField):
    def __post_init__(self):
        self.validators = [IsFile()]


@dataclass
class NumberField(BaseField):
    maxn : int = math.inf
    minn: int = -math.inf

    def __post_init__(self):
        self.validators = [Max(self.maxn), Min(self.minn)]
