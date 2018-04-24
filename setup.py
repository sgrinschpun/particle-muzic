from distutils.command.install_data import install_data

packages = ['phenomena', ]
#scripts = ['bin/myapp',]
#cmdclasses = {'install_data': install_data}
data_files = [('/etc', ['other/scripts/test.py'])]

setup_args = {
    'name': 'phenomena',
    'version': '0.1',
    'packages': packages,
#    'cmdclass': cmdclasses,
    'data_files': data_files,
#    'scripts': scripts,
#    'include_package_data': True,
#    'test_suite': 'nose.collector'
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**setup_args)