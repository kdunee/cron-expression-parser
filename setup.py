from setuptools import setup, find_packages

setup(
    name="cron_expression_parser",
    version="1.0.0",
    packages=find_packages(),
    scripts=['bin/cron_expression_parser'],
    python_requires='>=3.7',
    maintainer='Kosma Dunikowski',
    maintainer_email='kosmadunikowski@gmail.com',
    extras_require={
        'test': ['pytest']
    }
)