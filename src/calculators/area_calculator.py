"""Calculate flooring areas based on room specifications and layouts"""

from src.models import RoomSpecification
from typing import Optional


class AreaCalculator:
    """Handles area calculations for different room configurations"""
    
    @staticmethod
    def calculate_room_area(room: RoomSpecification) -> float:
        """Calculate total floor area for a room"""
        return room.get_total_area()
    
    @staticmethod
    def calculate_area_with_angles(length_m: float, width_m: float, 
                                   angle_degrees: float = 0) -> float:
        """Calculate area for diagonally laid flooring"""
        import math
        if angle_degrees == 0:
            return length_m * width_m
        
        # For diagonal cuts, additional area may be needed
        diagonal_factor = 1 + (angle_degrees / 90) * 0.15
        return (length_m * width_m) * diagonal_factor
    
    @staticmethod
    def calculate_perimeter(room: RoomSpecification) -> float:
        """Calculate room perimeter"""
        return room.get_perimeter()
    
    @staticmethod
    def calculate_border_area(room: RoomSpecification, border_width_m: float) -> float:
        """Calculate area needed for border flooring"""
        perimeter = room.get_perimeter()
        return perimeter * border_width_m
    
    @staticmethod
    def calculate_mosaic_pattern_area(room_area: float, pattern_complexity: float = 1.0) -> float:
        """Calculate area for complex mosaic patterns with potential extra material"""
        # Complex patterns may need additional material for intricate cuts
        return room_area * (1 + pattern_complexity * 0.05)
