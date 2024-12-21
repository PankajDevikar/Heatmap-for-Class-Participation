from setuptools import setup, find_packages

setup(
    name='class_participation_heatmap',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
    ],
    description='A project to visualize class participation trends with a heatmap.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Minal Devikar',
    author_email='meenal.madankar@gmail.com',
    url='https://github.com/minalmmm/Heatmap-for-Class-Participation.git',
    classifiers=[
        'Programming Language :: Python :: 3.12.0',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
