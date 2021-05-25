#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2021 Stéphane Caron <stephane.caron@normalesup.org>
#
# This file is part of qpsolvers.
#
# qpsolvers is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# qpsolvers is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with qpsolvers. If not, see <http://www.gnu.org/licenses/>.

# This file allows the whole repository to act as a Python module when e.g.
# included as a git submodule inside a project. It incurs some redundant
# bookkeeping but some users find it useful.

from qpsolvers.qpsolvers import __version__
from qpsolvers.qpsolvers import available_solvers
from qpsolvers.qpsolvers import dense_solvers
from qpsolvers.qpsolvers import sparse_solvers
from qpsolvers.qpsolvers import solve_ls
from qpsolvers.qpsolvers import solve_qp
from qpsolvers.qpsolvers import solve_safer_qp

__all__ = [
    "__version__",
    "available_solvers",
    "dense_solvers",
    "sparse_solvers",
    "solve_ls",
    "solve_qp",
    "solve_safer_qp",
]
