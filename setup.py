import os
import setuptools
from setuptools.command.build_ext import build_ext
import subprocess


class cmake_build_ext(build_ext):
    def build_extensions(self):
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['cmake', '-DBUILD_SHARED_LIBS=1', '../../'], cwd=self.build_temp)
        subprocess.check_call(['make', 'bssl'], cwd=self.build_temp)
        ext_path = self.get_ext_fullpath('boringssl')
        subprocess.check_call(['cp', self.build_temp + '/ssl/libssl.so', ext_path])


setuptools.setup(
    name='boringssl-binary-build',
    version='0.0.6',
    author="Jonatron",
    author_email="jon.ath.4n+boring@gmail.com",
    description='Build BoringSSL',
    long_description='Build BoringSSL',
    package_dir={"boringssl_binary_build": "."},
    packages=["boringssl_binary_build"],
    python_requires='>=3.6',
    ext_modules=[setuptools.extension.Extension('boringssl', sources=[])],
    cmdclass={'build_ext': cmake_build_ext},
)
