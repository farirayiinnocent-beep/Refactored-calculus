"""Calculate material requirements and quantities"""

from src.models import FlooringMaterial, LayingPattern
from typing import Dict, Optional
import math


class MaterialCalculator:
    """Handles material quantity calculations"""
    
    @staticmethod
    def calculate_material_needed(total_area: float, material: FlooringMaterial,
                                 pattern: LayingPattern) -> Dict:
        """
        Calculate total material needed including waste
        
        Returns:
            Dictionary with material quantities and counts
        """
        # Calculate area with waste
        total_waste_factor = pattern.get_total_waste_factor(material.waste_factor)
        area_with_waste = total_area * (1 + total_waste_factor)
        
        # Calculate quantity needed
        area_per_unit = material.get_area_per_unit()
        
        if material.unit_measurement == 'm2':
            quantity_m2 = area_with_waste
            quantity_units = area_with_waste / area_per_unit if area_per_unit > 0 else 0
        else:
            quantity_units = math.ceil(area_with_waste / area_per_unit) if area_per_unit > 0 else 0
            quantity_m2 = quantity_units * area_per_unit
        
        # Calculate boxes needed
        boxes_needed = 1
        if material.units_per_box and material.units_per_box > 0:
            boxes_needed = math.ceil(quantity_units / material.units_per_box)
        
        return {
            'area_needed_m2': quantity_m2,
            'quantity_units': quantity_units,
            'unit_measurement': material.unit_measurement,
            'boxes_needed': boxes_needed,
            'total_waste_factor_percent': (total_waste_factor * 100),
        }
    
    @staticmethod
    def calculate_grout_needed(total_area: float, pattern: LayingPattern) -> Optional[float]:
        """Calculate grout consumption if applicable"""
        if pattern.grout_consumption_kg_per_m2:
            return total_area * pattern.grout_consumption_kg_per_m2
        return None
    
    @staticmethod
    def calculate_consumables(total_area: float, pattern: LayingPattern) -> Dict:
        """Calculate consumables like grout, sealant, adhesive, etc."""
        consumables = {
            'grout_kg': MaterialCalculator.calculate_grout_needed(total_area, pattern),
            'adhesive_kg': total_area * 1.5,  # Typical 1.5 kg per m2 for thin-set
            'sealer_liters': total_area / 10,  # Typical coverage 10 m2 per liter
        }
        
        return {k: v for k, v in consumables.items() if v is not None}
