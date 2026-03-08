import json
import os
import csv
import datetime
from PIL import Image
import pytesseract

# ── Windows users: uncomment and set your tesseract path ──
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ACCEPTED_TYPES = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.tif', '.webp')

# ── Folder paths ──
IMAGES_FOLDER = "images"
OUTPUT_FOLDER = "output"

# ── Ask user for output format ──
print("📄 Select output format:")
print("  1. JSON")
print("  2. TXT")
print("  3. CSV")

while True:
    choice = input("\nEnter 1, 2, or 3: ").strip()
    if choice == "1":
        output_format = "json"
        break
    elif choice == "2":
        output_format = "txt"
        break
    elif choice == "3":
        output_format = "csv"
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")

print(f"\n✅ Output format selected: {output_format.upper()}\n")

# ── Make sure output folder exists ──
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

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

# ── Save output in chosen format ──
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
output_filename = f"extracted_{timestamp}.{output_format}"
output_path = os.path.join(OUTPUT_FOLDER, output_filename)

if output_format == "json":
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

elif output_format == "txt":
    with open(output_path, "w", encoding="utf-8") as f:
        for filename, data in results.items():
            f.write(f"{'='*60}\n")
            f.write(f"File: {filename}\n")
            if data["status"] == "success":
                f.write(f"Status: Success\n")
                f.write(f"Type: {data['file_type']} | Size: {data['image_size']['width']}x{data['image_size']['height']} | Mode: {data['mode']}\n")
                f.write(f"Words: {data['word_count']} | Characters: {data['character_count']}\n")
                f.write(f"Timestamp: {data['timestamp']}\n")
                f.write(f"\nExtracted Text:\n{data['extracted_text']}\n")
            else:
                f.write(f"Status: Error — {data['message']}\n")
            f.write("\n")

elif output_format == "csv":
    fieldnames = ["filename", "status", "file_type", "width", "height", "mode",
                  "word_count", "character_count", "extracted_text", "timestamp", "error_message"]
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for filename, data in results.items():
            if data["status"] == "success":
                writer.writerow({
                    "filename": data["filename"],
                    "status": data["status"],
                    "file_type": data["file_type"],
                    "width": data["image_size"]["width"],
                    "height": data["image_size"]["height"],
                    "mode": data["mode"],
                    "word_count": data["word_count"],
                    "character_count": data["character_count"],
                    "extracted_text": data["extracted_text"],
                    "timestamp": data["timestamp"],
                    "error_message": ""
                })
            else:
                writer.writerow({
                    "filename": data["filename"],
                    "status": data["status"],
                    "file_type": "", "width": "", "height": "", "mode": "",
                    "word_count": "", "character_count": "", "extracted_text": "",
                    "timestamp": "", "error_message": data.get("message", "")
                })

print(f"\n✅ Done! {output_format.upper()} saved to: {output_path}")