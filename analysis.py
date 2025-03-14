import numpy as np
import json as js
import matplotlib.pyplot as plt
from motor import Motor

# Global variables
MOTOR_DATA_PATH = "data/motors.json"
WHEEL_DIAMETER = 0.04  # 4 cm
WHEEL_SPEED = 20       # m/s
WHEEL_RPM = WHEEL_SPEED / (np.pi * WHEEL_DIAMETER) * 60 

def getMotorData(path):
    """Returns a dictionary of motor data from a json file"""
    with open(path) as file:
        data = js.load(file)
        motors = []
        for motor_data in data:
            motor = Motor(
                name=motor_data['family']+' '+str(motor_data['kv']), 
                kv=motor_data['kv'], 
                no_load_current=motor_data['noLoadCurrent'], 
                resistance=motor_data['resistance'], 
                max_power=motor_data['maxPower'], 
                max_current=motor_data['maxCurrent']
                )
            motors.append(motor)
        return motors
    
def main():
    motors = getMotorData(MOTOR_DATA_PATH)
    
    colormap = plt.cm.get_cmap('tab10')  # Use a predefined colormap
    num_motors = len(motors)
    
    # Plot the torque vs RPM for each motor
    plt.figure(1)
    for i, motor in enumerate(motors):
        color = colormap(i % num_motors)  # Get a color from the colormap
        plt.plot([0, motor.max_rpm], [motor.max_torque, 0], label=motor.name, color=color)
        plt.plot([0, motor.rated_rpm], [motor.rated_torque, motor.rated_torque], linestyle='--', color=color)
        plt.plot([motor.rated_rpm, motor.rated_rpm], [0, motor.rated_torque], linestyle='--', color=color)
    
    plt.plot([WHEEL_RPM, WHEEL_RPM], [0, motors[0].max_torque], label='Wheel RPM', color='black')

    plt.xlabel('RPM')
    plt.ylabel('Torque (Nm)')
    plt.title('Motor Torque vs RPM')
    plt.grid(True)
    plt.legend()

    # Find most suitable gear ratio for each motor at rated RPM
    gear_ratios = []
    for motor in motors:
        gear_ratios.append(WHEEL_RPM / motor.rated_rpm)

    # Plot the torque vs RPM for each motor with suitable gear ratios
    plt.figure(2)
    for i, motor in enumerate(motors):
        color = colormap(i % num_motors)  # Get a color from the colormap
        geared_max_torque = motor.max_torque / gear_ratios[i]
        geared_rated_torque = motor.rated_torque / gear_ratios[i]
        plt.plot([0, motor.max_rpm * gear_ratios[i]], [geared_max_torque, 0], label=f"{motor.name} {gear_ratios[i]:.3f}", color=color)
        plt.plot([0, motor.rated_rpm * gear_ratios[i]], [geared_rated_torque, geared_rated_torque], linestyle='--', color=color)
        plt.plot([motor.rated_rpm * gear_ratios[i], motor.rated_rpm * gear_ratios[i]], [0, geared_rated_torque], linestyle='--', color=color)

    plt.plot([WHEEL_RPM, WHEEL_RPM], [0, motors[0].max_torque], label='Wheel RPM', color='black')

    plt.xlabel('RPM')
    plt.ylabel('Torque (Nm)')
    plt.title('Motor Torque vs RPM at Suitable Gear Ratio')
    plt.grid(True)
    plt.legend()
    
    plt.show()

if __name__ == "__main__":
    main()
