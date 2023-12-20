from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return requirements from requirement.txt
    '''    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]
     
    
setup(
    name='mlprojects',
    version='0.0.1',
    author='Aashish Pant',
    author_email='aashishpnt@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)