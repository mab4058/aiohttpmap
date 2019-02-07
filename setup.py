from setuptools import find_packages
from setuptools import setup

version = '0.2.0'

setup(name='aiohttpmap',
      version=version,
      description='Asynchronously handle bulk http requests.',
      author='Michael Bayer',
      author_email='mab4058@gmail.com',
      url='https://github.com/mab4058/aiohttpmap',
      download_url='https://github.com/mab4058/aiohttpmap/tarball/master',
      license='MIT',
      install_requires=['aiohttp>=3.0.0,<4.0.0'],
      python_requires='>=3.6',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages())
