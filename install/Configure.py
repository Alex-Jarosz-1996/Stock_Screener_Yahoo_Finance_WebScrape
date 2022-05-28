import sys
import subprocess

def getAllPackages():
    # declaring all packages used in this project
    return ['requests', 'pandas', 'bs4', 'os', 'sys', 'subprocess', 're', 'time', 'shutil', 'random']

def install():
    packagesRequired = getAllPackages()
    numPackages = len(packagesRequired)

    print(f"Number of packages to install: {numPackages}\n\n")
    errorList = []
    for count, p in enumerate(packagesRequired, start=1):
        print('\n')
        print(f"Installing package: {p}")
        print(f"{count} / {numPackages}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{p}'])
        except Exception as e:
            errorList.append(p)
            print(f"Error: {e}")
            continue

    if not errorList:
        print('All packages successfully installed')
    else:
        for e in errorList:
            print('\n')
            print(e, ' did not install. ')
    
if __name__ == "__main__":
    install()
    
