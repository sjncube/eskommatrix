from setuptools import setup, find_packages

setup(
    name='eskommatrix',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Analyse Predict python package',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/sjncube/eskommatrix.git',
    author='<Sizwe Ncube>',
    author_email='<micanjohnscoderx@gmail.com>'
)