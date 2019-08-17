from distutils.core import setup

setup(
    name='libkloudtrader',
    version='1.0.0',
    author='KloudTrader',
    author_email='admin@kloudtrader.com',
    packages=['libkloudtrader'],
    url='https://github.com/KloudTrader/kloudtrader',
    license='LICENSE',
    description="kloudTrader's in-house library that makes it much easier for you to code algorithms that can trade for you.",
    long_description_content_type="text/markdown",
    long_description='pypi.md',
    install_requires=[
        "requests",
        "boto3",
        "pandas",
        "numpy",
        "pyti",
        "scipy",
        "empyrical",
        "tabulate",
        "ta",
        "TA-Lib",
        "streamz"
    ],
)
