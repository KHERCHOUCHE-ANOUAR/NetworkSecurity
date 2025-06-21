from setuptools import setup, find_packages
from typing import List



def get_requirements() -> List[str]:
    """
    Reads a requirements file and returns a list of requirements.
    :param file_path: Path to the requirements file.
    :return: List of requirements.
    """

    requirements_list : List[str]= []
    try:
        with open('requirements.txt', 'r') as file:
            requirements = file.readlines()
            for line in requirements:
                line = line.strip()
                if line and not line.startswith('-e .'):
                    requirements_list.append(line)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the current directory.")
    return requirements_list



setup(
    name='networksecurity',
    version='0.0.1',
    author='Anouar kherchouche',
    author_email='kherchoucheanouar98@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)



