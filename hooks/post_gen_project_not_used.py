import os
import subprocess

def env_exist(env_name):
    """Check if an env_name is already used/created"""
    enviroments  = os.popen('conda env list').readlines()

    for line in enviroments:
        if f'envs/{env_name}' in line:
            return True
    
    return False


MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"
project_packages = "{{ cookiecutter.project_packages }}"

print(f"{MESSAGE_COLOR}The enviroment will be created automatically")
print(f"with the name ds or tf in case that it does not exist {RESET_ALL}")

if env_exist(project_packages):
    print(f"{MESSAGE_COLOR}Run conda activate {project_packages} {RESET_ALL}")

else:
    
    env_path = project_packages +'_'+'environment.yaml'
    print(f"{MESSAGE_COLOR}Run conda env create -f {env_path} {RESET_ALL}")



print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")