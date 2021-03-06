"""
Test playground code for pyscf and psi4
"""
from taco.playground.fde_pyscf import run_co_h2o_pyscf_sto3g, run_co_h2o_pyscf_dz
from taco.playground.fde_pyscf import run_co_h2o_pyscf_dft_sto3g, run_co_h2o_pyscf_dft_dz
from taco.playground.fde_pyscf import run_co_h2o_pyscf_tz, run_co_h2o_pyscf_qz
from taco.playground.fde_pyscf import run_co_h2o_pyscf_dft_tz, run_co_h2o_pyscf_dft_qz
# from taco.playground.fde_psi4 import run_co_h2o_psi4_sto3g, run_co_h2o_psi4_dz
# from taco.playground.fde_psi4 import run_co_h2o_psi4_tz, run_co_h2o_psi4_qz


def test_playground_pyscf():
    run_co_h2o_pyscf_sto3g()
    run_co_h2o_pyscf_dz()
    run_co_h2o_pyscf_tz()
    run_co_h2o_pyscf_qz()
    run_co_h2o_pyscf_dft_sto3g()
    run_co_h2o_pyscf_dft_dz()
    run_co_h2o_pyscf_dft_tz()
    run_co_h2o_pyscf_dft_qz()
#
# def test_playground_psi4():
#     run_co_h2o_psi4_sto3g()
#     run_co_h2o_psi4_dz()
#     run_co_h2o_psi4_tz()
#     run_co_h2o_psi4_qz()
