# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


import git
import random
import time, os
from configparser import ConfigParser


def sleeper(sleeptime):
    for i in range(sleeptime):
        print("next time commit countdown:" + str(sleeptime - i))
        time.sleep(1)


def read_config():
    cf = ConfigParser()
    file = cf.read(r"./config/config.ini", encoding="utf-8")
    sleeptime = int(cf.get("sleep", "time"))
    return {"sleeptime": sleeptime}


def init_menu():
    print("The default sleeping gap is 30 s\nYou can modify it in config.ini\n")
    print("Have Fun! OvO")


def main():
    config = read_config()
    init_menu()
    if not os.path.exists("./commitfiles"):
        repo = git.Repo.clone_from(url='https://github.com/TK-Thousand/develop.git', to_path='commitfiles')
        print("repo directory not exist")

    else:
        repo = git.Repo("./commitfiles")
        print("repo directory already exist")

    remote = repo.remote()
    print("Starting commit")
    times = 1
    while True:
        print("This is %s time commit" % times)
        with open("./commitfiles/test.txt", "a+") as f:
            f.writelines("OneGO" + str(random.randrange(1, 65536)))
            f.close()
        index = repo.index
        index.add(["test.txt"])
        index.commit("PYcommit")
        remote.push()
        print("OK for " + str(times) + "times")
        times += 1
        sleeper(config.get("sleeptime"))


if __name__ == "__main__":
    main()
