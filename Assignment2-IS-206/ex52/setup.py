try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This is a test to check if you can move away, and live by yourself',
    'author': 'Marie Alstad',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'StartGame'
}

setup(**config)