"""
Flooring Finishes Calculator - Main Application
"""

from src.models import FlooringMaterial, LayingPattern, RoomSpecification, PatternType
from src.calculators import AreaCalculator, MaterialCalculator, CostCalculator, WasteCalculator
from src.utils.report_generator import ReportGenerator


def main():
    """Main application demonstration"""
    
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║         FLOORING FINISHES CALCULATOR                          ║")
    print("╚════════════════════════════════════════════════════════════════╝\n")
    
    # Example 1: Simple rectangular room with ceramic tiles
    print("EXAMPLE 1: Living Room with Ceramic Tiles")
    print("─" * 60)
    
    # Define room
    living_room = RoomSpecification(
        length_m=5.0,
        width_m=4.0,
        room_name="Living Room"
    )
    
    # Define material
    ceramic_tile = FlooringMaterial(
        name="Premium Ceramic Tile",
        material_type="tile",
        unit_cost=25.50,
        unit_measurement="m2",
        width_cm=30,
        length_cm=60,
        waste_factor=0.10
    )
    
    # Define laying pattern
    straight_pattern = LayingPattern(
        pattern_type=PatternType.STRAIGHT,
        description="Simple straight laying pattern",
        additional_waste_percentage=5,
        difficulty_level="easy",
        joints_width_mm=3.0,
        grout_consumption_kg_per_m2=1.8
    )
    
    # Calculate area
    total_area = AreaCalculator.calculate_room_area(living_room)
    print(f"\n{living_room}")
    print(f"Total Area: {total_area:.2f} m²")
    
    # Calculate waste
    waste_qty, waste_details = WasteCalculator.calculate_waste_quantity(
        total_area, ceramic_tile, straight_pattern
    )
    print(f"\nWaste Analysis:")
    print(f"  Material Waste: {waste_details['material_waste_m2']:.2f} m²")
    print(f"  Pattern Additional Waste: {waste_details['pattern_additional_waste_m2']:.2f} m²")
    print(f"  Total Waste: {waste_qty:.2f} m² ({waste_details['waste_percentage']:.1f}%)")
    
    # Calculate material needed
    material_info = MaterialCalculator.calculate_material_needed(
        total_area, ceramic_tile, straight_pattern
    )
    print(f"\nMaterial Requirements:")
    print(f"  Total Area with Waste: {material_info['area_needed_m2']:.2f} m²")
    print(f"  Quantity Needed: {material_info['quantity_units']:.2f} {material_info['unit_measurement']}")
    
    # Calculate consumables
    consumables = MaterialCalculator.calculate_consumables(total_area, straight_pattern)
    print(f"\nConsumables Required:")
    for item, qty in consumables.items():
        unit = "kg" if "kg" in item else "liters"
        print(f"  {item}: {qty:.2f} {unit}")
    
    # Calculate costs
    cost_info = CostCalculator.calculate_total_project_cost(
        total_area, ceramic_tile, straight_pattern,
        labor_cost_per_m2=15.0,
        additional_costs=50.0
    )
    print(f"\nCost Analysis:")
    print(f"  Material Cost: €{cost_info['material_cost']:.2f}")
    print(f"  Labor Cost: €{cost_info['labor_cost']:.2f} ({cost_info['labor_cost_per_m2']}€/m²)")
    print(f"  Consumables Cost: €{cost_info['consumable_cost']:.2f}")
    print(f"  Additional Costs: €{cost_info['additional_costs']:.2f}")
    print(f"  ─" * 40)
    print(f"  TOTAL PROJECT COST: €{cost_info['total_cost']:.2f}")
    print(f"  Cost per m²: €{cost_info['cost_per_m2']:.2f}")
    
    # Generate report
    report_data = {
        'area_m2': total_area,
        'material_name': ceramic_tile.name,
        'quantity_units': material_info['quantity_units'],
        'unit_measurement': material_info['unit_measurement'],
        'waste_percent': material_info['total_waste_factor_percent'],
        'pattern_name': straight_pattern.pattern_type.value.title(),
        'pattern_description': straight_pattern.description,
        'material_cost': cost_info['material_cost'],
        'labor_cost': cost_info['labor_cost'],
        'consumable_cost': cost_info['consumable_cost'],
        'total_cost': cost_info['total_cost'],
        'cost_per_m2': cost_info['cost_per_m2']
    }
    
    report = ReportGenerator.generate_project_report(living_room.room_name, report_data)
    print("\n" + report)
    
    print("\n✓ Calculator ready for use!")
    print("Import the modules to build your custom flooring calculations.")


if __name__ == "__main__":
    main()
