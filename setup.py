from setuptools import setup, find_packages

setup(
    name="necta",
    version="1.0.0",
    author="Ivan Nazarov",
    author_email="nazarovv676@gmail.com",
    description="This is a bot for saving, changing, and reviewing phone contacts and notes. The bot supports various commands to manage contacts and notes efficiently.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nazarovv676/neo-team-proj1",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "prompt_toolkit",
        "tabulate",
        "wcwidth"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
