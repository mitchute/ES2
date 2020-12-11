import codecs
from pathlib import Path

from setuptools import setup, find_packages

from enstore import VERSION

this_dir = Path(__file__).parent
with codecs.open(this_dir / "README.MD", encoding="utf-8") as ld_file:
    long_description = ld_file.read()

with codecs.open(this_dir / "LICENSE", encoding="utf-8") as lic_file:
    enstore_license = lic_file.read()

setup(
    name="EnStoreRefactorPrototype",
    author="Matt Mitchell",
    license=enstore_license,
    long_description=long_description,
    version=VERSION,
    packages=find_packages(exclude=["test", "tests", "test.*"]),
    long_description_content_type='text/markdown',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    python_requires=">=3.5"
)
