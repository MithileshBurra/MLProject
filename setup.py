from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_req(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, "r") as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Mithilesh',
    author_email='mithileshburra@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)
