#!/usr/bin/env python3
"""
QUICK START - Flooring Calculator

This script demonstrates the calculator in action with real examples.
Run: python3 quick_start.py
"""

import sys
sys.path.insert(0, '/workspaces/Refactored-calculus')

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")

def print_section(text):
    """Print a section header"""
    print("\n" + text)
    print("-" * 70)

def example_1():
    """Example 1: Simple ceramic tile calculation"""
    from src.models import FlooringMaterial, LayingPattern, RoomSpecification, PatternType
    from src.calculators import AreaCalculator, MaterialCalculator, CostCalculator, WasteCalculator
    
    print_section("📍 INPUT: Define the Project")
    
    # Room
    room = RoomSpecification(length_m=5.0, width_m=4.0, room_name="Living Room")
    print(f"Room: {room.room_name}")
    print(f"  Dimensions: {room.length_m}m × {room.width_m}m")
    
    # Material
    tile = FlooringMaterial(
        name="Ceramic Tile",
        material_type="tile",
        unit_cost=25.50,
        unit_measurement="m2",
        width_cm=30,
        length_cm=60,
        waste_factor=0.10
    )
    print(f"\nMaterial: {tile.name}")
    print(f"  Cost: €{tile.unit_cost}/m²")
    print(f"  Waste: {tile.waste_factor*100}%")
    
    # Pattern
    pattern = LayingPattern(
        pattern_type=PatternType.STRAIGHT,
        description="Simple straight layout",
        additional_waste_percentage=5,
        grout_consumption_kg_per_m2=1.8
    )
    print(f"\nPattern: {pattern.pattern_type.value.upper()}")
    print(f"  Additional Waste: {pattern.additional_waste_percentage}%")
    print(f"  Grout: {pattern.grout_consumption_kg_per_m2} kg/m²")
    
    print_section("🧮 OUTPUT: Calculations")
    
    # Calculate
    area = AreaCalculator.calculate_room_area(room)
    print(f"✓ Base Area: {area:.2f} m²")
    
    waste_qty, waste_details = WasteCalculator.calculate_waste_quantity(area, tile, pattern)
    print(f"✓ Waste: {waste_qty:.2f} m² ({waste_details['waste_percentage']:.1f}%)")
    
    material = MaterialCalculator.calculate_material_needed(area, tile, pattern)
    print(f"✓ Material Needed: {material['quantity_units']:.2f} m²")
    
    consumables = MaterialCalculator.calculate_consumables(area, pattern)
    print(f"✓ Grout: {consumables['grout_kg']:.2f} kg")
    print(f"✓ Adhesive: {consumables['adhesive_kg']:.2f} kg")
    
    costs = CostCalculator.calculate_total_project_cost(
        area, tile, pattern,
        labor_cost_per_m2=15.0,
        additional_costs=50.0
    )
    print(f"\n✓ Material Cost: €{costs['material_cost']:.2f}")
    print(f"✓ Labor Cost: €{costs['labor_cost']:.2f}")
    print(f"✓ Consumables: €{costs['consumable_cost']:.2f}")
    print(f"✓ Total: €{costs['total_cost']:.2f}")
    print(f"✓ Per m²: €{costs['cost_per_m2']:.2f}")

def example_2():
    """Example 2: Wood floor with herringbone pattern"""
    from src.models import FlooringMaterial, LayingPattern, RoomSpecification, PatternType
    from src.calculators import AreaCalculator, MaterialCalculator, CostCalculator
    
    print_section("📍 INPUT: Bedroom Project")
    
    room = RoomSpecification(length_m=4.0, width_m=3.5, room_name="Bedroom")
    print(f"Room: {room.room_name}")
    print(f"  Area: {room.get_total_area():.2f} m²")
    
    wood = FlooringMaterial(
        name="Oak Hardwood",
        material_type="wood",
        unit_cost=45.00,
        unit_measurement="m2",
        width_cm=9,
        length_cm=120,
        waste_factor=0.15
    )
    print(f"\nMaterial: {wood.name} @ €{wood.unit_cost}/m²")
    
    pattern = LayingPattern(
        pattern_type=PatternType.HERRINGBONE,
        description="Classic V-shaped weaving",
        additional_waste_percentage=12,
        difficulty_level="hard"
    )
    print(f"\nPattern: {pattern.pattern_type.value.upper()}")
    
    print_section("🧮 OUTPUT: Results")
    
    area = AreaCalculator.calculate_room_area(room)
    costs = CostCalculator.calculate_total_project_cost(
        area, wood, pattern,
        labor_cost_per_m2=20.0
    )
    print(f"Total Material Cost: €{costs['material_cost']:.2f}")
    print(f"Total Project Cost: €{costs['total_cost']:.2f}")
    print(f"Cost per m²: €{costs['cost_per_m2']:.2f}")

def example_3():
    """Example 3: Quick reference - all patterns"""
    from src.models import PatternType
    
    print_section("🎨 All Supported Patterns")
    
    for pattern in PatternType:
        print(f"  • {pattern.value.replace('_', ' ').upper()}")

def main():
    """Run examples"""
    print_header("⭐ FLOORING CALCULATOR - QUICK START ⭐")
    
    try:
        example_1()
        print("\n")
        example_2()
        print("\n")
        example_3()
        
        print_header("✅ EXAMPLES COMPLETED SUCCESSFULLY")
        print("\nDocumentation:")
        print("  • README.md - Full documentation")
        print("  • PROJECT_OVERVIEW.md - Complete overview")
        print("  • VISUAL_DEMO.md - Visual examples")
        print("  • TEST_GUIDE.md - Testing instructions")
        print("\nNext Steps:")
        print("  1. Check out the code structure in src/")
        print("  2. Run: python3 demo.py for more examples")
        print("  3. Run: pytest tests/ -v to run unit tests")
        print("  4. Customize for your needs!\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
