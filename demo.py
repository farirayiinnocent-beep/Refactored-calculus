#!/usr/bin/env python3
"""
Interactive Flooring Calculator Demo
Simple test without import dependencies
"""

# Direct imports with absolute paths
import sys
import os

# Add workspace to path
sys.path.insert(0, '/workspaces/Refactored-calculus')

print("\n" + "="*70)
print("  FLOORING FINISHES CALCULATOR - INTERACTIVE DEMO")
print("="*70 + "\n")

try:
    print("📦 Loading modules...")
    from src.models import FlooringMaterial, LayingPattern, RoomSpecification, PatternType
    from src.calculators import AreaCalculator, MaterialCalculator, CostCalculator, WasteCalculator
    print("✓ All modules loaded successfully!\n")
    
    # Example 1: Living Room
    print("-" * 70)
    print("EXAMPLE 1: LIVING ROOM WITH CERAMIC TILES")
    print("-" * 70)
    
    room = RoomSpecification(
        length_m=5.0,
        width_m=4.0,
        room_name="Living Room"
    )
    print(f"\n📍 Room: {room.room_name}")
    print(f"   Dimensions: {room.length_m}m × {room.width_m}m")
    
    ceramic_tile = FlooringMaterial(
        name="Premium Ceramic Tile",
        material_type="tile",
        unit_cost=25.50,
        unit_measurement="m2",
        width_cm=30,
        length_cm=60,
        waste_factor=0.10
    )
    print(f"\n🏷️  Material: {ceramic_tile.name}")
    print(f"   Type: {ceramic_tile.material_type}")
    print(f"   Cost: €{ceramic_tile.unit_cost}/{ceramic_tile.unit_measurement}")
    print(f"   Dimensions: {ceramic_tile.width_cm}cm × {ceramic_tile.length_cm}cm")
    print(f"   Waste Factor: {ceramic_tile.waste_factor*100}%")
    
    straight_pattern = LayingPattern(
        pattern_type=PatternType.STRAIGHT,
        description="Simple straight laying pattern",
        additional_waste_percentage=5,
        difficulty_level="easy",
        joints_width_mm=3.0,
        grout_consumption_kg_per_m2=1.8
    )
    print(f"\n🎨 Pattern: {straight_pattern.pattern_type.value.upper()}")
    print(f"   Description: {straight_pattern.description}")
    print(f"   Additional Waste: {straight_pattern.additional_waste_percentage}%")
    print(f"   Difficulty: {straight_pattern.difficulty_level}")
    print(f"   Grout: {straight_pattern.grout_consumption_kg_per_m2} kg/m²")
    
    # Calculate area
    total_area = AreaCalculator.calculate_room_area(room)
    print(f"\n📐 AREA CALCULATION")
    print(f"   Base Area: {total_area:.2f} m²")
    
    # Calculate waste
    waste_qty, waste_details = WasteCalculator.calculate_waste_quantity(
        total_area, ceramic_tile, straight_pattern
    )
    print(f"\n♻️  WASTE ANALYSIS")
    print(f"   Material Waste: {waste_details['material_waste_m2']:.2f} m²")
    print(f"   Pattern Additional Waste: {waste_details['pattern_additional_waste_m2']:.2f} m²")
    print(f"   Total Waste: {waste_qty:.2f} m²")
    print(f"   Total Waste %: {waste_details['waste_percentage']:.1f}%")
    
    # Calculate material needed
    material_info = MaterialCalculator.calculate_material_needed(
        total_area, ceramic_tile, straight_pattern
    )
    print(f"\n📦 MATERIAL REQUIREMENTS")
    print(f"   Area with Waste: {material_info['area_needed_m2']:.2f} m²")
    print(f"   Quantity Needed: {material_info['quantity_units']:.2f} {material_info['unit_measurement']}")
    print(f"   Boxes Needed: {material_info['boxes_needed']} (if applicable)")
    
    # Calculate consumables
    consumables = MaterialCalculator.calculate_consumables(total_area, straight_pattern)
    print(f"\n🧴 CONSUMABLES REQUIRED")
    for item, qty in consumables.items():
        unit = "kg" if "kg" in item else "liters"
        print(f"   {item.replace('_', ' ').title()}: {qty:.2f} {unit}")
    
    # Calculate costs
    cost_info = CostCalculator.calculate_total_project_cost(
        total_area, ceramic_tile, straight_pattern,
        labor_cost_per_m2=15.0,
        additional_costs=50.0
    )
    print(f"\n💰 COST BREAKDOWN")
    print(f"   Material Cost: €{cost_info['material_cost']:.2f}")
    print(f"   Labor Cost: €{cost_info['labor_cost']:.2f}")
    print(f"   Consumables Cost: €{cost_info['consumable_cost']:.2f}")
    print(f"   Additional Costs: €{cost_info['additional_costs']:.2f}")
    print(f"   {'-'*40}")
    print(f"   TOTAL PROJECT COST: €{cost_info['total_cost']:.2f}")
    print(f"   Cost per m²: €{cost_info['cost_per_m2']:.2f}")
    
    # Example 2: Bedroom with Herringbone Pattern
    print("\n" + "-" * 70)
    print("EXAMPLE 2: BEDROOM WITH HERRINGBONE PATTERN")
    print("-" * 70)
    
    bedroom = RoomSpecification(
        length_m=4.0,
        width_m=3.5,
        room_name="Bedroom"
    )
    print(f"\n📍 Room: {bedroom.room_name}")
    print(f"   Dimensions: {bedroom.length_m}m × {bedroom.width_m}m")
    print(f"   Area: {bedroom.get_total_area():.2f} m²")
    
    wood_floor = FlooringMaterial(
        name="Oak Hardwood",
        material_type="wood",
        unit_cost=45.00,
        unit_measurement="m2",
        width_cm=9,
        length_cm=120,
        waste_factor=0.15
    )
    print(f"\n🏷️  Material: {wood_floor.name}")
    print(f"   Cost: €{wood_floor.unit_cost}/{wood_floor.unit_measurement}")
    print(f"   Waste Factor: {wood_floor.waste_factor*100}%")
    
    herringbone_pattern = LayingPattern(
        pattern_type=PatternType.HERRINGBONE,
        description="Classic V-shaped weaving pattern",
        additional_waste_percentage=12,
        difficulty_level="hard",
        joints_width_mm=2.0,
        grout_consumption_kg_per_m2=0  # No grout for wood
    )
    print(f"\n🎨 Pattern: {herringbone_pattern.pattern_type.value.upper()}")
    print(f"   Description: {herringbone_pattern.description}")
    print(f"   Additional Waste: {herringbone_pattern.additional_waste_percentage}%")
    print(f"   Difficulty: {herringbone_pattern.difficulty_level}")
    
    bedroom_area = AreaCalculator.calculate_room_area(bedroom)
    waste_qty2, waste_details2 = WasteCalculator.calculate_waste_quantity(
        bedroom_area, wood_floor, herringbone_pattern
    )
    material_info2 = MaterialCalculator.calculate_material_needed(
        bedroom_area, wood_floor, herringbone_pattern
    )
    cost_info2 = CostCalculator.calculate_total_project_cost(
        bedroom_area, wood_floor, herringbone_pattern,
        labor_cost_per_m2=20.0,
        additional_costs=30.0
    )
    
    print(f"\n📐 AREA CALCULATION: {bedroom_area:.2f} m²")
    print(f"\n♻️  WASTE: {waste_qty2:.2f} m² ({waste_details2['waste_percentage']:.1f}%)")
    print(f"\n📦 MATERIAL: {material_info2['quantity_units']:.2f} {material_info2['unit_measurement']}")
    print(f"\n💰 TOTAL COST: €{cost_info2['total_cost']:.2f}")
    print(f"   Cost per m²: €{cost_info2['cost_per_m2']:.2f}")
    
    print("\n" + "="*70)
    print("✅ DEMO COMPLETED SUCCESSFULLY!")
    print("="*70 + "\n")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
