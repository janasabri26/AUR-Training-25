from setuptools import setup

package_name = 'my_turtle_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=['my_turtle_pkg'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/turtle_chase_launch.py']),  
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='janasabri26',
    maintainer_email='janasabri26@gmail.com',
    description='TurtleChase game package',
    license='MIT',
    entry_points={
        'console_scripts': [
            'turtle_chase=my_turtle_pkg.turtle_chase:main',
        ],
    },

)
