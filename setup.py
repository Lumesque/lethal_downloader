from setuptools import setup

setup(
    name='lethal_md',
    version='1.0.0',
    entry_points={
        'console_scripts': ['lethal_md=downloader.cli.lethal_md:main'],
    }
)
