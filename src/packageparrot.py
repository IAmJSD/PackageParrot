import sys, requests
# Imports go here.

class info:
    name = "PackageParrot"
    version = "1.00"
    author = "Jake Gealer"
    github_username = "jakemakesstuff"
    branch = "master"
    github_project_name = "packageparrot"
# The class that contains info globally used in the script.

def main(args):

    def install(args):
        if len(args) == 0:
            raise Exception("No arguments to install found. Do 'help' for command help.")
        else:
            windows32 = False
            windows64 = False
            linux = False
            mac = False
            if sys.platform == "linux" or sys.platform == "linux2":
                linux = True
            elif sys.platform == "darwin":
                mac = True
            elif sys.platform == "win32":
                windows32 = True
            elif sys.platform == "win64":
                windows64 = True
            else:
                raise Exception("Your OS is not supported by " + info.name)
            for arg in args:
                r = requests.get('https://raw.githubusercontent.com/'+info.github_username+'/'+info.github_project_name+'/'+info.branch+'/recipes/'+arg+'.json')
                if r.status_code == 404:
                    raise Exception("Could not find a project named " + arg)
                else:
                    r = r.json()
                    if linux and not r["linux"]:
                        raise Exception("You appear to be on Linux and the application does not support it.")
                    if windows32 and not r["windows32"]:
                        raise Exception("You appear to be on Windows x86 and the application does not support it.")
                    if windows64 and not r["windows64"]:
                        raise Exception("You appear to be on Windows x64 and the application does not support it.")
                    if mac and not r["mac"]:
                        raise Exception("You appear to be on OS X and the application does not support it.")
                    print("Fetching/running the cookbook required.")
                    x = requests.get(r["cookbook"])
                    exec(x.text)
    # The script used to install packages.

    function = args[0].lower()
    del args[0]
    if function == "install":
        install(args)
    # The part of the script used to route to other parts of the script.

# The main definition in the script.

if __name__ == '__main__':
    print(info.name + " " + info.version + ". Created by " + info.author + ".") 
    del sys.argv[0]
    if len(sys.argv) >= 1:
        main(sys.argv)
    else:
        raise Exception("Could not find any arguments. Do 'help' for command help.")
# The argument-based launcher.
