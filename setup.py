from setuptools import setup

setup(
    name="pytest-santa",
    version="0.1.0",
    description="Infers types and generates test data from the respective type with Monkeytype and Hypothesis.",
    long_description=open("README.md").read(),
    author="Enpu You, Haeley Griffin, Sweta Rauniyar, Alex Korzeniwsky, Issac Barrezueta",
    author_email="youe2@allegheny.edu, griffinh@allegheny.edu, rauniyars@allegheny.edu, barrezuetai@allegheny.edu, korzeniwskya@allegheny.edu",
    url="https://github.com/inTestiGator/pytest-santa",
    license="GNU",
    platforms="any",
    py_modules=[
        "pytest-santa",
    ],
    entry_points={
        'pytest11': ['santa = pytest-santa'],
    },
    install_requires=[
        'pytest>=3.5',
    ],
)
