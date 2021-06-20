from setuptools import find_packages, setup

setup(
    name="notix-python",
    version="0.0.1",
    description="Python Notix Push notification wrapper",
    author="Shreyanshu Shankar",
    long_description_content_type="text/markdown",
    author_email="shreyanshu7101904@gmail.com",
    url="https://github.com/shreyanshu7101904/notix-push-notification",
    packages=find_packages(include=["notix"]),
    install_requires=["requests"],
    setup_requires=["pytest-runner", "flake8"],
    tests_require=["pytest"],
)
