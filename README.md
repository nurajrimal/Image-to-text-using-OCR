# 🖼️ Image to Text using OCR

A Python tool that extracts text from images using Tesseract OCR and saves the results in your preferred format — **JSON**, **TXT**, or **CSV**.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Output Formats](#output-formats)
- [Supported Image Types](#supported-image-types)
- [Example Output](#example-output)
- [Troubleshooting](#troubleshooting)

---

## ✨ Features

- Extracts text from multiple images in one run
- Choose your output format: **JSON**, **TXT**, or **CSV**
- Captures image metadata (size, mode, file type)
- Word and character count per image
- Timestamps each extraction
- Handles errors gracefully without stopping the whole process

---

## ⚙️ Requirements

- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
- Python libraries:
  - `Pillow`
  - `pytesseract`

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Image-to-text-using-OCR.git
cd Image-to-text-using-OCR
```

### 2. Install Python dependencies

```bash
pip install Pillow pytesseract
```

### 3. Install Tesseract OCR

**macOS:**
```bash
brew install tesseract
```

**Ubuntu/Debian:**
```bash
sudo apt install tesseract-ocr
```

**Windows:**
- Download the installer from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
- After installing, uncomment and update this line in the script:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## 📁 Project Structure

```
Image-to-text-using-OCR/
│
├── images/               # 📂 Put your images here
│   ├── sample1.png
│   └── sample2.jpg
│
├── output/               # 📂 Extracted results saved here (auto-created)
│   └── extracted_20240101_120000.json
│
├── main.py               # 🐍 Main script
└── README.md             # 📖 You're reading this!
```

---

## 🖥️ How to Use

### Step 1 — Add your images

Place all your images inside the `images/` folder.

### Step 2 — Run the script

```bash
python main.py
```

### Step 3 — Choose your output format

The script will prompt you:

```
📄 Select output format:
  1. JSON
  2. TXT
  3. CSV

Enter 1, 2, or 3:
```

### Step 4 — Get your results

Your output file will be saved in the `output/` folder with a timestamp in the filename, e.g.:

```
output/extracted_20240315_143022.json
```

---

## 📄 Output Formats

### 1. JSON
Structured data — best for developers or further processing.
```json
{
    "sample.png": {
        "status": "success",
        "filename": "sample.png",
        "file_type": ".png",
        "image_size": { "width": 800, "height": 600 },
        "mode": "RGB",
        "extracted_text": "Hello, World!",
        "word_count": 2,
        "character_count": 13,
        "timestamp": "2024-03-15T14:30:22"
    }
}
```

### 2. TXT
Human-readable plain text — best for quick reading.
```
============================================================
File: sample.png
Status: Success
Type: .png | Size: 800x600 | Mode: RGB
Words: 2 | Characters: 13
Timestamp: 2024-03-15T14:30:22

Extracted Text:
Hello, World!
```

### 3. CSV
Spreadsheet-friendly — best for analysis in Excel or Google Sheets.

| filename | status | file_type | width | height | word_count | extracted_text |
|----------|--------|-----------|-------|--------|------------|----------------|
| sample.png | success | .png | 800 | 600 | 2 | Hello, World! |

---

## 🖼️ Supported Image Types

| Format | Extension |
|--------|-----------|
| PNG | `.png` |
| JPEG | `.jpg`, `.jpeg` |
| BMP | `.bmp` |
| GIF | `.gif` |
| TIFF | `.tiff`, `.tif` |
| WebP | `.webp` |

---

## 🔧 Troubleshooting

**`TesseractNotFoundError`**
Tesseract is not installed or not in your PATH. Follow the [installation steps](#3-install-tesseract-ocr) above.

**`No images found in 'images' folder`**
Make sure your images are inside the `images/` folder and are a supported file type.

**`images folder not found`**
Create an `images/` folder in the same directory as `main.py` and add your images to it.

**Poor text extraction quality**
- Use high-resolution images (300 DPI or more)
- Make sure the text in the image is clear and not rotated
- Avoid noisy or heavily compressed images

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or have a feature request, feel free to open an issue.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
