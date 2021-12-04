import os, re
print("current working directory:",os.getcwd())

URL = input("복사하고자 하는 레포지토리의 하위 폴더의 URL을 입력하세요: ")

#https://github.com/{username}/{reponame}/tree/{branchname}/{subfolders} 형식인지 검사
isrightURL =re.compile("https://github.com/[0-9|a-z|A-Z|\-]+/[0-9|a-z|A-Z\-]+/tree/[0-9|a-z|A-Z|/|\-]+").match(URL)
if not isrightURL:
    print("Error: 올바른 형식의 URL 또는 입력이 아닙니다.")
    print("""\
올바르지 않은 URL인 경우:
    * URL 끝에 확장자가 있는 경우(.git 포함)
    * 폴더경로로 이루어지지 않은 URL
    * https://github.com/로 시작하지 않는 URL""")
    exit()
else:
    if input("정말 이 URL로 clone하시겠습니까?(Y/n): ") == "Y":
        pass
    else:
        exit()
 
username, reponame, subfolders = URL.lstrip("https://github.com/").split("/",2)
subfolders = subfolders.lstrip("tree/").split("/",1)[-1] #branch이름이랑 subfolder를 분리

print(subfolders)

gitHTTPS = f"https://github.com/{username}/{reponame}.git"

os.system(f"mkdir {reponame}")
os.chdir(f"./{reponame}")
print("current working directory:",os.getcwd())
print( f"echo {subfolders}/* >> .git/info/sparse-checkout")

commands = (
    "git init",
    f"git remote add origin {gitHTTPS}",
    "git config core.sparsecheckout true",
    f"echo {subfolders}/* >> .git/info/sparse-checkout",
    "git pull origin master",)

for cmd in commands:
    os.system(cmd)