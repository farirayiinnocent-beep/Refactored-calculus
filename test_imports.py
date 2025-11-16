#!/usr/bin/env python3
"""Test if imports work correctly"""

try:
    print("Testing imports...")
    from src.models import FlooringMaterial, LayingPattern, RoomSpecification, PatternType
    print("✓ Models imported successfully")
    
    from src.calculators import AreaCalculator, MaterialCalculator, CostCalculator, WasteCalculator
    print("✓ Calculators imported successfully")
    
    from src.utils.report_generator import ReportGenerator
    print("✓ Utils imported successfully")
    
    print("\n✓ All imports successful!")
    
    # Quick test
    room = RoomSpecification(length_m=5.0, width_m=4.0, room_name="Test Room")
    print(f"\nTest: {room}")
    
except Exception as e:
    print(f"✗ Import failed: {e}")
    import traceback
    traceback.print_exc()
