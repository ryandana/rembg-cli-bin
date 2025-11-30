import argparse
import sys
from pathlib import Path
from rembg import remove
from PIL import Image

def process_file(file_path):
    try:
        path_obj = Path(file_path)
        
        if not path_obj.exists() or not path_obj.is_file():
            print(f"⚠️  File tidak ditemukan: {file_path}")
            return

        print(f"⏳ Memproses: {path_obj.name}...", end="\r")

        output_filename = f"{path_obj.stem}_no_bg.png"
        output_path = path_obj.parent / output_filename

        # Proses penghapusan background
        img = Image.open(path_obj)
        output = remove(img)
        
        # Simpan
        output.save(output_path)
        print(f"✅ Selesai: {output_filename}   ")

    except Exception as e:
        print(f"❌ Error pada {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Hapus background gambar dan simpan di folder yang sama.")
    parser.add_argument('files', nargs='+', help='List file gambar yang akan diproses')
    
    args = parser.parse_args()

    if not args.files:
        print("Gunakan: cli_rembg <file1> <file2> ...")
        sys.exit(1)

    for file in args.files:
        process_file(file)

if __name__ == "__main__":
    main()
