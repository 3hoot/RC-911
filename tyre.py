class FrictionCoeffs:
    """Friction coefficients for different surfaces, 
    currently returns a range of values for each surface regardless of tyre parameters"""
    
    @staticmethod
    def tpu_asphalt(velocity, tread_width, tread_type):
        # space for future calculations based on gathered data
        return range(0.6, 0.9, 0.1)

    @staticmethod
    def tpu_concrete(velocity, tread_width, tread_type):
        # space for future calculations based on gathered data
        return range(0.6, 0.8, 0.1)
    
    @staticmethod
    def tpu_carpet(velocity, tread_width, tread_type):
        # space for future calculations based on gathered data
        return range(0.7, 1, 0.1)

    @staticmethod
    def pla_asphalt(velocity, tread_width, tread_type):
        # space for future calculations based on gathered data
        return range(0.3, 0.5, 0.1)
    
    @staticmethod
    def pla_concrete(velocity, tread_width, tread_type):
        # space for future calculations based gathered data
        return range(0.2, 0.4, 0.1)
    
    @staticmethod
    def pla_carpet(velocity, tread_width, tread_type):
        # space for future calculations based on gathered data
        return range(0.4, 0.6, 0.1)
