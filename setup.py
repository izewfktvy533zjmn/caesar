from setuptools import setup, find_packages


setup(
    name='caesar',
    version='0.0.0',
    description='unlabored scheme interpreter',

    author='Taichi Soma',
    author_email='izewfktvy533zjmn@gmail.com',

    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
