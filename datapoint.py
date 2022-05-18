from dataclasses import dataclass


@dataclass
class Datapoint:
    flowerAssoc: str;
    slPosition: float;
    swPosition: float;
    plPosition: float;
    pwPosition: float;
    