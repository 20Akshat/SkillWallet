"""
Utility to generate realistic test sample images for PPE inspection and Crack Diagnostics
so that evaluators can run the Streamlit app seamlessly without needing external files.
"""
from PIL import Image, ImageDraw, ImageFilter
import os

def create_sample_ppe_image(filepath="sample_ppe.jpg"):
    # Create a 640x480 image representing a construction site
    img = Image.new("RGB", (640, 480), color=(140, 160, 180)) # Sky background
    draw = ImageDraw.Draw(img)
    
    # Construction structure / concrete slab
    draw.rectangle([0, 240, 640, 480], fill=(110, 115, 120)) # Concrete floor
    draw.rectangle([40, 80, 200, 480], fill=(70, 75, 80)) # Concrete pillar 1
    draw.rectangle([440, 80, 600, 480], fill=(70, 75, 80)) # Concrete pillar 2
    
    # Scaffolding lines (steel tubes)
    for y in range(100, 400, 60):
        draw.line([(0, y), (640, y)], fill=(180, 190, 200), width=4)
    for x in range(60, 600, 120):
        draw.line([(x, 50), (x, 480)], fill=(180, 190, 200), width=4)
        draw.line([(x, 50), (x+120, 250)], fill=(160, 170, 180), width=2)
        draw.line([(x+120, 50), (x, 250)], fill=(160, 170, 180), width=2)

    # Worker 1: Fully Compliant (Hard Hat, High-Vis Vest, Boots)
    # Head & Yellow Helmet
    draw.ellipse([270, 190, 310, 230], fill=(235, 180, 140)) # Face
    draw.chord([265, 180, 315, 215], 180, 360, fill=(255, 215, 0), outline=(200, 160, 0), width=2) # Yellow Hardhat
    # Body with Fluorescent Orange/Neon High-Vis Vest
    draw.rectangle([260, 230, 320, 330], fill=(255, 102, 0)) # High-vis orange
    draw.rectangle([275, 240, 305, 330], fill=(220, 255, 50)) # Neon yellow reflective strip
    draw.line([(260, 270), (320, 270)], fill=(240, 240, 240), width=6) # Reflective band
    # Legs (Work Jeans) & Steel-Toe Boots
    draw.rectangle([265, 330, 288, 420], fill=(40, 60, 100)) # Left leg
    draw.rectangle([292, 330, 315, 420], fill=(40, 60, 100)) # Right leg
    draw.rectangle([260, 420, 290, 440], fill=(30, 20, 15)) # Steel-toe boot left
    draw.rectangle([292, 420, 322, 440], fill=(30, 20, 15)) # Steel-toe boot right
    
    # Worker 2: Partial Violation (No Helmet, Normal Clothes near edge)
    draw.ellipse([370, 220, 400, 250], fill=(220, 170, 130)) # Head (Hair only, NO HELMET)
    draw.arc([370, 215, 400, 235], 180, 360, fill=(30, 20, 10), width=5) # Dark hair
    draw.rectangle([365, 250, 405, 340], fill=(60, 80, 120)) # Regular blue shirt (NO HIGH-VIS VEST)
    draw.rectangle([370, 340, 385, 420], fill=(50, 50, 50)) # Dark trousers
    draw.rectangle([390, 340, 405, 420], fill=(50, 50, 50))
    draw.rectangle([367, 420, 387, 435], fill=(200, 200, 200)) # Sneakers (NON-SAFETY FOOTWEAR)
    draw.rectangle([390, 420, 410, 435], fill=(200, 200, 200))
    
    # Danger warning sign on pillar
    draw.rectangle([70, 160, 170, 230], fill=(255, 255, 255), outline=(200, 0, 0), width=3)
    draw.polygon([(120, 170), (85, 220), (155, 220)], fill=(255, 200, 0), outline=(0, 0, 0))
    draw.text((100, 218), "CAUTION", fill=(200, 0, 0))
    
    img.save(filepath, quality=90)
    print(f"Saved {filepath}")

def create_sample_crack_image(filepath="sample_crack.jpg"):
    # Create concrete texture image
    img = Image.new("RGB", (640, 480), color=(185, 185, 180))
    draw = ImageDraw.Draw(img)
    
    # Draw concrete surface mottling / roughness
    import random
    random.seed(42)
    for _ in range(5000):
        x = random.randint(0, 639)
        y = random.randint(0, 479)
        shade = random.randint(140, 210)
        draw.point((x, y), fill=(shade, shade, shade))
        
    # Draw a 45-degree Structural Shear Crack across RCC Beam/Column junction
    # Main crack path with jagged offsets
    pts = [
        (120, 60), (145, 95), (170, 130), (195, 175), (230, 210),
        (270, 255), (320, 290), (370, 335), (420, 370), (480, 410), (530, 440)
    ]
    # Draw secondary spalling and crack line
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i+1]
        # Main deep fissure
        draw.line([(x1, y1), (x2, y2)], fill=(35, 30, 25), width=6)
        # Inner dark core
        draw.line([(x1, y1), (x2, y2)], fill=(15, 12, 10), width=3)
        # Concrete flaking / spalling edges
        draw.ellipse([x1-4, y1-3, x1+6, y1+5], fill=(120, 115, 110))
        # Branch hairline cracks
        if i % 2 == 1:
            draw.line([(x1, y1), (x1 + random.randint(-25, 25), y1 + random.randint(15, 35))], fill=(80, 75, 70), width=2)
            
    # Draw a measurement scale / gauge reference for engineering context
    draw.rectangle([50, 400, 150, 450], fill=(245, 245, 240), outline=(0, 0, 0), width=2)
    draw.text((60, 410), "SCALE: 10mm", fill=(0, 0, 0))
    for t in range(55, 145, 10):
        draw.line([(t, 430), (t, 445)], fill=(0, 0, 0), width=1)
        
    img.save(filepath, quality=90)
    print(f"Saved {filepath}")

if __name__ == "__main__":
    create_sample_ppe_image()
    create_sample_crack_image()
