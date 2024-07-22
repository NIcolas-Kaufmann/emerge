from setuptools import setup, find_packages

setup(
    name='emerge',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, for example:
        'requests',
        'numpy',
        'scipy'
    ],
    include_package_data=True,
    package_data={
        'emerge': ['data/*.dat'],
    },
    author='Nicolas Kaufmann',
    author_email='nicolas.kaufmann@unibe.ch',
    description='Porvides the results from my papet () to inform when the embryos reach the tranisiton mass',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NIcolas-Kaufmann/emerge',  # Replace with your package's homepage
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
