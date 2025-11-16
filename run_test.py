#!/usr/bin/env python3
"""Direct inline test of flooring calculator"""

import sys
sys.path.insert(0, '/workspaces/Refactored-calculus')

# Import all required modules
from src.models.flooring_material import FlooringMaterial
from src.models.laying_pattern import LayingPattern, PatternType
from src.models.room_specification import RoomSpecification
from src.calculators.area_calculator import AreaCalculator
from src.calculators.material_calculator import MaterialCalculator
from src.calculators.cost_calculator import CostCalculator
from src.calculators.waste_calculator import WasteCalculator
from src.utils.report_generator import ReportGenerator

print("╔════════════════════════════════════════════════════════════════╗")
print("║         FLOORING FINISHES CALCULATOR - TEST RUN               ║")
print("╚════════════════════════════════════════════════════════════════╝\n")

# Define room
living_room = RoomSpecification(
    length_m=5.0,
    width_m=4.0,
    room_name="Living Room"
)
print(f"\n✓ Room: {living_room}")

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
print(f"✓ Material: {ceramic_tile}")

# Define laying pattern
straight_pattern = LayingPattern(
    pattern_type=PatternType.STRAIGHT,
    description="Simple straight laying pattern",
    additional_waste_percentage=5,
    difficulty_level="easy",
    joints_width_mm=3.0,
    grout_consumption_kg_per_m2=1.8
)
print(f"✓ Pattern: {straight_pattern}")

# Calculate area
total_area = AreaCalculator.calculate_room_area(living_room)
print(f"\n📐 CALCULATIONS")
print(f"   Total Area: {total_area:.2f} m²")

# Calculate waste
waste_qty, waste_details = WasteCalculator.calculate_waste_quantity(
    total_area, ceramic_tile, straight_pattern
)
print(f"\n♻️  WASTE ANALYSIS")
print(f"   Material Waste: {waste_details['material_waste_m2']:.2f} m²")
print(f"   Pattern Additional Waste: {waste_details['pattern_additional_waste_m2']:.2f} m²")
print(f"   Total Waste: {waste_qty:.2f} m² ({waste_details['waste_percentage']:.1f}%)")

# Calculate material needed
material_info = MaterialCalculator.calculate_material_needed(
    total_area, ceramic_tile, straight_pattern
)
print(f"\n📦 MATERIAL REQUIREMENTS")
print(f"   Total Area with Waste: {material_info['area_needed_m2']:.2f} m²")
print(f"   Quantity Needed: {material_info['quantity_units']:.2f} {material_info['unit_measurement']}")

# Calculate consumables
consumables = MaterialCalculator.calculate_consumables(total_area, straight_pattern)
print(f"\n🧴 CONSUMABLES REQUIRED")
for item, qty in consumables.items():
    unit = "kg" if "kg" in item else "liters"
    print(f"   {item}: {qty:.2f} {unit}")

# Calculate costs
cost_info = CostCalculator.calculate_total_project_cost(
    total_area, ceramic_tile, straight_pattern,
    labor_cost_per_m2=15.0,
    additional_costs=50.0
)
print(f"\n💰 COST ANALYSIS")
print(f"   Material Cost: €{cost_info['material_cost']:.2f}")
print(f"   Labor Cost: €{cost_info['labor_cost']:.2f} ({cost_info['labor_cost_per_m2']}€/m²)")
print(f"   Consumables Cost: €{cost_info['consumable_cost']:.2f}")
print(f"   Additional Costs: €{cost_info['additional_costs']:.2f}")
print(f"   " + "─" * 40)
print(f"   TOTAL PROJECT COST: €{cost_info['total_cost']:.2f}")
print(f"   Cost per m²: €{cost_info['cost_per_m2']:.2f}")

print("\n✓ All calculations completed successfully!")
