from setuptools import setup, find_packages


with open('requirements.txt') as requirements:
    install_requires = []
    dependency_links = []
    for line in requirements:
        if line.startswith('-e git+') or line.startswith('git+'):
            dependency_links.append(line)
        elif line.startswith('--'):
            pass
        else:
            install_requires.append(line)

setup(
    name='ytest',
    version='0.1.0',
    author='redmeters',
    author_email='support@redmeters.com',
    description='Yoctopuce test app',
    packages=find_packages(exclude=['test', 'scripts']),
    install_requires=install_requires,
    package_data={
        '': ['*.json', '*.c']
    },
    dependency_links=dependency_links
)
