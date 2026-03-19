from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed = 0
        self.data = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed": self.processed
        }


class SensorProcessor(DataStream):
    def __init__(self) -> None:
        super().__init__("sensor_stream")

    def process_batch(self, data_batch):
        i = 0
        temp_total = "N/a"
        if not isinstance(data_batch, dict):
            raise ValueError("Invalid data format")
        for key, value in data_batch.items():
            if "temp" in key:
                temp_total = sum(value)
            i += 1
        return (
            f"Processed sensor batch: {data_batch}\nSensor analysis: {i} "
            f"readings processed, avg temp:{temp_total/i}" if i > 0 else
            f"Processed sensor batch: {data_batch}\nSensor analysis: {i} "
            f"readings processed, avg temp:N/a"
        )


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    sensor_stream = SensorProcessor()
    print(f"StreamID: {sensor_stream.stream_id} Type: Environmental Data")
