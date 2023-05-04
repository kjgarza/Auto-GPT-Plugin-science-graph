from setuptools import setup, find_packages

setup(
    name='science-graph-plugin',
    version='0.0.1',
    description='A plugin for AutoGPT to access to all scholarly articles, publications, preprints, or works with a DOI, ORCID, ROR or other scholarly identifiers',
    author='Kristian Garza',
    author_email='kj.garza@gmail.com',
    url='https://github.com/kjgarza/science-graph-plugin',
    packages=find_packages(),
    install_requires=[
        'scholarly>=1.0,<2.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
