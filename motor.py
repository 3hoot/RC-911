import numpy as np

class Motor:
    def __init__(self, name, kv, no_load_current, resistance, max_power, max_current):
        # Data specified in the datasheet
        self.name = name
        self.kv = kv
        self.no_load_current = no_load_current
        self.resistance = resistance
        self.max_power = max_power
        self.max_current = max_current

        # Calculated data
        self.max_voltage = self.max_power / self.max_current
        self.max_rpm = self.kv * self.max_voltage
        self.max_torque = 60 / (2 * np.pi) * self.max_power / self.max_rpm
        self.rated_torque = self.max_torque * 0.7 # 70% of max torque
        self.rated_rpm = self.max_rpm * (1 - self.rated_torque / self.max_torque)
        self.rated_voltage = self.rated_rpm / self.kv
        self.no_load_efficiency = 1 - self.no_load_current * self.resistance / self.max_voltage
            
    def _argsCheck(self, voltage, current):
        if voltage > self.max_voltage:
            raise ValueError("Voltage exceeds maximum voltage")
        if current > self.max_current:
            raise ValueError("Current exceeds maximum current")

    def getRPM(self, voltage, current = 0):
        self._argsCheck(voltage, current)
        return self.kv * (voltage - current * self.resistance)

    def getTorque(self, voltage, current = 0):
        rpm = self.getRPM(voltage)
        if current == 0:
            power = self.max_power
        else:
            power = voltage * current
        return power / rpm * 60 / (2 * np.pi)
    
    def getTorque(self, voltage, current):
        rpm = self.getRPM(voltage, current)
        power = voltage * current
        return power / rpm * 60 / (2 * np.pi)
