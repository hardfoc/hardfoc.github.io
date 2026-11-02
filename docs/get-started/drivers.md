# A chip driver on your MCU

Use one HardFOC chip driver in your own firmware, on any MCU, without the rest of HardFOC.

Every `hf-*-driver` repository is a C++ library with no platform code. The driver is a class template over a small
communication interface: you write one class that moves bytes over the bus (SPI, I2C or UART) and toggles the
chip's control pins, and the driver does the rest. Each one ships ESP32 examples that build in CI.

## Path

<div class="hf-steps" markdown>

1. **Find the chip** in the [catalogue](../repositories.md?topic=driver) (filter by bus: `spi`, `i2c`, `uart`).
2. **Read its quickstart**: wiring, the port class and a short example, compiled in CI. For example, the
   [TMC9660 quickstart](https://hardfoc.github.io/hf-tmc9660-driver/latest/quickstart/).
3. **Add it as a submodule** and link its CMake target, or add it as an ESP-IDF component.
4. **Write the port** for your MCU, following the driver's porting page, and run the example.

</div>

## What every driver has

| Page | What it covers |
| --- | --- |
| Quickstart | Wiring, the port, a short example, "if it does not work" |
| Hardware | Pins, bus settings and timing, power, errata |
| Porting | The interface methods and their contracts |
| API guide and reference | Task-oriented guide, and Doxygen under `api/` |
| Examples | The ESP32 examples and what each one shows |
