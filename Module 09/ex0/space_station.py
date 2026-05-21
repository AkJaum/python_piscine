from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool
    notes: Optional[str] = Field(default=None, max_length=200)


def print_station_data(station: SpaceStation) -> None:
    print("Validation station created:")
    print("ID:", station.station_id)
    print("Name:", station.name)
    print("Crew:", station.crew_size, "people")
    print("Power:", station.power_level)
    print("Oxygen:", station.oxygen_level)
    print("Status:", station.is_operational)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="No issues reported."
        )
        print_station_data(station)
    except ValidationError as e:
        for err in e.errors():
            print(err['loc'], err['msg'])
    print("\n========================================")
    print("Expected validation error:")
    try:
        station = SpaceStation(
            station_id="ST",
            name="Test Station",
            crew_size=21,
            power_level=5.0,
            oxygen_level=10.0,
            last_maintenance=datetime.now(),
            is_operational=False
        )
        print_station_data(station)
    except ValidationError as e:
        for err in e.errors():
            print(err['loc'], err['msg'])


if __name__ == "__main__":
    main()
