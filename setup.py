from setuptools import setup, find_packages

setup(
    name="deep-clone",
    version="0.0.1",
    py_modules=["deep_clone"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "reverse=deep_clone:main",
        ],
    },
    author="Rajan Gupta",
    author_email="96rajangupta@gmail.com",
    description="Deep clone specific folder from a GitHub repo",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rajan-personal/deep-clone",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
