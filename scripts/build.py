import os
import subprocess
import sys

rootDir = os.getcwd()

def buildPathFromRoot(*subdirs):
    return os.path.join(rootDir, *subdirs)


if __name__ == "__main__":
    preset: str = sys.argv[1]
    
    buildDir = buildPathFromRoot("build", preset)

    subprocess.run(["cmake", "--preset", preset, "-S", rootDir])
    
    os.chdir(buildDir)
    
    subprocess.run(["ninja"])
    
    os.chdir(rootDir)
