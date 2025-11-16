"""Calculate costs for flooring projects"""

from src.models import FlooringMaterial, LayingPattern
from src.calculators import MaterialCalculator
from typing import Dict


class CostCalculator:
    """Handles cost calculations for flooring projects"""
    
    @staticmethod
    def calculate_material_cost(total_area: float, material: FlooringMaterial,
                               pattern: LayingPattern) -> Dict:
        """
        Calculate total material cost
        
        Returns:
            Dictionary with cost breakdown
        """
        material_info = MaterialCalculator.calculate_material_needed(total_area, material, pattern)
        quantity_units = material_info['quantity_units']
        
        material_cost = quantity_units * material.unit_cost
        
        return {
            'quantity_units': quantity_units,
            'unit_cost': material.unit_cost,
            'material_cost': material_cost,
            'unit_measurement': material.unit_measurement,
        }
    
    @staticmethod
    def calculate_total_project_cost(total_area: float, material: FlooringMaterial,
                                    pattern: LayingPattern,
                                    labor_cost_per_m2: float = 0,
                                    additional_costs: float = 0) -> Dict:
        """
        Calculate total project cost including material, labor, and other costs
        
        Args:
            total_area: Total flooring area in m2
            material: FloringMaterial instance
            pattern: LayingPattern instance
            labor_cost_per_m2: Labor cost per square meter
            additional_costs: Any additional costs (delivery, prep, etc.)
        
        Returns:
            Complete cost breakdown
        """
        material_cost_info = CostCalculator.calculate_material_cost(total_area, material, pattern)
        material_cost = material_cost_info['material_cost']
        
        labor_cost = total_area * labor_cost_per_m2
        consumables_info = MaterialCalculator.calculate_consumables(total_area, pattern)
        
        # Estimate consumable costs
        consumable_cost = 0
        if 'grout_kg' in consumables_info:
            consumable_cost += consumables_info['grout_kg'] * 2.5  # ~2.5 per kg
        if 'adhesive_kg' in consumables_info:
            consumable_cost += consumables_info['adhesive_kg'] * 0.8  # ~0.8 per kg
        if 'sealer_liters' in consumables_info:
            consumable_cost += consumables_info['sealer_liters'] * 15  # ~15 per liter
        
        total_cost = material_cost + labor_cost + consumable_cost + additional_costs
        
        return {
            'area_m2': total_area,
            'material_cost': material_cost,
            'labor_cost': labor_cost,
            'labor_cost_per_m2': labor_cost_per_m2,
            'consumable_cost': consumable_cost,
            'additional_costs': additional_costs,
            'total_cost': total_cost,
            'cost_per_m2': total_cost / total_area if total_area > 0 else 0,
        }
    
    @staticmethod
    def get_cost_summary(total_area: float, material: FlooringMaterial,
                        pattern: LayingPattern,
                        labor_cost_per_m2: float = 0) -> Dict:
        """Get comprehensive cost summary for project"""
        return CostCalculator.calculate_total_project_cost(
            total_area, material, pattern, labor_cost_per_m2
        )
