"""
Icon Generator for NOSTROMO

Converts SVG icon to platform-specific formats:
- Windows: .ico (multi-resolution)
- macOS: .icns

Requirements:
    pip install Pillow cairosvg

Usage:
    python generate_icons.py
"""

import io
import struct
from pathlib import Path

try:
    from PIL import Image
    import cairosvg
except ImportError:
    print("Required packages not found. Install with:")
    print("  pip install Pillow cairosvg")
    print("")
    print("On Windows, you may also need:")
    print("  - GTK3 runtime: https://github.com/nicegram/cairosvg-binary/releases")
    print("")
    print("Alternative: Use online converter like https://convertio.co/svg-ico/")
    exit(1)


def svg_to_png(svg_path: Path, size: int) -> bytes:
    """Convert SVG to PNG at specified size."""
    return cairosvg.svg2png(
        url=str(svg_path),
        output_width=size,
        output_height=size,
    )


def create_ico(svg_path: Path, output_path: Path, sizes: list[int] = None):
    """Create Windows .ico file with multiple resolutions."""
    if sizes is None:
        sizes = [16, 24, 32, 48, 64, 128, 256]
    
    images = []
    for size in sizes:
        png_data = svg_to_png(svg_path, size)
        img = Image.open(io.BytesIO(png_data))
        images.append(img)
    
    # Save as ICO
    images[0].save(
        output_path,
        format='ICO',
        sizes=[(img.width, img.height) for img in images],
        append_images=images[1:],
    )
    print(f"Created: {output_path}")


def create_icns(svg_path: Path, output_path: Path):
    """Create macOS .icns file."""
    # ICNS required sizes and their type codes
    icns_sizes = {
        16: b'icp4',    # 16x16
        32: b'icp5',    # 32x32
        64: b'icp6',    # 64x64
        128: b'ic07',   # 128x128
        256: b'ic08',   # 256x256
        512: b'ic09',   # 512x512
        1024: b'ic10',  # 1024x1024
    }
    
    # For simplicity, use PNG-in-ICNS format (modern macOS)
    icon_data = bytearray()
    
    for size, type_code in icns_sizes.items():
        try:
            png_data = svg_to_png(svg_path, size)
            
            # ICNS entry: type (4 bytes) + length (4 bytes) + data
            entry_length = 8 + len(png_data)
            icon_data.extend(type_code)
            icon_data.extend(struct.pack('>I', entry_length))
            icon_data.extend(png_data)
        except Exception as e:
            print(f"  Warning: Could not create {size}x{size}: {e}")
    
    # ICNS header: 'icns' + total length
    total_length = 8 + len(icon_data)
    
    with open(output_path, 'wb') as f:
        f.write(b'icns')
        f.write(struct.pack('>I', total_length))
        f.write(icon_data)
    
    print(f"Created: {output_path}")


def create_png_set(svg_path: Path, output_dir: Path):
    """Create PNG files at various sizes for other uses."""
    sizes = [16, 32, 48, 64, 128, 256, 512]
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for size in sizes:
        png_data = svg_to_png(svg_path, size)
        output_path = output_dir / f"nostromo-{size}.png"
        with open(output_path, 'wb') as f:
            f.write(png_data)
        print(f"Created: {output_path}")


def main():
    # Paths
    script_dir = Path(__file__).parent
    svg_path = script_dir / "icons" / "nostromo.svg"
    
    if not svg_path.exists():
        print(f"SVG not found: {svg_path}")
        return
    
    print("Generating NOSTROMO icons...")
    print(f"Source: {svg_path}")
    print("")
    
    # Create Windows ICO
    ico_path = script_dir / "windows" / "nostromo.ico"
    ico_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        create_ico(svg_path, ico_path)
    except Exception as e:
        print(f"Failed to create ICO: {e}")
    
    # Create macOS ICNS
    icns_path = script_dir / "macos" / "nostromo.icns"
    icns_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        create_icns(svg_path, icns_path)
    except Exception as e:
        print(f"Failed to create ICNS: {e}")
    
    # Create PNG set
    png_dir = script_dir / "icons" / "png"
    try:
        create_png_set(svg_path, png_dir)
    except Exception as e:
        print(f"Failed to create PNGs: {e}")
    
    print("")
    print("Done! Icons generated successfully.")
    print("")
    print("Manual alternatives if generation failed:")
    print("  - https://convertio.co/svg-ico/")
    print("  - https://cloudconvert.com/svg-to-icns")
    print("  - https://icoconvert.com/")


if __name__ == "__main__":
    main()
