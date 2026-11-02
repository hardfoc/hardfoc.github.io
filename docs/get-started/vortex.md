# Vortex V1 motor controller

From a new Vortex V1 board to the product firmware running, and where to read next.

<div class="hf-chip hf-chip--board" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Motor controller board</span>
<span class="hf-chip__name">Vortex V1</span>
<span class="hf-chip__vendor">HardFOC</span>
</div>

MCU
:   ESP32-C6

Motor control
:   TMC9660 smart gate driver, FOC on chip

Feedback
:   AS5047U magnetic encoder

Field bus
:   CAN, CANopen node in the product firmware

Firmware
:   ESP-IDF 5.5, FreeRTOS, C++
</div>

## Path

<div class="hf-steps" markdown>

1. **Bring the board up with the HAL.** The HAL's quickstart installs ESP-IDF, builds an example and reads its
   log, one step at a time: [HAL quickstart](https://hardfoc.github.io/hf-hal-vortex-v1/latest/quickstart/).
2. **Check the hardware.** The [pin map](https://hardfoc.github.io/hf-hal-vortex-v1/latest/hardware/pin-map/) and
   the [bring-up guide](https://hardfoc.github.io/hf-hal-vortex-v1/latest/bring-up/) list every signal and what to
   check first.
3. **Build and flash the product firmware.** The
   [getting-started page](https://hardfoc.github.io/hardfoc-vortex-v1/latest/getting-started/) of
   `hardfoc-vortex-v1` builds with the pinned ESP-IDF and explains the boot log.
4. **Talk to it over CAN.** [CANopen](https://hardfoc.github.io/hardfoc-vortex-v1/latest/canopen/) and the
   [object dictionary](https://hardfoc.github.io/hardfoc-vortex-v1/latest/od-reference/).

</div>

## Documentation

| Site | What it covers |
| --- | --- |
| [hardfoc-vortex-v1](https://hardfoc.github.io/hardfoc-vortex-v1/latest/) | The product: architecture, threads, safety, boot and updates, CANopen, configuration, design notes |
| [hf-hal-vortex-v1](https://hardfoc.github.io/hf-hal-vortex-v1/latest/) | The board: hardware, pin map, managers (motor, encoder, IMU, ADC, LEDs, temperature, NVS, comms), examples |
| [hf-tmc9660-driver](https://hardfoc.github.io/hf-tmc9660-driver/latest/) | The motor controller chip: bootloader, FOC, telemetry |
| [hf-as5047u-driver](https://hardfoc.github.io/hf-as5047u-driver/latest/) | The encoder |
| [hf-core](https://hardfoc.github.io/hf-core/latest/) | The shared core the HAL is built on |
