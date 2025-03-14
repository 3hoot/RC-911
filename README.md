# RC-911: Custom 1/16 Scale RC Drift Car

## About This Project
RC-911 is a custom-built 1/16 scale RC drift car, inspired by the Porsche 911 964 Carrera 2 with an RWB body kit. The project also includes a custom standalone RC controller.

This repository serves as a comprehensive database and progress tracker for the project. Here, you'll find analyses of various components, working implementations, and open development tasks. Feel free to explore and use any shared resources.

---

## Features (Planned & Implemented)
- **Brushless motor control** for smooth acceleration and drifting
- **Custom suspension geometry** for realistic handling
- **Wireless communication** using NRF24L01 transceiver modules
- **Optimized power management** for maximum efficiency
- **Addressable LED lights** for enhanced aesthetics
- **Variable ride height system** (planned future upgrade)
- **FPV Camera module** for real-time driving experience (future upgrade)

---

## Project Status: Work in Progress
### 🏎 **RC Car Components**

| Component | Status | Notes |
|-----------|--------|-------|
| **Microcontroller** | ✅ Figured out | Arduino Nano ATmega328P |
| **Brushless Motor** | ⚠️ Needs performance calculations | A2212 BLDC Motor |
| **ESC (Electronic Speed Controller)** | ✅ Figured out | LittleBee ESC 20A + BLHeli Firmware |
| **Battery** | ⚠️ Needs capacity calculation | 2S1P Li-ion/LiPo |
| **Battery Balancer** | ✅ Figured out | Active 2S balancer based on ETA3000 |
| **Battery Monitor** | ❌ Not figured out | Coulomb counting algorithm needed |
| **Current Sensing** | ✅ Figured out | ACS712 module |
| **Voltage Sensing** | ✅ Figured out | Arduino Nano inbuilt ADC |
| **Voltage Converter** | ✅ Figured out | 5V Synchronous Buck Converter |
| **Suspension & Wheels** | ⚠️ Under testing | Custom PETG rims, TPU & PLA tires |
| **Radio Transceiver** | ✅ Figured out | NRF24L01+ 3.3V logic |
| **Servo Control** | ❌ Not figured out | Needs analysis and right motor choice |
| **Lights (LEDs)** | ❌ Not figured out | Needs more research on adressable LEDs |

---

### 🎮 **Standalone RC Controller**
| Component | Status | Notes |
|-----------|--------|-------|
| **Microcontroller** | ✅ Figured out | Arduino Nano ATmega328P |
| **Transceiver** | ✅ Figured out | NRF24L01+ |
| **Throttle & Steering** | ❌ Not figured out | Will use potentiometer and button input, needs figuring out how many inputs |
| **Display Interface** | ❌ Not figured out | Planned for battery status & telemetry |

---

## Next Steps & Future Plans
- 🔧 Implement **battery monitoring** (Coulomb counting algorithm)
- 🎨 Finalize **body shell design** and 3D print components
- 💡 Integrate **addressable LED lighting**
- 🛠 Tune **suspension geometry** for optimal drift performance

---

## Resources & References
- [State-of-Charge Estimation for Batteries](https://www.analog.com/en/resources/technical-articles/a-closer-look-at-state-of-charge-and-state-health-estimation-tech.html)
- [BLHeli ESC Firmware Overview](https://brushlesswhoop.com/dshot-and-bidirectional-dshot/)

