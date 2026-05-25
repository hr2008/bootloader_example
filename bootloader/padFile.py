#!/usr/bin/env python3

import sys
from pathlib import Path

BOOTLOADER_SIZE = 0x8000

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <bootloader_bin>")
    sys.exit(1)

bootloader_file = Path(sys.argv[1])

if not bootloader_file.is_file():
    print(f"Error: File not found: {bootloader_file}")
    sys.exit(1)

with open(bootloader_file, "rb") as f:
    file_data = f.read()

if len(file_data) > BOOTLOADER_SIZE:
    print(
        f"Error: File size ({len(file_data)} bytes) exceeds "
        f"BOOTLOADER_SIZE ({BOOTLOADER_SIZE} bytes)"
    )
    sys.exit(1)

padding_size = BOOTLOADER_SIZE - len(file_data)
padding = bytes([0xFF] * padding_size)

with open(bootloader_file, "wb") as f:
    f.write(file_data)
    f.write(padding)

print(
    f"Padded {bootloader_file} to "
    f"{BOOTLOADER_SIZE} bytes with 0xFF"
)
