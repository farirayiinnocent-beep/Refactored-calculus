"""Generate reports for flooring projects"""

from typing import Dict, Any
from datetime import datetime


class ReportGenerator:
    """Generate comprehensive project reports"""
    
    @staticmethod
    def generate_project_report(room_name: str, calculations: Dict[str, Any]) -> str:
        """Generate a formatted project report"""
        report = f"""
╔════════════════════════════════════════════════════════════════╗
║               FLOORING PROJECT REPORT                          ║
╚════════════════════════════════════════════════════════════════╝

PROJECT DETAILS
───────────────────────────────────────────────────────────────
Room: {room_name}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

ROOM SPECIFICATIONS
───────────────────────────────────────────────────────────────
Area: {calculations.get('area_m2', 0):.2f} m²

MATERIAL INFORMATION
───────────────────────────────────────────────────────────────
Material: {calculations.get('material_name', 'N/A')}
Quantity Needed: {calculations.get('quantity_units', 0):.2f} {calculations.get('unit_measurement', 'units')}
Waste Factor: {calculations.get('waste_percent', 0):.1f}%

LAYING PATTERN
───────────────────────────────────────────────────────────────
Pattern: {calculations.get('pattern_name', 'N/A')}
Description: {calculations.get('pattern_description', 'N/A')}

COST BREAKDOWN
───────────────────────────────────────────────────────────────
Material Cost: €{calculations.get('material_cost', 0):.2f}
Labor Cost: €{calculations.get('labor_cost', 0):.2f}
Consumables Cost: €{calculations.get('consumable_cost', 0):.2f}
───────────────────────────────────────────────────────────────
TOTAL PROJECT COST: €{calculations.get('total_cost', 0):.2f}
Cost per m²: €{calculations.get('cost_per_m2', 0):.2f}

════════════════════════════════════════════════════════════════
"""
        return report
    
    @staticmethod
    def export_to_csv(calculations_list: list) -> str:
        """Export multiple calculations to CSV format"""
        csv = "Room,Area_m2,Material,Quantity,Waste%,Total_Cost,Cost_per_m2\n"
        for calc in calculations_list:
            csv += f"{calc.get('room_name', 'N/A')},{calc.get('area_m2', 0):.2f},"
            csv += f"{calc.get('material_name', 'N/A')},{calc.get('quantity_units', 0):.2f},"
            csv += f"{calc.get('waste_percent', 0):.1f},{calc.get('total_cost', 0):.2f},"
            csv += f"{calc.get('cost_per_m2', 0):.2f}\n"
        return csv
