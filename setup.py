import os

from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as _f:
        return _f.read()


setup(
    author="Benjamin Staneck",
    author_email="staneck@gmail.com",
    description="Custom HTML anchor slogs for Python-Markdown",
    install_requires=["Markdown~=3.0"],
    keywords="markdown html anchor slug",
    license="MIT",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    name="pymdown_custom_slugs",
    packages=find_packages(exclude=['tools', 'test*']),
    python_requires=">=3.6",
    version="0.0.2",
    url="https://github.com/Stanzilla/pymdown-custom-slugs",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)