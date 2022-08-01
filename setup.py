import io
import os

from setuptools import find_packages, setup

NAME = "delivery_service"
DESCRIPTION = ""
URL = ""
EMAIL = "rajughorai41410@gmail.com"
AUTHOR = "Raju Ghorai"
REQUIRES_PYTHON = ">=3.10.0"
VERSION = "1.0.0"
REQUIRE = ["typer[all]", "pydentic", "pytest"]

EXTRA = {"Code Formationg": ["black", "isort"]}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRE,
    extras_require=EXTRA,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
