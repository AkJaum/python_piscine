from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_id(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("ID Contact must start with 'AC'")
        return self

    @model_validator(mode='after')
    def validate_physical_contact(self) -> "AlienContact":
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact must be verified")
        return self

    @model_validator(mode='after')
    def validate_telepathic_contact(self) -> "AlienContact":
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        return self

    @model_validator(mode='after')
    def validate_strong_signal(self) -> "AlienContact":
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signal must have a message received")
        return self


def print_contact(contact: AlienContact) -> None:
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witness: {contact.witness_count}")
    if contact.message_received:
        print(f"Message Received: '{contact.message_received}'")
    else:
        print("Message: None")


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli.",
            is_verified=True
        )
        print_contact(contact)
    except ValidationError as e:
        for err in e.errors():
            print(err['loc'], err['msg'])
    print("\n======================================")
    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,  # Not enough witness
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print_contact(invalid_contact)
    except ValidationError as e:
        for err in e.errors():
            print(err['loc'], err['msg'])
