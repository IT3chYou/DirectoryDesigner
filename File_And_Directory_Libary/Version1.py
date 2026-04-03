import os
from rich import print
from rich.prompt import Prompt
from rich.console import Console
import base64

class Design:
    def __init__(self,directory_name):
        self.file_name = "file"
        self.directory_name = directory_name # For Root File To Searching File and sub File 
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
    ".c", ".cpp", ".h", ".hpp", ".java", ".js", ".ts", ".py", ".cs", ".rb", ".go", ".rs", ".swift", ".php", ".html", ".htm", ".css", ".scss", ".xml", ".json", ".yaml", ".yml", ".ini", ".cfg", ".toml", ".sql",

    # Veritabanı dosyaları
    ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb",

    # Sanal makine / disk imajı
    ".vdi", ".vmdk", ".vhd", ".img", ".dmg",

    # Yazı tipi dosyaları
    ".ttf", ".otf", ".woff", ".woff2", ".fon",

    # Sistem dosyaları
    ".sys", ".dll", ".drv", ".bak", ".tmp", ".swp", ".lock",

    # Web / tarayıcı ile ilgili
    ".asp", ".aspx", ".jsp", ".php", ".cgi", ".xhtml", ".shtml", ".htaccess",

    # Diğer
    ".torrent", ".crdownload", ".part", ".desktop", ".lnk"
]


    def __str__(self):
        return f"[orange]Starting Directory and File Design[/orange]"
    


    def create_directory(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                self.console.print(f"[green]Directory created: {path}[/green]")
            return path
        except Exception as e:
            self.console.print(f"[red]Error creating directory:[/red] {e}")


    def move_file(self,source,dest):
        try:
            os.rename(source,dest)
        except Exception as e:
            self.console.print(f"[red]Error: {e}[/red]")



    def read_file(self,file_name):
        try:
            with open(file_name,"rb") as file:
                content = file.read()
                print(content)
        except Exception as e:
            print("Error : ", e)
    
    
    
    def discover(self, current_dir=None):
        if current_dir is None:
            current_dir = self.directory_name
        try:
            for dict_or_file in os.listdir(current_dir):  # Şu anki klasör
                self.console.print(f"[green]Root Dict :{dict_or_file}[/green]")
                full_path = os.path.join(current_dir, dict_or_file)  # Dosya tam yolu

                if os.path.isfile(full_path):
                    name, ext = os.path.splitext(dict_or_file)
                    if ext in self.file_extensions:
                        new_file_name = self.create_directory(f"{self.file_name}_{ext.lstrip('.')}")
                        dest_path = os.path.join(new_file_name, dict_or_file)
                        self.move_file(full_path, dest_path)
                    else:
                        self.console.print("[yellow]Unknown Extension![/yellow]")


                elif os.path.isdir(full_path):
                    self.discover(full_path)  # recursive: klasörün içine gir

                else:
                    self.console.print(f"[Yellow]There is no file in root path[Yellow]") 

        except (FileExistsError, FileNotFoundError) as e:
            print(e)



if __name__=="__main__":
    name = input("Enter Directory ")
    De = Design(name)
    De.discover()