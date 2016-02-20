from setuptools import setup

setup(
    name='pretty_print_json',
    version='1.1.0',
    description='Tool for printing pretty JSON',
    long_description='Tool for printing pretty JSON',
    url='http://andrewshay.me',
    author='Andrew Shay',
    author_email='andrew.shay@andrewshay.me',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    ],
    packages=['pretty_print_json'],
    entry_points={
        'console_scripts': [
            'ppj = pretty_print_json.__main__:main'
        ],
    }
)
