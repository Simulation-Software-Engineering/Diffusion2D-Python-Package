from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='bektassidiffusion2D',
    package_dir = {'': 'src'},
    packages=['bektassidiffusion2D'],
    version='0.0.8',
    url='https://github.com/Simulation-Software-Engineering/Diffusion2D-Python-Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
                    "Programming Language :: Python :: 3",
                    "Operating System :: POSIX :: Linux"
                ],
)