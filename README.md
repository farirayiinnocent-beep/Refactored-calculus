# Refactored-calculus

A comprehensive flooring finishes calculator with emphasis on calculating area for different laying patterns, cut and waste of material, costs, consumables, and all other necessary information for different floor finishes laying.

## Features

✓ **Area Calculation** - Calculate flooring areas for various room configurations and shapes
✓ **Laying Patterns** - Support for multiple patterns (Straight, Diagonal, Herringbone, Chevron, etc.)
✓ **Waste Calculation** - Accurate material waste estimation based on pattern and material type
✓ **Material Requirements** - Determine exact quantities needed for tiles, boards, or other flooring materials
✓ **Cost Estimation** - Calculate total project costs including material, labor, and consumables
✓ **Consumables** - Track grout, adhesive, sealant, and other materials required
✓ **Comprehensive Reports** - Generate detailed project reports with all calculations

## Project Structure

```
Refactored-calculus/
├── src/
│   ├── __init__.py
│   ├── models/                 # Data models
│   │   ├── flooring_material.py    # Material specifications
│   │   ├── laying_pattern.py       # Pattern definitions
│   │   └── room_specification.py   # Room dimensions
│   ├── calculators/            # Calculation engines
│   │   ├── area_calculator.py      # Area calculations
│   │   ├── waste_calculator.py     # Waste estimations
│   │   ├── material_calculator.py  # Material quantities
│   │   └── cost_calculator.py      # Cost breakdowns
│   └── utils/                  # Utilities
│       ├── unit_converter.py       # Unit conversions
│       └── report_generator.py     # Report generation
├── tests/
│   └── test_calculators.py     # Unit tests
├── main.py                     # Main application with examples
├── requirements.txt            # Python dependencies
└── README.md                   # Documentation
```

## Installation

### Requirements
- Python 3.8+

### Setup

1. Clone the repository:
```bash
git clone https://github.com/farirayiinnocent-beep/Refactored-calculus.git
cd Refactored-calculus
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Install editable for CLI:
```bash
pip install -e .
```

## Quick Start

### Run Examples
```bash
# Run main example with multiple calculations
python main.py

# Run quick demo with 2 scenarios
python quick_start.py

# Run interactive demo
python demo.py
```

### Use the CLI
```bash
# Show living room example report
python cli.py --example living-room

# Show bedroom example report
python cli.py --example bedroom

# Custom calculation (tile 20m² room, 10% waste, €25/m²)
python cli.py --material-cost 25 --waste-factor 0.1 --area 20

# Save report to file
python cli.py --example living-room --save-report report.txt
```

### Run Tests
```bash
pytest tests/ -v
```

## Usage

### Basic Script Usage

Run the example calculations:
```bash
python main.py
```

### Basic Usage Example

```python
from src.models import FlooringMaterial, LayingPattern, RoomSpecification, PatternType
from src.calculators import AreaCalculator, MaterialCalculator, CostCalculator
from src.utils.report_generator import ReportGenerator

# Define room
room = RoomSpecification(
    length_m=5.0,
    width_m=4.0,
    room_name="Living Room"
)

# Define material
tile = FlooringMaterial(
    name="Ceramic Tile",
    material_type="tile",
    unit_cost=25.50,
    unit_measurement="m2",
    width_cm=30,
    length_cm=60,
    waste_factor=0.10
)

# Define laying pattern
pattern = LayingPattern(
    pattern_type=PatternType.STRAIGHT,
    description="Simple straight laying",
    additional_waste_percentage=5,
    joints_width_mm=3.0,
    grout_consumption_kg_per_m2=1.8
)

# Calculate area
area = AreaCalculator.calculate_room_area(room)
print(f"Room area: {area:.2f} m²")

# Calculate material needed
material_info = MaterialCalculator.calculate_material_needed(area, tile, pattern)
print(f"Material needed: {material_info['quantity_units']:.2f} {material_info['unit_measurement']}")

# Calculate costs
costs = CostCalculator.calculate_total_project_cost(
    area, tile, pattern,
    labor_cost_per_m2=15.0,
    additional_costs=50.0
)
print(f"Total cost: €{costs['total_cost']:.2f}")
```

## Available Laying Patterns

- **STRAIGHT** - Simple horizontal/vertical alignment
- **DIAGONAL** - 45-degree angled layout
- **HERRINGBONE** - V-shaped weaving pattern
- **CHEVRON** - Angled zigzag pattern
- **BASKET_WEAVE** - Interlocking rectangular pattern
- **RANDOM** - Random size and arrangement
- **RUNNING_BOND** - Offset brick-like pattern
- **MIXED_SIZES** - Combination of different tile sizes

## Core Modules

### Models

#### `FlooringMaterial`
Represents flooring material properties:
- Material type (tile, wood, laminate, stone, etc.)
- Unit cost and measurement
- Dimensions (width, length, thickness)
- Waste factor
- Area per unit calculation

#### `LayingPattern`
Represents laying patterns:
- Pattern type enumeration
- Description
- Additional waste percentage
- Difficulty level
- Joint width
- Grout consumption

#### `RoomSpecification`
Represents room dimensions:
- Length and width
- Height (optional)
- Room shape and name
- Additional area for irregular shapes
- Perimeter calculation

### Calculators

#### `AreaCalculator`
- Calculate room area
- Calculate area with angles (diagonal layouts)
- Calculate perimeter
- Calculate border areas
- Calculate mosaic pattern areas

#### `WasteCalculator`
- Calculate waste quantity
- Calculate cutting waste
- Generate waste summary
- Waste percentage calculations

#### `MaterialCalculator`
- Calculate total material needed
- Calculate grout requirements
- Calculate consumables (adhesive, sealant)
- Box count estimation

#### `CostCalculator`
- Calculate material costs
- Calculate labor costs
- Calculate consumable costs
- Generate comprehensive cost breakdowns
- Cost per square meter

### Utilities

#### `UnitConverter`
Convert between measurement units:
- Centimeters ↔ Meters
- Millimeters ↔ Meters
- Feet ↔ Meters
- Square feet ↔ Square meters

#### `ReportGenerator`
Generate professional reports:
- Project reports (formatted text)
- CSV exports for spreadsheets
- Cost summaries

## Testing

Run the test suite:
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest tests/ --cov=src --cov-report=html
```

## Supported Flooring Types

- Ceramic tiles
- Porcelain tiles
- Natural stone (marble, granite, slate)
- Wooden flooring (parquet, hardwood)
- Laminate
- Vinyl
- Linoleum
- Engineered wood

## Cost Estimation Features

The calculator includes:
- **Material Costs**: Based on unit pricing and quantity
- **Labor Costs**: Per square meter customizable rates
- **Consumables**: Grout, adhesive, sealer costs
- **Additional Costs**: Delivery, prep work, etc.
- **Cost per m²**: Average cost calculation

## Waste Factors

Default waste factors by material type:
- Tiles: 10%
- Wood: 12-15%
- Natural Stone: 12-15%
- Laminate: 10%

Additional pattern-specific waste:
- Straight: 5%
- Diagonal/Herringbone/Chevron: 10-15%
- Complex patterns: 15-20%

## Consumables Estimated

- **Grout**: Variable by pattern (1-2 kg/m²)
- **Adhesive (Thin-set)**: ~1.5 kg/m²
- **Sealer**: ~0.1 liters/m²

## API Documentation

### Key Methods

```python
# Area Calculations
area = AreaCalculator.calculate_room_area(room)
border_area = AreaCalculator.calculate_border_area(room, border_width)

# Waste Calculations
waste, details = WasteCalculator.calculate_waste_quantity(area, material, pattern)
waste_summary = WasteCalculator.get_waste_summary(area, material, pattern)

# Material Requirements
material_info = MaterialCalculator.calculate_material_needed(area, material, pattern)
consumables = MaterialCalculator.calculate_consumables(area, pattern)

# Cost Calculations
material_cost = CostCalculator.calculate_material_cost(area, material, pattern)
total_cost = CostCalculator.calculate_total_project_cost(
    area, material, pattern, labor_cost_per_m2, additional_costs
)

# Reports
report = ReportGenerator.generate_project_report(room_name, calculations)
csv = ReportGenerator.export_to_csv(calculations_list)
```

## Examples

See `main.py` for complete working examples including:
- Living room with ceramic tiles
- Material calculations
- Cost breakdowns
- Report generation

## Future Enhancements

- [ ] Web UI interface
- [ ] 3D visualization of patterns
- [ ] Supplier integration
- [ ] Quote generation
- [ ] Project history tracking
- [ ] Material pricing API
- [ ] Advanced pattern optimization
- [ ] Installation time estimation

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.

## Author

**Flooring Calculator Team**
- Repository: [Refactored-calculus](https://github.com/farirayiinnocent-beep/Refactored-calculus)

## Support

For issues and questions, please create an issue on the GitHub repository.

---

**Last Updated**: November 16, 2025
**Version**: 1.0.0 
