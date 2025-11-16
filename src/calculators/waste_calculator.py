"""Calculate material waste and cutting losses"""

from src.models import FlooringMaterial, LayingPattern
from typing import Dict, Tuple


class WasteCalculator:
    """Handles waste calculations for different patterns and materials"""
    
    @staticmethod
    def calculate_waste_quantity(total_area: float, material: FlooringMaterial, 
                                 pattern: LayingPattern) -> Tuple[float, Dict]:
        """
        Calculate waste quantity based on material and pattern
        
        Returns:
            Tuple of (waste_area_m2, waste_details_dict)
        """
        material_waste = total_area * material.waste_factor
        pattern_additional_waste = material_waste * pattern.additional_waste_percentage / 100
        total_waste = material_waste + pattern_additional_waste
        
        details = {
            'material_waste_m2': material_waste,
            'pattern_additional_waste_m2': pattern_additional_waste,
            'total_waste_m2': total_waste,
            'waste_percentage': (total_waste / total_area * 100) if total_area > 0 else 0
        }
        
        return total_waste, details
    
    @staticmethod
    def calculate_cutting_waste(piece_size_m2: float, room_area: float) -> float:
        """Calculate waste from cutting tiles/boards to fit"""
        if piece_size_m2 == 0:
            return 0
        pieces_needed = room_area / piece_size_m2
        full_pieces = int(pieces_needed)
        partial_piece_waste = pieces_needed - full_pieces
        return partial_piece_waste * piece_size_m2
    
    @staticmethod
    def get_waste_summary(total_area: float, material: FlooringMaterial, 
                         pattern: LayingPattern) -> Dict:
        """Get comprehensive waste summary"""
        waste, details = WasteCalculator.calculate_waste_quantity(total_area, material, pattern)
        
        return {
            'room_area_m2': total_area,
            'with_waste_area_m2': total_area + waste,
            **details
        }
