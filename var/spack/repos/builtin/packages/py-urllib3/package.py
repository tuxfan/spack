# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyUrllib3(PythonPackage):
    """HTTP library with thread-safe connection pooling, file post, and
    more."""

    homepage = "https://urllib3.readthedocs.io/"
    url = "https://pypi.io/packages/source/u/urllib3/urllib3-1.20.tar.gz"

    version('1.21.1', sha256='b14486978518ca0901a76ba973d7821047409d7f726f22156b24e83fd71382a5')
    version('1.20', sha256='97ef2b6e2878d84c0126b9f4e608e37a951ca7848e4855a7f7f4437d5c34a72f')
    version('1.14', sha256='dd4fb13a4ce50b18338c7e4d665b21fd38632c5d4b1d9f1a1379276bd3c08d37')

    depends_on('py-setuptools', type='build')
