from setuptools import setup


setup(
    name="Python-Elm",
    version="0.0.3",
    license='BSD',
    url='https://github.com/volker48/Python-ELM',
    description='Extreme Learning Machine',
    author='David C. Lambert',
    py_modules=['elm', 'random_layer'],
    install_requires=['numpy', 'scipy', 'sklearn'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]

)
