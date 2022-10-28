from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in core_erp/__init__.py
from core_erp import __version__ as version

setup(
	name="core_erp",
	version=version,
	description="Unified Solution for Your Business Needs",
	author="Extension Technologies Pvt Ltd",
	author_email="hello@extensionerp.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
