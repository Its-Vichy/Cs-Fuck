from setuptools import *

setup(
    name='Cs-Fuck',
    description='Cs-Fuck MultiHack',
    version='0.0.4',
    author='Its-Vichy, Sofia',
    python_require='>=3.0',
    packages=find_packages(),
    install_package_data=True,
    install_requires=[
        'pyfade',
        'pymem',
        'requests'
    ]
)
