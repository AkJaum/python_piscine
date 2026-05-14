from pydantic import BaseModel, Field, model_validator
from typing import List
from enum import Enum
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_id_validator(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        return self

    @model_validator(mode='after')
    def check_leadership(self) -> 'SpaceMission':
        if not any(member.rank in [Rank.CAPTAIN, Rank.COMMANDER] for member in self.crew):
            raise ValueError("Mission must have at least one Commander or Captain")
        return self

    @model_validator(mode='after')
    def long_mission_validator(self) -> 'SpaceMission':
        if self.duration_days > 365 and not any(member.years_experience > 5 for member in self.crew):
            raise ValueError("Long missions must have at least one crew member with more than 5 years of experience")
        return self

    @model_validator(mode='after')
    def crew_members_validator(self) -> 'SpaceMission':
        for member in self.crew:
            if not member.is_active:
                raise ValueError(f"Crew member {member.name} is not active")
        return self


def print_mission_details(mission: SpaceMission):
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions:.2f}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"  - {member.name} ({member.rank.value}) - {member.specialization}")


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=================================")
    try:
        crew_members = [
            CrewMember(member_id="C001", name="Alice", rank=Rank.CAPTAIN, age=35, specialization="Pilot", years_experience=10),
            CrewMember(member_id="C002", name="Bob", rank=Rank.OFFICER, age=30, specialization="Engineer", years_experience=5),
            CrewMember(member_id="C003", name="Charlie", rank=Rank.LIEUTENANT, age=28, specialization="Scientist", years_experience=3)
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2025, 7, 20),
            duration_days=900,
            crew=crew_members,
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print_mission_details(mission)
    except ValueError as e:
        for err in e.errors():
            print(err['loc'], err['msg'])
    print("\n=================================")
    print("Expected validation error:")
    try:
        crew_members = [
            CrewMember(member_id="C001", name="Alice", rank=Rank.CADET, age=35, specialization="Pilot", years_experience=10),
            CrewMember(member_id="C002", name="Bob", rank=Rank.OFFICER, age=30, specialization="Engineer", years_experience=5),
            CrewMember(member_id="C003", name="Charlie", rank=Rank.LIEUTENANT, age=28, specialization="Scientist", years_experience=3)
        ]
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2025, 7, 20),
            duration_days=900,
            crew=crew_members,
            budget_millions=2500.0
        )
    except ValueError as e:
        for err in e.errors():
            print(err['loc'], err['msg'])
