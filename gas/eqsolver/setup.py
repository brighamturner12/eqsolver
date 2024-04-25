from setuptools import setup, find_packages

with open("README.md", "r") as fh: 
    long_description = fh.read() 

setup(
    name='eqsolver',
    version='0.2.2',
    author='Brigham Turner',
    author_email='brighamturner12@gmail.com',
    description='Define model from system of equations, algebraically solve for variables, calculate boiling point, latent heat, other physics gas concepts',
    long_description=long_description, 
    long_description_content_type="text/markdown", 
    packages=find_packages(),
    license="MIT",
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)