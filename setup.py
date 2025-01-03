from setuptools import find_packages, setup

setup(
    name = "MlPipeline",
    version= "0.0.0",
    author="abhishek199677",
    author_email="puttapoguabhishek1007@gmail.com",
    packages= find_packages(),   #local packages in src where __init__.py is a constructor below to has all the packages which are the local packages
    install_requires=[]     #requirements are already listed in reqirements.txt file
)