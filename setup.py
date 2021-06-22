from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="scipy_calculator",
    version="1.0.0",
    description="A Scientific calculator",
    py_modules=["calculator"],
    package_dir={"": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/komus/scipy_calculator",
    author="Oyindolapo Komolafe",
    author_email="oyindolapokomolafe@yahoo.com",

    install_requires = [
        "multipledispatch ~= 0.6.0",
    ],

    extras_require = {
        "dev": [
            "pytest >= 3.7",
        ],
    },
)