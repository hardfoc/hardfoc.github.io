# Flux V1 valve controller

From a new Flux V1 board to its examples running, and where to read next.

<div class="hf-chip hf-chip--board" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Valve controller board</span>
<span class="hf-chip__name">Flux V1</span>
<span class="hf-chip__vendor">HardFOC</span>
</div>

MCU
:   ESP32-S3

Solenoid drivers
:   TLE92466ED (six low-side channels), MAX22200 (eight channels)

Valves
:   On/off and proportional solenoid channels

Firmware
:   ESP-IDF 5.5, FreeRTOS, C++
</div>

## Path

<div class="hf-steps" markdown>

1. **Bring the board up with the HAL.** The [HAL quickstart](https://hardfoc.github.io/hf-hal-flux-v1/latest/quickstart/)
   installs ESP-IDF, builds an example and reads its log.
2. **Check the hardware.** The [pin map](https://hardfoc.github.io/hf-hal-flux-v1/latest/hardware/pin-map/) and the
   [bring-up guide](https://hardfoc.github.io/hf-hal-flux-v1/latest/bring-up/).
3. **Drive the valves.** The [ValveManager](https://hardfoc.github.io/hf-hal-flux-v1/latest/managers/valves/) page
   and the examples.

</div>

The product firmware, `hardfoc-flux-v1`, is a private repository. Its documentation is built in CI as an artifact
for people with access, and is not published here.

## Documentation

| Site | What it covers |
| --- | --- |
| [hf-hal-flux-v1](https://hardfoc.github.io/hf-hal-flux-v1/latest/) | The board: hardware, pin map, managers (valves, ADC, GPIO, LEDs, temperature, NVS, comms), examples |
| [hf-tle92466ed-driver](https://hardfoc.github.io/hf-tle92466ed-driver/latest/) | The six-channel solenoid driver |
| [hf-max22200-driver](https://hardfoc.github.io/hf-max22200-driver/latest/) | The eight-channel solenoid driver |
| [hf-core](https://hardfoc.github.io/hf-core/latest/) | The shared core the HAL is built on |
