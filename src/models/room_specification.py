"""Room and space specifications"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class RoomSpecification:
    """Represents room dimensions and specifications"""
    
    length_m: float
    width_m: float
    height_m: Optional[float] = None
    room_name: str = "Room"
    shape: str = "rectangular"  # rectangular, l-shaped, irregular, etc.
    additional_area_m2: float = 0.0  # For irregular shapes or additional areas
    
    def get_total_area(self) -> float:
        """Calculate total floor area"""
        base_area = self.length_m * self.width_m
        return base_area + self.additional_area_m2
    
    def get_perimeter(self) -> float:
        """Calculate perimeter for linear materials like baseboards"""
        return 2 * (self.length_m + self.width_m)
    
    def __str__(self) -> str:
        area = self.get_total_area()
        return f"{self.room_name}: {self.length_m}m x {self.width_m}m (Area: {area:.2f} m²)"
