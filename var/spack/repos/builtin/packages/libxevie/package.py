# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libxevie(AutotoolsPackage):
    """Xevie - X Event Interception Extension (XEvIE)."""

    homepage = "http://cgit.freedesktop.org/xorg/lib/libXevie"
    url      = "https://www.x.org/archive/individual/lib/libXevie-1.0.3.tar.gz"

    version('1.0.3', sha256='3759bb1f7fdade13ed99bfc05c0717bc42ce3f187e7da4eef80beddf5e461258')

    depends_on('libx11')
    depends_on('libxext')

    depends_on('xproto', type='build')
    depends_on('xextproto', type='build')
    depends_on('evieext', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
