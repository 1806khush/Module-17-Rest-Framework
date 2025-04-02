import subprocess
import sys
import os

# Step 1: Create a virtual environment
def create_virtualenv(venv_name):
    print(f"Creating a virtual environment '{venv_name}'...")
    subprocess.check_call([sys.executable, "-m", "venv", venv_name])

# Step 2: Activate the virtual environment
def activate_virtualenv(venv_name):
    activate_script = os.path.join(venv_name, 'Scripts', 'activate_this.py')  # For Windows
    if not os.path.exists(activate_script):
        activate_script = os.path.join(venv_name, 'bin', 'activate_this.py')  # For Linux/Mac

    with open(activate_script) as f:
        exec(f.read(), {'__file__': activate_script})

# Step 3: Install packages from requirements.txt
def install_requirements():
    print("Installing dependencies from 'requirements.txt'...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Step 4: Create a new Django project
def create_django_project(project_name):
    print(f"Creating Django project '{project_name}'...")
    subprocess.check_call([sys.executable, "-m", "django", "admin", "startproject", project_name])

def main():
    venv_name = "myenv"  # You can change this to any name you want for the virtual environment
    project_name = "myproject"  # You can change this to any Django project name

    # Step-by-step process to set up the environment and create the Django project
    create_virtualenv(venv_name)
    activate_virtualenv(venv_name)
    install_requirements()
    create_django_project(project_name)

    print(f"Your Django project '{project_name}' is now set up!")

if __name__ == "__main__":
    main()
