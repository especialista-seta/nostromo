#!/usr/bin/env python3
"""Generate icon files from nostromo.jpg."""

from pathlib import Path
from PIL import Image

def main():
    # Get paths
    project_root = Path(__file__).parent.parent
    source_img = project_root / "nostromo.jpg"
    build_dir = project_root / "build"
    
    # Load and convert to RGBA
    img = Image.open(source_img)
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    
    print(f"Loaded: {source_img} ({img.size})")
    
    # Create Windows ICO
    windows_dir = build_dir / "windows"
    windows_dir.mkdir(parents=True, exist_ok=True)
    
    ico_sizes = [16, 24, 32, 48, 64, 128, 256]
    ico_images = [img.resize((s, s), Image.Resampling.LANCZOS) for s in ico_sizes]
    
    ico_path = windows_dir / "nostromo.ico"
    ico_images[0].save(
        ico_path,
        format="ICO",
        sizes=[(s, s) for s in ico_sizes],
        append_images=ico_images[1:]
    )
    print(f"Created: {ico_path}")
    
    # Create Windows Installer wizard images (BMP format)
    # WizardImageFile: 164x314 pixels (left side banner)
    wizard_img = img.resize((164, 164), Image.Resampling.LANCZOS)
    # Create a 164x314 image with the icon centered vertically
    wizard_banner = Image.new("RGB", (164, 314), (0, 32, 0))  # Dark green background
    wizard_banner.paste(wizard_img.convert("RGB"), (0, 75))
    wizard_path = windows_dir / "wizard.bmp"
    wizard_banner.save(wizard_path, format="BMP")
    print(f"Created: {wizard_path}")
    
    # WizardSmallImageFile: 55x55 pixels (top right corner)
    wizard_small = img.resize((55, 55), Image.Resampling.LANCZOS)
    wizard_small_path = windows_dir / "wizard-small.bmp"
    wizard_small.convert("RGB").save(wizard_small_path, format="BMP")
    print(f"Created: {wizard_small_path}")
    
    # Create PNG versions
    png_dir = build_dir / "icons" / "png"
    png_dir.mkdir(parents=True, exist_ok=True)
    
    for size in [16, 32, 64, 128, 256, 512]:
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        png_path = png_dir / f"nostromo-{size}.png"
        resized.save(png_path, format="PNG")
        print(f"Created: {png_path}")
    
    # Create macOS iconset
    iconset_dir = build_dir / "macos" / "nostromo.iconset"
    iconset_dir.mkdir(parents=True, exist_ok=True)
    
    macos_sizes = [
        (16, "16x16"),
        (32, "16x16@2x"),
        (32, "32x32"),
        (64, "32x32@2x"),
        (128, "128x128"),
        (256, "128x128@2x"),
        (256, "256x256"),
        (512, "256x256@2x"),
        (512, "512x512"),
        (1024, "512x512@2x"),
    ]
    
    for size, name in macos_sizes:
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        icon_path = iconset_dir / f"icon_{name}.png"
        resized.save(icon_path, format="PNG")
        print(f"Created: {icon_path}")
    
    print("\nAll icons generated successfully!")
    print("\nNote: To create .icns on macOS, run:")
    print("  iconutil -c icns build/macos/nostromo.iconset")


if __name__ == "__main__":
    main()
