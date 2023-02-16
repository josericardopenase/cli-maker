from abc import ABC
from .colors import Tint, tint_text
from dataclasses import dataclass
from typing import Optional

def cli_write(text, **kwargs):
    print(text)

class UIElement(ABC):
    pass

class Loader(UIElement):
    pass

class ProgressBar(UIElement):
    pass

@dataclass
class Text(UIElement):
    text : str
    color : Optional[Tint]

    def show(self):
        cli_write(tint_text(self.text, color=self.color))

class Select(UIElement):
    pass

class Question(UIElement):
    pass


