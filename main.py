"""Project configuration and shared category rules."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "file_inventory.csv"
SCAN_FOLDER = BASE_DIR / "sample_files"

CATEGORY_EXTENSIONS = {
    "Documents": {".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt"},
    "Images": {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"},
    "Spreadsheets": {".csv", ".xls", ".xlsx"},
    "Presentations": {".ppt", ".pptx"},
    "Audio": {".mp3", ".wav", ".m4a"},
    "Video": {".mp4", ".mov", ".mkv"},
    "Archives": {".zip", ".rar", ".7z", ".tar"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".cpp"},
}

CSV_COLUMNS = ["record_id", "file_name", "extension", "category", "size_bytes", "modified_date", "file_path"]
