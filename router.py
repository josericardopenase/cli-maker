from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from commands import Command

@dataclass
class Router:
    routes : List[Route]

    def __iter__(self):
        return self.routes.__iter__()

@dataclass
class Route:
    path : str 
    children : Optional[List[Route]] = None
    command : Optional[Command] = None

    def __iter__(self):
        return self.children.__iter__()
    
    @property
    def is_leave(self):
        if self.children:
            return False
        return True
