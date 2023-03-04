import re
import os
import sys
import glob


def replace(s: re.Match):
    var_name = s.group(1)
    if var_name in os.environ:
        return os.environ[var_name]

    return ""


def replace_file(filename: str) -> None:
    *base, _, ext = filename.split('.')
    base = '.'.join(base)
    print(base)

    with open(filename, 'r') as infile:
        s = infile.read()
        s = re.sub(r"{{\s*\$([\da-zA-Z_]*)\s*}}", replace, s)
        with open(base + '.' + ext, 'w') as outfile:
            outfile.write(s)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = glob.glob("./**/*.template.yaml", recursive=True)

    if len(files):
        for i, filename in enumerate(files):
            print(f"Processing file \"{filename}\" [{i+1} of [{len(files)}]]")
            replace_file(filename)
    else:
        print("No files found.")
