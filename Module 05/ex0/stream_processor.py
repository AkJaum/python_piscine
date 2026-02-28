from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data = []
        
    def format_output(self, result: str) -> str:
        return f"Output: {result}\n"

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        lenght = len(data)
        sum = 0
        for num in data:
            sum += num
        avg = sum/lenght
        result = f"Processed {lenght} numeric values, sum={sum}, avg={avg}"
        return result
        
    def validate(self, data: Any) -> bool:
            total = 0
            count = 0
            for value in data:
                total += value
                count += 1
            if count == 0:
                return False
            return True

class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
    
    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        lenght = len(data)
        words = len(data.split())
        for char in data:
            if char == " " and (char + 1) is not " ":
                words += 1
        result = f"Processed test: {lenght} characters, {words} words"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    processor = NumericProcessor()
    try:
        num_data = [1, 2, 3, 4, 5]
        result_as_str = processor.process(num_data)
        if processor.validate(num_data)is False:
            raise Exception("Invalid numeric data")
        print(f"Validation: Numeric data verified")
        print(f"{processor.format_output(result_as_str)}\n")
    except Exception as Error:
        print("Error:", Error)
