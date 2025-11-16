"""Laying pattern definitions and properties"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class PatternType(Enum):
    """Available laying patterns for flooring"""
    STRAIGHT = "straight"
    DIAGONAL = "diagonal"
    HERRINGBONE = "herringbone"
    CHEVRON = "chevron"
    BASKET_WEAVE = "basket_weave"
    RANDOM = "random"
    RUNNING_BOND = "running_bond"
    MIXED_SIZES = "mixed_sizes"


@dataclass
class LayingPattern:
    """Represents a laying pattern with its specifications"""
    
    pattern_type: PatternType
    description: str
    additional_waste_percentage: float = 0.0  # Additional waste beyond material waste
    difficulty_level: str = "medium"  # easy, medium, hard
    joints_width_mm: float = 3.0  # Joint width if applicable
    grout_consumption_kg_per_m2: Optional[float] = None
    
    def get_total_waste_factor(self, material_waste: float) -> float:
        """Calculate total waste factor including pattern-specific waste"""
        return material_waste + (material_waste * self.additional_waste_percentage / 100)
    
    def __str__(self) -> str:
        return f"{self.pattern_type.value.replace('_', ' ').title()} - {self.description}"
