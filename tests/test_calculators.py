"""Unit tests for calculator modules"""

import pytest
from src.models import FlooringMaterial, LayingPattern, RoomSpecification, PatternType
from src.calculators import AreaCalculator, MaterialCalculator, CostCalculator, WasteCalculator


class TestAreaCalculator:
    """Test area calculation functions"""
    
    def test_calculate_room_area(self):
        """Test basic room area calculation"""
        room = RoomSpecification(length_m=5.0, width_m=4.0)
        area = AreaCalculator.calculate_room_area(room)
        assert area == 20.0
    
    def test_calculate_perimeter(self):
        """Test room perimeter calculation"""
        room = RoomSpecification(length_m=5.0, width_m=4.0)
        perimeter = AreaCalculator.calculate_perimeter(room)
        assert perimeter == 18.0
    
    def test_border_area_calculation(self):
        """Test border area calculation"""
        room = RoomSpecification(length_m=5.0, width_m=4.0)
        border_area = AreaCalculator.calculate_border_area(room, border_width_m=0.5)
        assert border_area == 9.0


class TestWasteCalculator:
    """Test waste calculation functions"""
    
    def test_waste_calculation_basic(self):
        """Test basic waste calculation"""
        material = FlooringMaterial(
            name="Tile", material_type="tile",
            unit_cost=10, unit_measurement="m2",
            waste_factor=0.10
        )
        pattern = LayingPattern(
            pattern_type=PatternType.STRAIGHT,
            description="Straight", additional_waste_percentage=5
        )
        
        waste, details = WasteCalculator.calculate_waste_quantity(100, material, pattern)
        
        assert waste > 10  # At least 10% waste
        assert 'waste_percentage' in details
        assert details['waste_percentage'] > 10


class TestMaterialCalculator:
    """Test material calculation functions"""
    
    def test_material_needed_calculation(self):
        """Test material quantity calculation"""
        material = FlooringMaterial(
            name="Wood Plank", material_type="wood",
            unit_cost=20, unit_measurement="m2",
            waste_factor=0.15
        )
        pattern = LayingPattern(
            pattern_type=PatternType.DIAGONAL,
            description="Diagonal", additional_waste_percentage=10
        )
        
        material_info = MaterialCalculator.calculate_material_needed(50, material, pattern)
        
        assert 'area_needed_m2' in material_info
        assert 'quantity_units' in material_info
        assert material_info['area_needed_m2'] > 50


class TestCostCalculator:
    """Test cost calculation functions"""
    
    def test_material_cost_calculation(self):
        """Test material cost calculation"""
        material = FlooringMaterial(
            name="Tile", material_type="tile",
            unit_cost=25, unit_measurement="m2",
            waste_factor=0.10
        )
        pattern = LayingPattern(
            pattern_type=PatternType.STRAIGHT,
            description="Straight", additional_waste_percentage=0
        )
        
        cost_info = CostCalculator.calculate_material_cost(100, material, pattern)
        
        assert 'material_cost' in cost_info
        assert cost_info['material_cost'] > 0
    
    def test_total_project_cost(self):
        """Test total project cost calculation"""
        material = FlooringMaterial(
            name="Tile", material_type="tile",
            unit_cost=25, unit_measurement="m2",
            waste_factor=0.10
        )
        pattern = LayingPattern(
            pattern_type=PatternType.STRAIGHT,
            description="Straight", additional_waste_percentage=0
        )
        
        cost = CostCalculator.calculate_total_project_cost(
            100, material, pattern,
            labor_cost_per_m2=15,
            additional_costs=100
        )
        
        assert cost['total_cost'] > 0
        assert 'cost_per_m2' in cost
        assert cost['cost_per_m2'] > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
