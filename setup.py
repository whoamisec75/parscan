import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "parscan",
    version = "1.0",
    author = "Devansh Raghav",
    author_email = "whoamisec75@gmail.com",
    license = "MIT",
    keywords = ["parscan", "Bug Bounty", "pentesting", "security", "hacking"],
    url = "https://github.com/DevanshRaghav75/parscan",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    install_requires=[
        'colorama',
        'requests'
    ],
    package_data={'parscan': ['db/*']},
    entry_points={
        'console_scripts': [
            'parscan = parscan.__main__:main'
        ]
    },
)