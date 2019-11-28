import setuptools

setuptools.setup(
    name='byte-size-string-handler',
    version='1.0.0',
    author='Ricardo Mendes',
    author_email='ricardolsmendes@gmail.com',
    description='Handle Python strings according to their size in bytes',
    platforms='Posix; MacOS X; Windows',
    packages=setuptools.find_packages(where='./src'),
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    setup_requires=(
        'pytest-runner',
    ),
    tests_require=(
        'pytest-cov',
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
