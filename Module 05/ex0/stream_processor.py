from typing import Any
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
        length = len(data)
        total = 0
        for num in data:
            total += num
        avg = total/length
        result = f"Processed {length} numeric values, sum={total}, avg={avg}"
        return result
        
    def validate(self, data: Any) -> bool:
        try:
            for num in data:
                float(num)
        except:
            return False
        return True

class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        length = len(data)
        words = len(data.split())
        result = f"Processed text: {length} characters, {words} words"
        return result

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return True

class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        
    def process(self, data):
        level, message = data.split(":", 1)
        level = level.strip().upper()
        message = message.strip()
        if level not in ["ERROR", "INFO"]:
            raise Exception("Unsupported log level")
        if level == "ERROR":
            level = f"[ALERT] {level} level detected:"
        elif level == "INFO":
            level = f"[INFO] {level} level detected:"
        result = f"{level} {message}"
        return result
    
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if ":" not in data:
            return False
        return True

if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    data_type: list[str] = [
        "Numeric",
        "Text",
        "Log"
    ]
    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    data_samples = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout"
    ]
    index = 0
    for processor in processors:
        try:
            print(f"Initializing {data_type[index]} Processor...")
            data = data_samples[index]
            if data_type[index] == "Numeric":
                print(f"Processing data: {data}")
            else:
                print(f'Processing data: "{data}"')
            if processor.validate(data) is False:
                raise Exception("Invalid data")
            print(f"Validation: {data_type[index]} data verified")
            result_as_str = processor.process(data)
            print(f"{processor.format_output(result_as_str)}")
            index += 1
        except Exception as Error:
            print("Error:", Error)

    data_samples = [
        [1, 2, 3],
        "Hello Nexus ",
        "INFO: System ready"
    ]
    print("=== Polymorphic Processing Demo ===\n")
    index = 0
    for processor in processors:
        data = data_samples[index]
        if processor.validate(data):
            result_as_str = processor.process(data)
            print(f"Result: {index+1}: {result_as_str}")
        index += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")