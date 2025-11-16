"""Unit conversion utilities"""


class UnitConverter:
    """Convert between different measurement units"""
    
    @staticmethod
    def cm_to_m(cm: float) -> float:
        """Convert centimeters to meters"""
        return cm / 100
    
    @staticmethod
    def m_to_cm(m: float) -> float:
        """Convert meters to centimeters"""
        return m * 100
    
    @staticmethod
    def mm_to_m(mm: float) -> float:
        """Convert millimeters to meters"""
        return mm / 1000
    
    @staticmethod
    def m_to_mm(m: float) -> float:
        """Convert meters to millimeters"""
        return m * 1000
    
    @staticmethod
    def ft_to_m(ft: float) -> float:
        """Convert feet to meters"""
        return ft * 0.3048
    
    @staticmethod
    def m_to_ft(m: float) -> float:
        """Convert meters to feet"""
        return m / 0.3048
    
    @staticmethod
    def sq_ft_to_sq_m(sq_ft: float) -> float:
        """Convert square feet to square meters"""
        return sq_ft * 0.092903
    
    @staticmethod
    def sq_m_to_sq_ft(sq_m: float) -> float:
        """Convert square meters to square feet"""
        return sq_m / 0.092903
