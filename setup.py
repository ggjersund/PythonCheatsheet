from setuptools import setup, find_packages

setup(
    name='python-cheatsheet',
    description='Python cheatsheet repository for testing, CI/CD and packaging.',
    version='0.0.1',
    author='ggjersund',
    license='MIT License',
    package_dir={'':'src'},
    packages=find_packages('src'),
    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
    ],
    python_requires='>=3.7',
    install_requires=[],
    url='https://github.com/ggjersund/python-cheatsheet'
)
