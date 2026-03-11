from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod
class DataStream(ABC):
    def __init__(self) -> None:
        self.data = []
    
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    
    @abstractmethod