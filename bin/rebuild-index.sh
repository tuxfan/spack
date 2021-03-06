#!/bin/bash

# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

set -x

SPACK_BIN_DIR="${CI_PROJECT_DIR}/bin"
export PATH="${SPACK_BIN_DIR}:${PATH}"

spack buildcache update-index -d "$MIRROR_URL"
