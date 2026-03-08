import json
import os
import datetime
from PIL import Image
import pytesseract

# ── Windows users: uncomment and set your tesseract path ──
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ACCEPTED_TYPES = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.tif', '.webp')

# ── Folder paths ──
IMAGES_FOLDER = "images"
JSON_FOLDER = "json"

# ── Make sure json folder exists ──
os.makedirs(JSON_FOLDER, exist_ok=True)

# ── Check images folder exists ──
if not os.path.exists(IMAGES_FOLDER):
    print(f"❌ '{IMAGES_FOLDER}' folder not found. Please create it and add images.")
    exit()

# ── Get all valid image files ──
image_files = [f for f in os.listdir(IMAGES_FOLDER) if f.lower().endswith(ACCEPTED_TYPES)]

if not image_files:
    print(f"❌ No images found in '{IMAGES_FOLDER}' folder.")
    exit()

print(f"📁 Found {len(image_files)} image(s). Processing...\n")

results = {}

for filename in image_files:
    image_path = os.path.join(IMAGES_FOLDER, filename)
    ext = os.path.splitext(filename)[1].lower()

    try:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image).strip()

        results[filename] = {
            "status": "success",
            "filename": filename,
            "file_type": ext,
            "image_size": {
                "width": image.width,
                "height": image.height
            },
            "mode": image.mode,
            "extracted_text": extracted_text,
            "word_count": len(extracted_text.split()) if extracted_text else 0,
            "character_count": len(extracted_text),
            "timestamp": datetime.datetime.now().isoformat()
        }
        print(f"  ✅ {filename}")

    except Exception as e:
        results[filename] = {
            "status": "error",
            "filename": filename,
            "message": str(e)
        }
        print(f"  ❌ {filename} — {str(e)}")

# ── Save JSON output ──
output_filename = f"extracted_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
output_path = os.path.join(JSON_FOLDER, output_filename)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print(f"\n✅ Done! JSON saved to: {output_path}")
