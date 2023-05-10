from setuptools import setup, find_packages

DEPENDENCIES = [
    'wheel',
    'dnspython',
    'pymongo[srv]',
    'pydantic>=1.8.2',
]
DEV_DEPENDENCIES = [
    'pipenv',
    'pytest',
    'python-dotenv'
]

setup(
    name='MongoPie',
    version='0.1.0',
    author='Xiyuan Chen',
    description="MongoPie is a OOP Python library for MongoDB.",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    extras_require={
        'dev': DEV_DEPENDENCIES
    },
    keywords=['MongoDB', 'OOP', 'Python'],
    url='https://github.com/GareArc/MongoPie.git',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)