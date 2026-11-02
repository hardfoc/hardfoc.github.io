"""The four layers of HardFOC firmware: chip drivers, core, board HALs, products.

Reads: From bottom to top, each layer builds on the one below it as a Git submodule pinned to a commit or tag.
Chip drivers are hardware-agnostic C++ libraries with no platform code; each one needs only a small bus adapter.
hf-core gathers them with the peripheral interface wrap, the pin configuration and the utility libraries
(RTOS wrappers, general helpers, CANopen). A board HAL builds one object per board from hf-core, with one manager
per board function. A product is the application firmware for one board, on top of its HAL.
"""

from hardfoc_mkdocs_theme.figkit import Fig

SOURCES = ["mkdocs.yml"]


def build(_data):
    f = Fig(
        "hardfoc-layers",
        "Four layers, each a set of repositories",
        alt="Layer diagram, top to bottom: products (hardfoc-vortex-v1, hardfoc-flux-v1) build on board HALs "
        "(hf-hal-vortex-v1, hf-hal-flux-v1), which build on hf-core (hf-core-drivers and hf-core-utils), which "
        "gathers the hardware-agnostic chip drivers (hf-*-driver) and the peripheral interface wrap.",
        width=1200,
        kicker="Architecture",
        subtitle="Each layer is a Git submodule of the one above it, pinned to a commit or tag.",
        profile="overview",
        legend=[("teal", "application firmware"), ("brand", "board and platform"), ("slate", "portable libraries")],
    )
    W = f.body_w
    gap = 24
    half = (W - gap) / 2
    third = (W - 2 * gap) / 3
    vortex = f.card(0, 0, half, "hardfoc-vortex-v1", ["Vortex V1 motor controller firmware"], tone="teal", accent=True)
    flux = f.card(half + gap, 0, half, "hardfoc-flux-v1", ["Flux V1 valve controller firmware"], tone="teal",
                  accent=True, h=vortex.h)
    y = vortex.b + 48
    hv = f.card(0, y, half, "hf-hal-vortex-v1", ["ESP32-C6, TMC9660, AS5047U"], tone="brand")
    hfx = f.card(half + gap, y, half, "hf-hal-flux-v1", ["ESP32-S3, MAX22200, TLE92466ED"], tone="brand", h=hv.h)
    y = hv.b + 48
    core = f.card(0, y, W, "hf-core", ["hf-core-drivers + hf-core-utils: device handlers, RTOS, CANopen"],
                  tone="brand", accent=True)
    y = core.b + 48
    drv = f.card(0, y, third, "Chip drivers", ["hf-*-driver, no platform code"], tone="slate")
    wrap = f.card(third + gap, y, third, "Interface wrap", ["hf-internal-interface-wrap, hf-pincfg"], tone="slate")
    utils = f.card(2 * (third + gap), y, third, "Utilities", ["hf-utils-general, hf-utils-rtos-wrap, hf-utils-canopen"], tone="slate")
    for a, b in ((vortex, hv), (flux, hfx)):
        f.connect(a, b, "bottom", "top", tone="rail")
    # Straight arrows: each one leaves and enters at the same x.
    for hal in (hv, hfx):
        f.connect(hal, core, "bottom", "top", bt=(hal.cx - core.x) / core.w, tone="rail")
    for b in (drv, wrap, utils):
        f.connect(core, b, "bottom", "top", at=(b.cx - core.x) / core.w, tone="rail")
    return f
