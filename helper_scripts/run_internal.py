import os
import subprocess

import subprocess
import platform

buildType = "internal"
projectName = "TemplateProject"

buildPlatform = platform.system().lower();
buildArgument = f"{buildPlatform}-{buildType}"

rootDir = os.getcwd()

def buildPathFromRoot(*subdirs):
    return os.path.join(rootDir, *subdirs)

binDir = buildPathFromRoot("build", buildArgument)
binPath = buildPathFromRoot("build", buildArgument, projectName)

callingDir = os.getcwd();

os.chdir(binDir)

subprocess.run([binPath])

os.chdir(callingDir)
