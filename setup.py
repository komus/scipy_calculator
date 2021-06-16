from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "scipy_calculator",
    version = "0.0.1",
    description = "Advanced python calculator",
    package_dir = {'', 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
     classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/komus/scipy_calculator",
    author="Oyindolapo Komolafe",
    author_email="",

    install_requires = [
        
    ],

    extras_require = {
        "dev": [
            "pytest >= 3.7",
            
        ],
    },
    )