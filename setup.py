from setuptools import setup

dependencies = [
    'seaborn',
    'statsmodels',
    'scipy',
    'patsy',
    'matplotlib',
    'pandas',
    'numpy'
  ]

VERSION = "0.3.4.2"

setup(
    name='pymatch',
    packages=['pymatch'],
    version=VERSION,
    description='Matching techniques for Observational Studies',
    author='eclee',
    author_email='ecleetw@gmail.com',
    url='https://github.com/eclee/pymatch',
    download_url='https://github.com/eclee/pymatch/archive/{}.tar.gz'.format(VERSION),
    keywords=['logistic', 'regression', 'matching', 'observational', 'study', 'causal', 'inference'],
    include_package_data=True,
    install_requires=dependencies
)
