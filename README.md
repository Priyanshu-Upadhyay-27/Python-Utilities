# 🐍 Python as Utility

> **A collection of handy Python automation scripts that solve everyday file-conversion headaches.**

Transfer photos and videos from macOS / iOS to Windows? Need to convert a PDF into images? These lightweight scripts handle it — just drop your files in, run the script, and pick up the converted output.

---

## 📦 What's Inside

| Script | What It Does | Input → Output | Core Library |
|---|---|---|---|
| [`FileFormat/changer.py`](./FileFormat/changer.py) | Batch image conversion | `.heic` → `.jpg` | [Pillow](https://python-pillow.org/) + [pillow-heif](https://github.com/bigcat88/pillow_heif) |
| [`VideoFormat/VideoCHanger.py`](./VideoFormat/VideoCHanger.py) | Batch video conversion | `.mov` `.avi` `.mp4` → `.mp4` (H.264) | [MoviePy](https://zulko.github.io/moviepy/) |
| [`PDF2IMAGE.py`](./PDF2IMAGE.py) | PDF page extraction | `.pdf` → `.jpg` (per page) | [pdf2image](https://github.com/Belval/pdf2image) |

All scripts use **`.env` files** for path configuration — no hardcoded paths, nothing personal gets pushed.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) (required **only** for `PDF2IMAGE.py` — add to `PATH`)

### 1. Clone & Enter

```bash
git clone https://github.com/<your-username>/python-as-utility.git
cd python-as-utility
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
# For HEIC → JPEG conversion
pip install Pillow pillow-heif python-dotenv

# For Video conversion
pip install moviepy python-dotenv

# For PDF → Image conversion
pip install pdf2image python-dotenv
```

### 4. Configure Paths

Each script reads paths from a `.env` file. Copy the template and fill in your paths:

```bash
cp .env.example .env                         # For PDF2IMAGE.py
cp FileFormat/.env.example FileFormat/.env   # For changer.py
cp VideoFormat/.env.example VideoFormat/.env # For VideoCHanger.py
```

### 5. Run

```bash
python FileFormat/changer.py        # Convert HEIC photos to JPEG
python VideoFormat/VideoCHanger.py  # Convert MOV/AVI videos to MP4
python PDF2IMAGE.py                 # Convert PDF pages to JPEG images
```

---

## 🖼️ FileFormat — HEIC → JPEG

Converts Apple HEIC photos (from iPhone / macOS AirDrop) to universally compatible JPEG.

**`.env` config:**
```env
INPUT_FOLDER=C:\path\to\your\heic\files
OUTPUT_FOLDER=C:\path\to\output\jpegs
```

**What it does:**
- Scans the input folder for `.heic` files
- Converts each to JPEG using Pillow with HEIF support
- Creates the output directory automatically
- Preserves original filenames (only the extension changes)

**Customise:**
| Want to… | Change this |
|---|---|
| Output as **PNG** | `img.save(output_path, "PNG")` + change extension |
| Adjust **JPEG quality** | `img.save(output_path, "JPEG", quality=95)` |
| Process **subfolders** | Replace `os.listdir()` with `os.walk()` |

---

## 🎬 VideoFormat — MOV / AVI → MP4

Re-encodes videos with **H.264 + AAC** — the most universally compatible codec pairing.

**`.env` config:**
```env
INPUT_FOLDER=C:\path\to\your\videos
OUTPUT_FOLDER=C:\path\to\output\mp4s
```

**What it does:**
- Scans for `.mov`, `.avi`, and `.mp4` files
- Re-encodes with `libx264` video + `aac` audio codecs
- Shows a progress bar per file (via MoviePy/tqdm)
- No system FFmpeg install needed — `imageio-ffmpeg` bundles it

**Verify MoviePy install:**
```bash
python VideoFormat/testin.py
# Expected: "MoviePy is working!"
```

**Customise:**
| Want to… | Change this |
|---|---|
| Use **H.265** codec | `codec="libx265"` |
| **Strip audio** | `clip.write_videofile(..., audio=False)` |
| **Resize** video | `clip.resize(height=720)` before `write_videofile()` |
| Control **bitrate** | `clip.write_videofile(..., bitrate="8000k")` |

---

## 📄 PDF2IMAGE — PDF → JPEG

Extracts every page of a PDF as a high-resolution JPEG image.

**`.env` config:**
```env
PDF_PATH=C:\path\to\your\document.pdf
OUTPUT_FOLDER=C:\path\to\output\images
```

**What it does:**
- Converts each PDF page to a 300 DPI JPEG (configurable)
- Saves as `page_1.jpg`, `page_2.jpg`, etc.
- Creates the output directory automatically

> **Note:** Requires [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) installed and added to your system `PATH`.

---

## 🔒 Environment Variables & Security

All personal file paths are stored in `.env` files which are **gitignored** — they never get pushed.

Each script has a matching `.env.example` template checked into git:

```
.env.example              ← PDF2IMAGE paths
FileFormat/.env.example   ← HEIC converter paths
VideoFormat/.env.example  ← Video converter paths
```

Clone the repo → copy `.env.example` to `.env` → fill in your paths → run.

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'pillow_heif'` | `pip install pillow-heif` |
| `ModuleNotFoundError: No module named 'moviepy'` | `pip install moviepy` |
| `pdf2image` errors about Poppler | Install [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) and add its `bin/` to your `PATH` |
| Video conversion is very slow | Expected — re-encoding is CPU-intensive. Try reducing resolution |
| `.env` values not loading | Ensure no extra spaces around `=` in your `.env` file |

---

## 📁 Project Structure

```
Python-as-Utility/
├── .env.example              # Path template for PDF2IMAGE
├── .gitignore
├── README.md
├── PDF2IMAGE.py              # PDF → JPEG converter
│
├── FileFormat/
│   ├── .env.example          # Path template
│   └── changer.py            # HEIC → JPEG converter
│
└── VideoFormat/
    ├── .env.example          # Path template
    ├── VideoCHanger.py       # MOV/AVI → MP4 converter
    └── testin.py             # MoviePy install verification
```

---

## 📝 License

This project is licensed under the [MIT License](./LICENSE) — you're free to use, modify, and distribute it.

---

## 👤 Author

**Priyanshu Upadhyay**

- GitHub: [@Priyanshu-Upadhyay-27](https://github.com/Priyanshu-Upadhyay-27)

---

<p align="center">
  ⭐ If you found these scripts useful, consider giving the repo a star!
</p>
