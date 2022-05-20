from dataclasses import dataclass


@dataclass
class DataPoint:
    
    slPosition: float; # sepal length
    swPosition: float; # sepal width
    plPosition: float; # petal length
    pwPosition: float; # petal width
    flowerActual: str; # actual type
    flowerAssoc: str = " ";  # centroid closest type