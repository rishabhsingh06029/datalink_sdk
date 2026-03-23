from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A lightweight, unified database connector SDK for Python."

setup(
    name="datalink-sdk",
    version="1.0.0",
    author="DataLink SDK Contributors",
    description="A lightweight, unified database connector SDK for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rishabhsingh06029/datalink_sdk",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "mysql-connector-python>=8.0.0",
        "psycopg2-binary>=2.9.0",
        "pymongo>=4.0.0",
        "redis>=4.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="database connector sdk mysql postgres mongodb redis datalink",
)