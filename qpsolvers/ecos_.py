#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2020 Stephane Caron <stephane.caron@normalesup.org>
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

"""Solver interface for ECOS"""

from typing import Optional
from warnings import warn

from ecos import solve
from numpy import ndarray
from scipy import sparse

from .socp import convert_to_socp


__exit_flag_meaning__ = {
    0: "OPTIMAL",
    1: "PRIMAL INFEASIBLE",
    2: "DUAL INFEASIBLE",
    -1: "MAXIT REACHED",
}


def ecos_solve_qp(
    P, q, G=None, h=None, A=None, b=None, initvals=None, verbose: bool = False, **kwargs,
) -> Optional[ndarray]:
    """
    Solve a Quadratic Program defined as:

    .. math::

        \\begin{split}\\begin{array}{ll}
        \\mbox{minimize} &
            \\frac{1}{2} x^T P x + q^T x \\\\
        \\mbox{subject to}
            & G x \\leq h                \\\\
            & A x = h
        \\end{array}\\end{split}

    using `ECOS <https://github.com/embotech/ecos>`_.

    Parameters
    ----------
    P : numpy.array
        Primal quadratic cost matrix.
    q : numpy.array
        Primal quadratic cost vector.
    G : numpy.array
        Linear inequality constraint matrix.
    h : numpy.array
        Linear inequality constraint vector.
    A : numpy.array, optional
        Linear equality constraint matrix.
    b : numpy.array, optional
        Linear equality constraint vector.
    initvals : numpy.array, optional
        Warm-start guess vector (not used).
    verbose : bool, optional
        Set to `True` to print out extra information.

    Returns
    -------
    x : array, shape=(n,)
        Solution to the QP, if found, otherwise ``None``.
    """
    if initvals is not None:
        warn("note that warm-start values ignored by this wrapper")
    c_socp, G_socp, h_socp, dims = convert_to_socp(P, q, G, h)
    if A is not None:
        A_socp = sparse.hstack([A, sparse.csc_matrix((A.shape[0], 1))], format="csc")
        solution = solve(c_socp, G_socp, h_socp, dims, A_socp, b, verbose=verbose)
    else:
        solution = solve(c_socp, G_socp, h_socp, dims, verbose=verbose)
    flag = solution["info"]["exitFlag"]
    if flag != 0:
        warn(f"ECOS returned exit flag {flag} ({__exit_flag_meaning__[flag]})")
        return None
    return solution["x"][:-1]
