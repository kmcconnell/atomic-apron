from setuptools import setup, find_packages

setup(
    name="recipyzer",
    version="0.1.0-alpha.4",
    author="Kane McConnell",
    description="A toolkit for managing and organizing the Recipyzer recipe repository.",
    long_description=open('./Recipyzer/README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/kmcconnell/recipyzer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'frontmatter'
    ],
    entry_points={
        'console_scripts': [
            'recipyzer=recipyzer.compile_metadata:main'
        ]
    }
)