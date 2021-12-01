from setuptools import setup


DEV_PACKAGES = [
    "black==20.8b1",
    "flake8>=3.8.1",
    "isort>=4.3.21",
    "ipython>=7.30.0",
]

setup(
    name="aoc",
    description="Advent of code helpers",
    version="0.1",
    extras_require={"dev": DEV_PACKAGES},
    packages=["aoc"]
)

