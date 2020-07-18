from pathlib import Path
import shutil, os, sys, collections

if len(sys.argv) != 3:
    print('Incorrect Input!')
    sys.exit()
path = Path(sys.argv[1])
# check if the input begin with root directory
# if not apppend the input with it
if not str(path).startswith(str(Path.home())): path = Path.home() / path
# if path is not exist or not a directory, print message
if not path.exists() or not path.is_dir():
    print(f'\"{path}\" is either not exist or is not a directory!')
else:
    print(f'\"{path}\" is valid and exist!')
    userInput = sys.argv[2]
    # find files by type
    if userInput.startswith('.'):
        # create output directory in Desktop
        ext, outPath = userInput, Path.home() / 'Desktop/Result'
        os.mkdir(outPath)

        pathlist, tempStr = outPath / 'pathlist.txt', ""
        trackfiles = collections.Counter()
        for p in sorted(path.glob('**/*' + ext)):
            trackfiles[p.name] += 1
            if trackfiles[p.name] > 1:
                newName = p.name.split('.')[0] + str(trackfiles[p.name]) + ext
                shutil.copy(p, outPath / newName)
                tempStr += f'{p}\n(\'{newName}\' in output folder)\n'
            else:
                shutil.copy(p, outPath)
                tempStr += str(p) + '\n'
            pathlist.write_text(tempStr)
    # find files by name
    else:
        userInput = userInput.split('.')[0]
        resPath, tempStr = Path.home() / 'Desktop/Result.txt', ""
        for p in sorted(path.glob('**/*')):
            if p.name.split('.')[0] == userInput:
                tempStr += str(p) + '\n'
        resPath.write_text(tempStr)