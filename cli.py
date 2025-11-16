#!/usr/bin/env python3
"""Command-line interface for the Flooring Finishes Calculator

Usage examples:
  python cli.py --example living-room
  python cli.py --length 5 --width 4 --material-name "Ceramic" --unit-cost 25.5 --pattern straight --labor 15
"""

import argparse
import sys
from src.models import FlooringMaterial, LayingPattern, RoomSpecification, PatternType
from src.calculators import AreaCalculator, MaterialCalculator, CostCalculator, WasteCalculator
from src.utils.report_generator import ReportGenerator


def parse_pattern(value: str) -> PatternType:
    s = value.strip().lower().replace('-', '_').replace(' ', '_')
    for p in PatternType:
        if p.value == s or p.name.lower() == s:
            return p
    raise argparse.ArgumentTypeError(f"Unknown pattern '{value}'. Use one of: " + ", ".join([p.value for p in PatternType]))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Flooring Finishes Calculator — CLI")

    group = p.add_mutually_exclusive_group()
    group.add_argument('--example', choices=['living-room', 'bedroom'], help='Run a built-in example')
    group.add_argument('--interactive', action='store_true', help='(Reserved) interactive mode (not implemented)')

    p.add_argument('--length', type=float, help='Room length in meters')
    p.add_argument('--width', type=float, help='Room width in meters')
    p.add_argument('--room-name', default='Room', help='Room name')

    p.add_argument('--material-name', default='Material', help='Material name')
    p.add_argument('--material-type', default='tile', help='Material type (tile, wood, etc.)')
    p.add_argument('--unit-cost', type=float, default=0.0, help='Material unit cost (per unit_measurement)')
    p.add_argument('--unit-measurement', default='m2', help='Unit measurement, e.g., m2')
    p.add_argument('--width-cm', type=float, help='Material width in cm')
    p.add_argument('--length-cm', type=float, help='Material length in cm')
    p.add_argument('--waste-factor', type=float, default=0.10, help='Material waste factor (e.g., 0.10 for 10%)')

    p.add_argument('--pattern', type=parse_pattern, default=PatternType.STRAIGHT, help='Laying pattern (straight, diagonal, herringbone, etc.)')
    p.add_argument('--pattern-waste', type=float, default=None, help='Override additional pattern waste percent (e.g., 5)')
    p.add_argument('--grout-kg-per-m2', type=float, default=None, help='Grout consumption kg per m2')

    p.add_argument('--labor', type=float, default=0.0, help='Labor cost per m2')
    p.add_argument('--additional-costs', type=float, default=0.0, help='Additional fixed costs')

    p.add_argument('--save-report', help='Save a text report to given filename')

    return p


def run_from_args(args: argparse.Namespace) -> str:
    # Build room
    room = RoomSpecification(
        length_m=args.length,
        width_m=args.width,
        room_name=args.room_name
    )

    # Build material
    material = FlooringMaterial(
        name=args.material_name,
        material_type=args.material_type,
        unit_cost=args.unit_cost,
        unit_measurement=args.unit_measurement,
        width_cm=args.width_cm,
        length_cm=args.length_cm,
        waste_factor=args.waste_factor
    )

    # Build pattern
    pattern = LayingPattern(
        pattern_type=args.pattern,
        description=args.pattern.value,
        additional_waste_percentage=(args.pattern_waste if args.pattern_waste is not None else args.pattern.value and 0),
        joints_width_mm=3.0,
        grout_consumption_kg_per_m2=args.grout_kg_per_m2
    )

    area = AreaCalculator.calculate_room_area(room)
    waste_qty, waste_details = WasteCalculator.calculate_waste_quantity(area, material, pattern)
    material_info = MaterialCalculator.calculate_material_needed(area, material, pattern)
    consumables = MaterialCalculator.calculate_consumables(area, pattern)
    cost_info = CostCalculator.calculate_total_project_cost(
        area, material, pattern, labor_cost_per_m2=args.labor, additional_costs=args.additional_costs
    )

    report_data = {
        'room_name': room.room_name,
        'area_m2': area,
        'material_name': material.name,
        'quantity_units': material_info['quantity_units'],
        'unit_measurement': material_info['unit_measurement'],
        'waste_percent': (waste_details.get('waste_percentage') if waste_details else 0),
        'pattern_name': pattern.pattern_type.value,
        'pattern_description': pattern.description,
        'material_cost': cost_info['material_cost'],
        'labor_cost': cost_info['labor_cost'],
        'consumable_cost': cost_info['consumable_cost'],
        'total_cost': cost_info['total_cost'],
        'cost_per_m2': cost_info['cost_per_m2']
    }

    report = ReportGenerator.generate_project_report(room.room_name, report_data)

    # Print summary
    print(report)

    return report


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.example:
        if args.example == 'living-room':
            args.length = 5.0
            args.width = 4.0
            args.room_name = 'Living Room'
            args.material_name = 'Premium Ceramic Tile'
            args.material_type = 'tile'
            args.unit_cost = 25.50
            args.unit_measurement = 'm2'
            args.width_cm = 30
            args.length_cm = 60
            args.waste_factor = 0.10
            args.pattern = PatternType.STRAIGHT
            args.grout_kg_per_m2 = 1.8
            args.labor = 15.0
            args.additional_costs = 50.0
        elif args.example == 'bedroom':
            args.length = 4.0
            args.width = 3.5
            args.room_name = 'Bedroom'
            args.material_name = 'Oak Hardwood'
            args.material_type = 'wood'
            args.unit_cost = 45.0
            args.unit_measurement = 'm2'
            args.width_cm = 9
            args.length_cm = 120
            args.waste_factor = 0.15
            args.pattern = PatternType.HERRINGBONE
            args.grout_kg_per_m2 = None
            args.labor = 20.0
            args.additional_costs = 30.0

    # Validate required args
    if args.length is None or args.width is None:
        parser.error('You must provide --length and --width (or use --example).')

    report = run_from_args(args)

    if args.save_report:
        with open(args.save_report, 'w', encoding='utf-8') as fh:
            fh.write(report)
        print(f"Saved report to {args.save_report}")


if __name__ == '__main__':
    main()
