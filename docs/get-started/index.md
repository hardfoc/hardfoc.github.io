# Get started

Pick the path that matches what you have on the bench: a HardFOC board, or a chip and your own MCU.

| You have | Start with | Then |
| --- | --- | --- |
| A Vortex V1 motor controller | [Vortex V1](vortex.md): flash a HAL example, then the product firmware | CANopen, configuration, the HAL managers |
| A Flux V1 valve controller | [Flux V1](flux.md): flash a HAL example | The valve and ADC managers |
| A chip from the driver list and any MCU | [A chip driver on your MCU](drivers.md) | The driver's own quickstart and porting guide |

Every path needs the same tools:

| Tool | Version | Notes |
| --- | --- | --- |
| ESP-IDF | 5.5 | The boards' firmware and the ESP32 examples; each repository says which release it pins |
| Git | with submodules | Every layer is a submodule of the one above it |
| A C++ compiler | C++17 or C++20, as the repository says | For a driver on another MCU, your own toolchain |
| Python 3 | 3.10 or newer | Only to build documentation locally |

!!! warning "Power"
    Bring a new board up on a current-limited bench supply, with the motor or valves unloaded.
