import os
import subprocess
import platform

rootDir = os.getcwd()

def buildPathFromRoot(*subdirs):
    return os.path.join(rootDir, *subdirs)


if __name__ == "__main__":
    buildDir = buildPathFromRoot("build")
    vcpkgDir = buildPathFromRoot("vendor", "vcpkg")

    os.makedirs(buildDir, exist_ok=True)
    os.makedirs(vcpkgDir, exist_ok=True)

    platform = platform.system().lower();
    if platform == "linux":
        vcpkgBootstrap = f"{buildPathFromRoot(vcpkgDir, 'bootstrap-vcpkg.sh')}"
    elif platform == "windows":
        vcpkgBootstrap = f"{buildPathFromRoot(vcpkgDir, 'bootstrap-vcpkg.bat')}"
    else:
        print(f"Unsupported platform: {platform}")
        exit()

    vcpkgInstallLocation = buildPathFromRoot(vcpkgDir, "vcpkg")
    
    subprocess.run([vcpkgBootstrap])
    subprocess.run([vcpkgInstallLocation, "install"])
