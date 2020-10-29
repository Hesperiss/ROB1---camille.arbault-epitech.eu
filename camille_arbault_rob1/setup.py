import os
from glob import glob
from setuptools import setup

package_name = 'camille_arbault_rob1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Include launch files
        ('share/' + package_name, ['launch/rob1.launch.py']),
        ('share/' + package_name, ['launch/map.launch.py']),

        # include resources
        ('share/' + package_name, ['resource/worlds/challenge_maze.world']),
        ##(os.path.join('share', package_name), glob('resource/models', recursive=True))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Camille Arbault',
    maintainer_email='camille.arbault@epitech.eu',
    description='ROB1 module',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rob1 = camille_arbault_rob1.main:main',
        ],
    },
)