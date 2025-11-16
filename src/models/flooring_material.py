"""Flooring material specifications and properties"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class FlooringMaterial:
    """Represents a flooring material with its properties"""
    
    name: str
    material_type: str  # e.g., 'tile', 'wood', 'laminate', 'stone'
    unit_cost: float  # Cost per unit (m2, piece, etc.)
    unit_measurement: str  # 'm2', 'piece', 'box'
    units_per_box: Optional[int] = None  # If applicable
    thickness_mm: Optional[float] = None
    width_cm: Optional[float] = None  # For tiles, boards, etc.
    length_cm: Optional[float] = None
    waste_factor: float = 0.10  # Default 10% waste allowance
    
    def get_area_per_unit(self) -> float:
        """Calculate area covered per unit (for tiles, boards, etc.)"""
        if self.width_cm and self.length_cm:
            return (self.width_cm / 100) * (self.length_cm / 100)  # Convert cm to m
        return 1.0  # Default 1 m2 if dimensions not specified
    
    def __str__(self) -> str:
        return f"{self.name} ({self.material_type}) - {self.unit_cost} per {self.unit_measurement}"
