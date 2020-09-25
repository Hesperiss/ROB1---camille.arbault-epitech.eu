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
            'start = camille_arbault_rob1.main:main',
        ],
    },
)
