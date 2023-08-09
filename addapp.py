#!/usr/bin/python3
import os
import sys

if not 3 <= len(sys.argv) <= 4:
    print("Usage: addapp name exec [icon]")
    exit()

name = sys.argv[1]
exec = sys.argv[2]

out = """
[Desktop Entry]
Name={0}
Comment={1}
Exec={2}
Terminal=false
Type=Application
""".format(name, name, exec)

if len(sys.argv) == 4:
    out += "Icon={argv[3]}"

home = os.path.expanduser('~')
f = open(home + f'/.local/share/applications/{name}.desktop',"w+")
f.write(out)
