import setuptools
from pathlib import Path

# Constants
AUTHOR_USER_NAME = "yassineiscoding"
REPO_NAME = "waterpurity"
SRC_REPO = "waterpurity"
AUTHOR_EMAIL = "yassine.elbadraoui@gmail.com"
__version__ = "0.0.0"
GITHUB_URL = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"

# Read long description from README.md
long_description = Path("README.md").read_text(encoding="utf-8")

# Setup arguments
setup_args = {
    "name": SRC_REPO,
    "version": __version__,
    "author": AUTHOR_USER_NAME,
    "author_email": AUTHOR_EMAIL,
    "description": "A small python package for ml app",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": GITHUB_URL,
    "project_urls": {
        "Bug Tracker": f"{GITHUB_URL}/issues"
    },
    "package_dir": {"": "src"},
    "packages": setuptools.find_packages(where="src"),
}



setuptools.setup(**setup_args)