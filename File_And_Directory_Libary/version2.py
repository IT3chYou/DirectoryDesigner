import os
import shutil
from rich import print
from rich.console import Console


class Design:
    def __init__(self, directory_name):
        self.file_name = "file"
        self.directory_name = directory_name
        self.console = Console()
        self.file_extensions = [
            # Metin ve belge
            ".txt", ".doc", ".docx", ".pdf", ".odt", ".rtf", ".tex", ".wpd", ".md", ".log",
            # Tablolar
            ".xls", ".xlsx", ".csv", ".ods",
            # Sunum
            ".ppt", ".pptx", ".odp",
            # Görsel dosyalar
            ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".ico", ".psd", ".ai",
            # Ses dosyaları
            ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".mid",
            # Video dosyaları
            ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".3gp", ".mpeg", ".mpg", ".m4v",
            # Sıkıştırılmış dosyalar / arşivler
            ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".cab",
            # Yürütülebilir dosyalar
            ".exe", ".msi", ".bat", ".sh", ".apk", ".bin", ".com", ".cmd", ".jar", ".py", ".pl", ".ps1",
            # Kod / kaynak dosyalar
            ".c", ".cpp", ".h", ".hpp", ".java", ".js", ".ts", ".cs", ".rb", ".go", ".rs", ".swift",
            ".php", ".html", ".htm", ".css", ".scss", ".xml", ".json", ".yaml", ".yml",
            ".ini", ".cfg", ".toml", ".sql",
            # Veritabanı dosyaları
            ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb",
            # Sanal makine / disk imajı
            ".vdi", ".vmdk", ".vhd", ".img", ".dmg",
            # Yazı tipi dosyaları
            ".ttf", ".otf", ".woff", ".woff2", ".fon",
            # Sistem dosyaları
            ".sys", ".dll", ".drv", ".bak", ".tmp", ".swp", ".lock",
            # Web / tarayıcı ile ilgili
            ".asp", ".aspx", ".jsp", ".cgi", ".xhtml", ".shtml", ".htaccess",
            # Diğer
            ".torrent", ".crdownload", ".part", ".desktop", ".lnk"
        ]

    def __str__(self):
        return "[orange]Starting Directory and File Design[/orange]"

    def create_directory(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                self.console.print(f"[green]Directory created: {path}[/green]")
            return path
        except Exception as e:
            self.console.print(f"[red]Error creating directory: {e}[/red]")

    def move_file(self, source, dest):
        try:
            shutil.move(source, dest)
        except Exception as e:
            self.console.print(f"[red]Move Error: {e}[/red]")

    def discover(self, current_dir=None):
        if current_dir is None:
            current_dir = self.directory_name
        try:
            for entry in os.listdir(current_dir):
                full_path = os.path.join(current_dir, entry)
                self.console.print(f"[green]Scanning: {full_path}[/green]")

                if os.path.isfile(full_path):
                    name, ext = os.path.splitext(entry)
                    if ext.lower() in self.file_extensions:
                        dest_dir = self.create_directory(
                            os.path.join(self.directory_name, f"{self.file_name}_{ext.lstrip('.')}"))
                        dest_path = os.path.join(dest_dir, entry)
                        self.move_file(full_path, dest_path)
                    else:
                        self.console.print(f"[yellow]Unknown extension: {ext}[/yellow]")

                elif os.path.isdir(full_path):
                    self.discover(full_path)

        except Exception as e:
            self.console.print(f"[red]Discovery Error: {e}[/red]")


if __name__ == "__main__":
    directory = input("Enter directory path: ").strip()
    if os.path.isdir(directory):
        d = Design(directory)
        d.discover()
    else:
        print("[red]Invalid directory![/red]")
