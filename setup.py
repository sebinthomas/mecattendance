from setuptools import setup, find_packages
from mecattendance import __version__

setup(
    name='mecattendance',
    version=__version__,
    description='Script to scrape attendance info from mec.ac.in/attn',
    author='Sebin Thomas',
    author_email='me@sebin.in',
    url='http://github.com/stc043/mecattendance',
    packages = find_packages(),
    install_requires=['BeautifulSoup >= 3.2.1']
    include_package_data=True,
)
