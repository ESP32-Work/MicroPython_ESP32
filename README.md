# Wokwi MicroPython Project

This project demonstrates how to use Wokwi with VSCode for MicroPython programming, specifically for an ESP32 microcontroller. It includes a simple example that toggles an LED when a button is pressed.

## Project Structure

- `main.py`: The main MicroPython script that runs on the ESP32.
- `diagram.json`: Wokwi diagram file that describes the hardware setup.
- `wokwi.toml`: Configuration file for the Wokwi simulator.
- `ESP32_GENERIC_S3-20240602-v1.22.1.bin`: ESP32 firmware file (you need to download this separately).

## Prerequisites

To use this project, you'll need:

1. Visual Studio Code
2. Wokwi extension for VSCode
3. A Wokwi license (30-day free trial available)
4. Python and pip installed on your system

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/ESP32-Work/MicroPython_ESP32
   cd MicroPython_ESP32/Led\ Blink/
   ```

2. Install the Wokwi extension in VSCode.

3. Install `mpremote`:
   ```
   pip install mpremote
   ```

4. Download the ESP32 firmware file (`ESP32_GENERIC_S3-20240602-v1.22.1.bin`) and place it in the project root.

## Usage

1. Open the project folder in VSCode.

2. Open the `diagram.json` file and click on "Run Simulation" to start the Wokwi simulator.

3. Then upload the code remotely:
   ```
   python -m mpremote connect port:rfc2217://localhost:4000 run main.py
   ```

4. In the simulation, press the button to toggle the LED on and off.

## Video

![Screencastfrom09-15-2024123340AM-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/c5ad02a3-7214-4246-be3c-92cbe7e62c2b)

## Customization

- Modify `main.py` to change the behavior of the MicroPython program.
- Edit `diagram.json` to change the hardware configuration.
- Update `wokwi.toml` if you need to change the firmware file or server port.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- Thanks to Wokwi for providing the simulation platform.
- MicroPython for enabling Python on microcontrollers.