from typing import Any, List, Tuple, Dict
from abc import ABC, abstractmethod


class DataStream():
    def __init__(self) -> None:
        self.processor: List[DataProcessor] = []

    def register_processor(self, proc: "DataProcessor") -> None:
        self.processor.append(proc)

    '''Return the processor of the given type found in self.processor'''
    def _get_processor(self, proc_type: type) -> "DataProcessor | None":
        for proc in self.processor:
            if isinstance(proc, proc_type):
                return proc
        return None

    def process_stream(self, stream: list[Any]) -> None:
        if not isinstance(stream, list) or not self.processor:
            return
        processors = [
            (
                TextProcessor,
                lambda x: isinstance(x, str) or (
                    isinstance(x, list) and all(isinstance(i, str) for i in x)
                ),
            ),
            (
                NumericProcessor,
                lambda x: isinstance(x, (int, float)) or (
                    isinstance(x, list)
                    and all(isinstance(i, (int, float)) for i in x)
                ),
            ),
            (
                LogProcessor,
                lambda x: isinstance(x, Dict) or (
                    isinstance(x, list) and all(isinstance(i, Dict) for i in x)
                ),
            ),
        ]
        for item in stream:
            try:
                for processor, check in processors:
                    if check(item):
                        proc = self._get_processor(processor)
                        if proc is None or proc.validate(item) is False:
                            raise Exception(
                                f"Can't process element in stream: {item}"
                            )
                        if (
                            processor in [NumericProcessor, LogProcessor]
                            and not isinstance(item, list)
                        ):
                            proc.ingest([item])
                        else:
                            proc.ingest(item)
                        break
                else:
                    raise Exception(
                        f"Can't process element in stream: {item}"
                    )
            except Exception as e:
                print(f"DataStream error - {e}")

    def print_processors_stat(self) -> None:
        print("== DataStream statistics ==")
        if not self.processor:
            print("No processors found, no data\n")
            return
        for proc in self.processor:
            print(
                f"{proc.__class__.__name__}: Total {proc.total_processed} "
                f"items processed, remaining {len(proc.data)} on processor"
                )


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: List[Tuple[int, str]] = []
        self._rank: int = 0
        self.total_processed: int = 0

    def output(self) -> Tuple[int, str]:
        if not self.data:
            raise Exception("No processed data available")
        return self.data.pop(0)

    def _store_result(self, result: str) -> None:
        self._rank += 1
        self.data.append((self._rank, result))
        self.total_processed += 1

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
        if not isinstance(data, list):
            raise Exception("Improper numeric data")
        for i in range(len(data)):
            num = data[i]
            if not isinstance(num, (int, float)):
                raise Exception("Data must be a list of numbers")
            self._store_result(f"Numeric value {i}: {num}")

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
        list_flag: int = 0
        if isinstance(data, str):
            pass
        elif (
            isinstance(data, list)
            and all(isinstance(item, str) for item in data)
        ):
            list_flag += 1
        else:
            raise Exception("Data must be a string or a list of strings")
        if list_flag == 0:
            data = [data]
        for i in range(len(data)):
            if isinstance(data, str):
                text = data
            else:
                text = data[i]
            self._store_result(f"Text value {i}: {text}")

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def ingest(self, data: Any) -> None:
        index: int = 0
        if isinstance(data, Dict):
            pass
        elif (
            isinstance(data, list)
            and all(isinstance(item, Dict) for item in data)
        ):
            pass
        else:
            raise Exception("Data must be a dict or a list of dicts")
        for item in data:
            level = item.get("log_level")
            message = item.get("log_message")
            result = f"Log entry {index}: {level}: {message}"
            index += 1
            self._store_result(result)

    def validate(self, data: Any) -> bool:
        if isinstance(data, Dict):
            return True
        elif isinstance(data, list):
            return all(isinstance(item, Dict) for item in data)
        return False


def main() -> None:
    ds = DataStream()
    data_batch: list = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    ds.print_processors_stat()
    print("Registering Numeric Processor\n")
    ds.register_processor(NumericProcessor())
    print(f"Send first batch of data on stream: {data_batch}")
    ds.process_stream(data_batch)
    ds.print_processors_stat()

    print("\nRegistering other data processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())
    print("Send the same batch again")
    ds.process_stream(data_batch)
    ds.print_processors_stat()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
        )
    for _ in range(3):
        ds._get_processor(NumericProcessor).output()
    for _ in range(2):
        ds._get_processor(TextProcessor).output()
    for _ in range(1):
        ds._get_processor(LogProcessor).output()
    ds.print_processors_stat()


if __name__ == "__main__":
    main()
