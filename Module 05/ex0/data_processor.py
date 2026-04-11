from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: List[tuple[int, str]] = []
        self._rank: int = 0

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise Exception("No processed data available")
        return self.data.pop(0)

    def _store_result(self, result: str) -> None:
        self._rank += 1
        self.data.append((self._rank, result))

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise Exception("Improper numeric data")
        if not isinstance(data, list):
            data = [data]
        print(f"Extracting {len(data)} values...")
        for i in range(len(data)):
            num = data[i]
            self._store_result(f"Numeric value {i}: {num}")
            print(self.output()[1])

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise Exception("Improper text data")
        if not isinstance(data, list):
            data = [data]
        print(f"Extracting {len(data)} values...")
        for i in range(len(data)):
            if isinstance(data, str):
                text = data
            else:
                text = data[i]
            self._store_result(f"Text value {i}: {text}")
            print(self.output()[1])

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def ingest(self, data: Any) -> None:
        index: int = 0
        if self.validate(data) is False:
            raise Exception("Improper log data")
        if not isinstance(data, list):
            data = [data]
        print(f"Extracting {len(data)} values...")
        for item in data:
            level = item.get("log_level")
            message = item.get("log_message")
            result = f"Log entry {index}: {level}: {message}"
            index += 1
            self._store_result(result)
            print(self.output()[1])

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, list):
            return all(isinstance(item, dict) for item in data)
        return False


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    data_samples: List[Any] = [
        [1, 2, 3, 4, 5],
        ["Hello", "Nexus", "World"],
        [{"log_level": "NOTICE", "log_message": "Connection to server"},
         {"log_level": "ERROR", "log_message": "Unauthorized access!"}]
    ]
    print("Testing Numeric Processor...")
    print(
        f"Trying to validate input '42': "
        f"{NumericProcessor().validate(42)}"
    )
    print(
        f"Trying to validate input 'Hello': "
        f"{NumericProcessor().validate('Hello')}"
    )
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        NumericProcessor().ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")
    print(f"Processing data: {data_samples[0]}")
    try:
        NumericProcessor().ingest(data_samples[0])
    except Exception as e:
        print(f"Error processing numeric data: {e}\n")

    print("\nTesting Text Processor...")
    print(
        f"Trying to validate input '42': "
        f"{TextProcessor().validate(42)}"
    )
    print(f"Processing data: {data_samples[1]}")
    try:
        TextProcessor().ingest(data_samples[1])
    except Exception as e:
        print(f"Error processing text data: {e}\n")
    print()

    print("Testing Log Processor...")
    print(
        f"Trying to validate input 'Hello': "
        f"{LogProcessor().validate('Hello')}"
    )
    print(f"Processing data: {data_samples[2]}")
    try:
        LogProcessor().ingest(data_samples[2])
    except Exception as e:
        print(f"Error processing log data: {e}\n")
    try:
        NumericProcessor().ingest(42)
    except Exception as e:
        print(f"Error processing numeric data 42: {e}\n")


if __name__ == "__main__":
    main()
