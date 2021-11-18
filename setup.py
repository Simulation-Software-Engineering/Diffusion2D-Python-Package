from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ostertmsdiffusion2D',
    version='0.0.1',
    description='Diffusion2D-Python-Package',
    author='Ishaan Desai, Magnus Ostertag',
    url='https://github.com/MagnusOstertag/Diffusion2D-Python-Package',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
    ],
    install_requires=['matplotlib', 'numpy'],
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
