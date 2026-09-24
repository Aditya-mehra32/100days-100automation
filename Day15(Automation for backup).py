import shutil
from datetime import datetime

source = "C:/Users/YourName/Documents"
backup = "D:/Backup"

date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

destination = f"{backup}/Backup_{date}"

shutil.copytree(source, destination)

print("Backup completed!")
