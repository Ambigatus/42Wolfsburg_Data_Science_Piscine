from setuptools import setup, find_packages


setup(
    name='ft_package',
    version='0.0.1',
    author='Ambigatus',
    description='A sample test package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ambigatus',
    author_email='ddzuba@student.42wolfsburg.de',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'count_in_list=ft_package.count_in_list:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
