import sys
import os
from pathlib import Path



def main():
    parameters = sys.argv[1:]
    fileteredFiles = []
    if len(parameters) < 3:
        print("[error] At least 3 parameters required 1 provided")
        return
    for file in os.listdir(parameters[0]):
        if file.endswith(parameters[1]):
            fileteredFiles.append(file)

    for filteredFile in fileteredFiles:
        content = Path(parameters[0] + '/' + filteredFile).read_text(encoding="UTF-8")
        filteredText = [line for line in content.splitlines() if parameters[2] in line]
    Path('result_text.txt').write_text("\n".join(filteredText), encoding="UTF-8")
main()


