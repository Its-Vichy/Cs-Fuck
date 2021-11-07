from setuptools import *

setup(
    name='Cs-Fuck',
    description='Cs-Fuck MultiHack',
    version='0.0.2',
    author='Sofia, Its-Vichy',
    python_require='>=3.0',
    packages=find_packages(),
    install_package_data=True,
    install_requires=[
        'pystyle',
        'pynput',
        'pymem',
        'requests',
        'json'
    ]
)
