from setuptools import setup, find_packages

setup(
    name="negotiaX",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
        "langchain",
        "langchain_groq",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "negotiaX=main:main",
        ],
    },
)
