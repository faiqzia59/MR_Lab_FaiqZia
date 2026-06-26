import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'my_launch_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # ✅ Install ALL launch files
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='faiqi',
    maintainer_email='2022mc59@student.uet.edu.pk',
    description='Launch package for turtle follower',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            # ✅ follower node executable
            'follow_turtle = my_launch_pkg.follow_turtle:main',
        ],
    },
)
