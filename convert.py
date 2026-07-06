import os
from PIL import Image
import glob

folder = r"Store\Trees"
png_files = glob.glob(os.path.join(folder, "*.png"))

for png_path in png_files:
    # Open image
    img = Image.open(png_path)
    
    # Save as webp
    webp_path = os.path.splitext(png_path)[0] + ".webp"
    
    # We use a quality setting of 80 which usually provides excellent compression with virtually no visual quality loss
    img.save(webp_path, "webp", quality=80)
    print(f"Converted {png_path} to {webp_path}")
    
    # Remove original png
    os.remove(png_path)
    print(f"Deleted {png_path}")

print("All files converted successfully!")
