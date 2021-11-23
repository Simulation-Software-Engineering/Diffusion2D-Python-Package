from setuptools import setup
import setuptools
import versioneer

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="brenchladiffusion2D",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Larissa Brencher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LarissaBrencher/Diffusion2D-Python-Package",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["numpy", "matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
    ]
)
