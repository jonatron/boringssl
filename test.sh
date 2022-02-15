#!/bin/bash -ex

echo "hello `date` world"
echo "TEST_ENV: $TEST_ENV ."
echo "TEST_WITH_ENV: $TEST_WITH_ENV ."
echo "Length of TWINE_USERNAME ${#TWINE_USERNAME} ."
find /opt/python
cd /github/workspace/
echo "TWINE_USERNAME: $TWINE_USERNAME ."
yum -y install golang
/opt/python/cp36-cp36m/bin/python setup.py bdist_wheel
auditwheel show dist/*.whl
auditwheel repair dist/*.whl
/opt/python/cp36-cp36m/bin/pip install twine
mv wheelhouse/*manylinux*.whl wheelhouse/boringssl_binary_build-0.0.6-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
/opt/python/cp36-cp36m/bin/twine upload --verbose --repository testpypi wheelhouse/*manylinux*.whl
