from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Tuple
from enum import Enum
from dataclasses import dataclass

class Tint(Enum):
    def __str__(self):
        return str(self.value)

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def tint_text(text, color=Tint, bgcolor=Tint):
    return str(color) + text + str(Tint.ENDC)

class Convertions:
    @staticmethod
    def rgb_to_hex(rgb : RGB):
        return Hex('#%02x%02x%02x' % rgb.color)

    @staticmethod
    def hex_to_rgb(hex: Hex):
        value = str(hex).lstrip('#')
        lv = len(value)
        return RGB(tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))

class Color(ABC):
    @abstractmethod
    def tint_text(self, text):
        pass

@dataclass
class Hex(Color):
    color : str

    def tint_text(self, text):
        rgb = Convertions.hex_to_rgb(self.color)
        return rgb.tint_text(text)

    def __str__(self):
        return self.color

@dataclass
class RGB(Color):
    color: Tuple

    def tint_text(self, text):
        return '\033[38;2;{};{};{};m{}\033[0m'.format(self.color[0], self.color[1], self.color[2], text)

    def __str__(self):
        return "({}, {}, {})".format(self.color[0], self.color[1], self.color[2])
    
