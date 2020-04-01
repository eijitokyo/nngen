from __future__ import absolute_import
from __future__ import print_function

import os
import sys

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

import nngen as ng
import veriloggen

import onnx_matrix_mul


a_shape = (15, 15)
b_shape = (15, 1)
a_dtype = ng.int16
b_dtype = ng.int16
c_dtype = ng.int16
par = 1
axi_datawidth = 32


def test(request, silent=True):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    rslt = onnx_matrix_mul.run(a_shape, b_shape,
                               a_dtype, b_dtype, c_dtype,
                               par, axi_datawidth, silent,
                               filename=None, simtype=simtype,
                               outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')

    verify_rslt = rslt.splitlines()[-1]
    assert(verify_rslt == '# verify: PASSED')


if __name__ == '__main__':
    rslt = onnx_matrix_mul.run(a_shape, b_shape,
                               a_dtype, b_dtype, c_dtype,
                               par, axi_datawidth, silent=False,
                               filename='tmp.v',
                               outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')
    print(rslt)
