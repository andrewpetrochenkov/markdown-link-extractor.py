import setuptools

setuptools.setup(
    name='markdown-link-extractor',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
