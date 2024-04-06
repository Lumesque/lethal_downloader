from setuptools import setup

setup(
    name='lethal_md',
    version='1.0.0',
    entry_points={
        'console_scripts': ['lethal_md=downloader.cli.lethal_md:main'],
    },
    install_requires=[
        "attrs==23.2.0",
        "certifi==2024.2.2",
        "h11==0.14.0",
        "idna==3.6",
        "outcome==1.3.0.post0",
        "PySocks==1.7.1",
        "selenium==4.19.0",
        "sniffio==1.3.1",
        "sortedcontainers==2.4.0",
        "trio==0.25.0",
        "trio-websocket==0.11.1",
        "typing_extensions==4.11.0",
        "urllib3==2.2.1",
        "wsproto==1.2.0",
    ]
)
