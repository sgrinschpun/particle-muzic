from setuptools.command.install import install
from setuptools import find_packages
from distutils import log
from setuptools.command.install_scripts import install_scripts
import os

class OverrideInstall(install):

    def run(self):
        uid, gid = 0, 0
        mode = 0770
        install.run(self) # calling install.run(self) insures that everything that happened previously still happens, so the installation does not break!
        # here we start with doing our overriding and private magic ..
        log.info("Changing phenomenad daemon properties")
        os.chown("/etc/init.d/phenomenad", uid, gid)
        os.chmod("/etc/init.d/phenomenad", mode)


packages = ['phenomena']
#scripts = ['bin/myapp',]
#cmdclasses = {'install_data': install_data}
data_files = [('/etc/init.d/', ['other/utils/phenomenad'])]

setup_args = {
    'name': 'phenomena',
    'version': '0.1',
    'packages': find_packages(),
#    'cmdclass': cmdclasses,
    'data_files': data_files,
    'cmdclass':{'install': OverrideInstall}
#    'scripts': scripts,
#    'include_package_data': True,
#    'test_suite': 'nose.collector'
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**setup_args, install_requires=['mido'])