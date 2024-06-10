import sys

with open(sys.argv[1], "r") as fh:
    lines = fh.readlines()

new_lines = []
for line in lines:
    if line.startswith("export ACLOCAL_PATH="):
        line = line.replace("/usr/share/aclocal", "${ACLOCAL_PATH}")
    if line.startswith("export MANPATH="):
        line = line.replace("/usr/share/man:.:", "${MANPATH}")
    if line.startswith("export PATH="):
        line = line.replace("/sdf/home/p/psrel/spack/bin:/sdf/home/p/psrel/.local/bin:/sdf/home/p/psrel/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin", "${PATH}")
    if line.startswith("export PKG_CONFIG_PATH="):
        line = line.replace("/usr/share/pkgconfig:/usr/lib64/pkgconfig", "${PKG_CONFIG_PATH}")
    if line.startswith("export PYTHONPATH="):
        line = f"#{line}"
    if line.startswith("export XDG_DATA_DIRS="):
        line = line.replace("/sdf/home/p/psrel/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share:/usr/share", "${XDG_DATA_DIRS}")
    new_lines.append(line)

with open(sys.argv[2], "w") as fh:
    for line in new_lines:
        lines = fh.write(line)
