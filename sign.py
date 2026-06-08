import hashlib
import struct
import sys

IMAGE_MAGIC = 0xDEADFEED
FW_VERSION = 123

# Size of application slot (excluding header)
APP_SLOT_SIZE = 975 * 1024

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input.bin> <output.bin>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Read application image
with open(input_file, "rb") as f:
    app_data = f.read()

app_size = len(app_data)

if app_size > APP_SLOT_SIZE:
    raise ValueError(
        f"Application size ({app_size}) exceeds slot size ({APP_SLOT_SIZE})"
    )

# Pad remaining bytes with 0xFF
padded_app = app_data + bytes([0xFF]) * (APP_SLOT_SIZE - app_size)

# Compute SHA256 over padded application image
sha256_hash = hashlib.sha256(padded_app).digest()

# Build image header
header = struct.pack(
    "<III32s",
    IMAGE_MAGIC,
    FW_VERSION,
    app_size,
    sha256_hash
)

padding_size = 256 - len(header)
header_padding = bytes([0xFF] * padding_size)

print(f"Magic     : 0x{IMAGE_MAGIC:08X}")
print(f"FW Version: {FW_VERSION}")
print(f"App Size  : {app_size} bytes")
print(f"SHA256    : {sha256_hash.hex()}")

# Write header + padded application
with open(output_file, "wb") as f:
    f.write(header)
    f.write(header_padding)
    f.write(padded_app)

print(f"Created image: {output_file}")
print(f"Total size   : {len(header) + len(padded_app)} bytes")
