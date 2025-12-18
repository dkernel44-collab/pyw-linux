import subprocess as sp
def run(c, a) :
    sp.run([c, a])
def run_root(cmd, arg) :
    sp.run(["sudo", cmd, arg])
def mkdir(dir) :
    sp.run(["mkdir", dir])
def get(URL) :
    sp.run(["wget", URL])
def ping(url, count) :
    sp.run(["ping", "-c", count, url])
def vi(file) :
    vi_out = sp.run(["vi", file])
    if vi_out == "command not found" :
        pacman("vi")
        apt("vi")
        apk("vi")

def nano(file) :
    nano_out == sp.run(["nano", file])
    if nano_out == "command not found" :
        pacman("nano")
        apt("nano")
        apk("nano")
def ssh(username, ip, port, command):
    sp.run([f"ssh", "-{port}", "{username}@{ip}"])
def ssh_run(username, ip, port, command):
    sp.run([f"ssh", "-{port}", "{username}@{ip}", command])
def docker_images_pull(image):
    sp.run(["docker", "image", "pull", image])
def docker_images_list():
    sp.run(["docker", "images"])
def docker_run(name, image):
    sp.run(["docker", "run", "--name", name, "-d", image])
def docker_stop(cname):
    sp.run(["docker", "stop", cname])
def docker_rm(cname):
    sp.run(["docker", "rm", cname])
def screenfetch():
    sp.run(["screenfetch"])
def get_os():
    cat_proc = sp.run(["cat", "/etc/os-release"], capture_output=True, text=True)
    os_name = sp.run(["grep", "ID_LIKE"], input=cat_proc.stdout, capture_output=True, text=True)
    print(os_name.stdout)
def cat(file):
    sp.run(["cat", file])
def store_os():
    os = getos()
def nvim() :
    nvim_out = sp.run(["nvim", file])
    if nvim_out == "command not found" :
        pacman()
def pacman(pkg) :
    ask = input(f"the program has asked to install package {pkg} <Y/N> : ")
    if ask == "y" :
        sp.run(["sudo", "pacman", "-S", pkg])
    elif ask == "n" :
        print("Aborted.")
    else :
        print("Aborted.")
def apt(apkg) :
    ask = input(f"the program has asked to install package {apkg} <Y/N> : ")
    if ask == "y" :
        sp.run(["sudo","apt","install", apkg])
    elif ask == "n" :
        print("Aborted.")
    else :
        print("Aborted.")
def apk(ppkg) :
    ask = input(f"the program has asked to install package {ppkg} <Y/N> : ")
    if ask == "y" :
        sp.run(["sudo", "apk", "add", ppkg])
    elif ask == "n" :
        print("Aborted.")
    else :
        print("Aborted.")
def ls(lsfile) :
    sp.run(["ls", lsfile])
def version():
    print("25.git.1.homer")
def version_simple():
    print("25.1")