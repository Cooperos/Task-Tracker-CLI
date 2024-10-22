from setuptools import find_packages, setup

setup(
    name="task-cli",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "task-cli = main:main",
        ],
    },
    python_requires=">=3.6",
    install_requires=[
        "tabulate",
    ],
)
