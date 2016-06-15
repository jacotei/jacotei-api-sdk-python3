from setuptools import setup
from setuptools import find_packages

setup(name='jacotei_api',
    version='1.0.0',
    description='Jacotei_api',
    url='https://github.com/jacotei/jacotei-api-sdk-python3',
    author='JaCotei',
    author_email='',
    license='MIT',
    packages=find_packages(),
    install_requires=['request'],
    zip_safe=False)
