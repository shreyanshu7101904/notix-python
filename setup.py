from setuptools import find_packages, setup
from os import path
current_dir = path.abspath(path.dirname(__file__))
with open(path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="notix-python",
    version="1.0.0",
    description="Python Notix Push notification wrapper",
    author="Shreyanshu Shankar",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email="shreyanshu7101904@gmail.com",
    url="https://github.com/shreyanshu7101904/notix-push-notification",
    packages=find_packages(include=["notix"]),
    install_requires=["requests"],
    setup_requires=["pytest-runner", "flake8"],
    tests_require=["pytest"],
)
