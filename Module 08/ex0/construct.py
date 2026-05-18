import os
import sys


def build_site_packages_path(prefix_path: str) -> str:
    '''Constructs the path to the sitepackages directory based on the given'''
    major = sys.version_info.major  # Get the major version of Python (e.g., 3)
    minor = sys.version_info.minor  # Get the minor version of Python (e.g., 8)
    return (
        os.path.join(
                     prefix_path, "lib",
                     f"python{major}.{minor}",
                     "site-packages")
        )
    # If prefix_path is "/home/user/matrix_env", and Python version is 3.8,
    # this will return "/home/user/matrix_env/lib/python3.8/site-packages"


def get_environment_name(env_path: str) -> str:
    '''Extracts the name of the virtual environment from its path.'''
    normalized = os.path.normpath(env_path)
    return os.path.basename(normalized)


def main() -> None:
    '''Checks if the user is in a virtual environment via os.environ.get().
    If in a virtual environment, it prints the current Python executable,
    the name of the virtual environment, its path, and the site-packages path.
    If not in a virtual environment, it warns the user'''
    if os.environ.get("VIRTUAL_ENV"):
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(
            f"Virtual Environment: "
            # Extract the environment name from the path of the venv
            f"{get_environment_name(os.path.abspath(sys.prefix))}"
        )
        print(f"Environment Path: {os.path.abspath(sys.prefix)}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(build_site_packages_path(sys.prefix))
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
