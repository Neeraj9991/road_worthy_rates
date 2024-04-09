from pydantic import BaseModel


class Car(BaseModel):
    company: str
    year: int
    owner: str
    fuel: str
    km_driven: str
    mileage_mpg: float
    engine_cc: float
    seats: float
