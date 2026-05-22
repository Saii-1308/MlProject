#responsible for creating ml learning application as a package and installing it in the system and project build entire application and install it in the system
from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->list[str]:
    '''This function will return the list of requirements'''
    with open('requirements.txt') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-r')]        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ml_project',
    version='0.01',
    description='A machine Learning Project',
    author_name="sai jadhav",
    author_email="jadhavsai299@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)