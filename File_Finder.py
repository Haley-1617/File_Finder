from pathlib import Path
import shutil, os
path = Path(input("Enter the path of your current directory: "))
if not str(path).startswith(str(Path.home())): path = Path.home() / path
if not path.exists() or not path.is_dir():
    print(f'\"{path}\" is either not exist or is not a directory!')
else:
    print(f'\"{path}\" is valid and exist!')
    for p in sorted(path.glob('**/*.html')):
        shutil.copy(p, Path.home() / 'Desktop/Result')
        print(str(p)[len(str(path)):])
