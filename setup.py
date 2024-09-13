from setuptools import setup, find_packages

setup(
    name="atomic-apron",
    version="0.1.0-alpha.0",
    author="Kane McConnell",
    description="A toolkit for managing and organizing the AtomicApron recipe repository.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/kmcconnell/atomic-apron",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)