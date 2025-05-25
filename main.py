import streamlit as st

from Views.graph import show_graph
from Views.newton_v import show_newton
from Views.secante_v import show_secant
from Views.bisection_v import show_bisection
from Views.false_rule_v import show_regula_falsi
from Views.incremental_v import show_incremental
from Views.gauss_no_pivot_v import show_gauss_jordan_no_pivot
from Views.gauss_partial_pivot_v import show_gauss_jordan_partial_pivot
from Views.gauss_total_pivot_v import show_gauss_jordan_total_pivot
from Views.LU_v import show_LU_factorization
from Views.PLU_v import show_PLU_factorization
from Views.jacobi_v import show_Jacobi
from Views.vandermonde_v import show_vandermonde
from Views.newton_div_diff_v import show_newton_divided_diff
from Views.lagrange_v import show_lagrange
from Views.spline_v import show_spline
from Views.gauss_seidel_v import show_gauss_seidel
from Views.Spline_Quadratic_View import show_quadratic_spline
from Views.fixed_point_v import show_fixed_point
from Views.multiple_roots_v import show_multiple_roots
from Views.SOR_v import show_SOR
from Views.spline_cubic_v import show_cubic_spline

if "page" not in st.session_state:
    st.session_state.page = "main"

def main():
    st.set_page_config(
        page_title="Numerical Methods",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("Chapter 1: Finding Roots")
    st.sidebar.title("Navigation")
    st.sidebar.markdown("[Bisection Method](#bisection-method)")
    st.sidebar.markdown("[False Position Method](#false-position-method)")
    st.sidebar.markdown("[Newton's Method](#newtons-method)")
    st.sidebar.markdown("[Secant Method](#secant-method)")
    st.sidebar.markdown("[Fixed Point Iteration](#fixed-point-iteration)")
    st.sidebar.markdown("[Multiple roots Method](#multiple-roots-method)")

    st.title("Chapter 2: Solving systems of equations")
    st.sidebar.markdown("[Gauss Elimination Simple Method](#gauss-elimination-method)")
    st.sidebar.markdown("[Gauss Elimination with Partial Pivoting](#gauss-elimination-with-partial-pivoting)")
    st.sidebar.markdown("[Gauss Elimination Total Pivot Method](#gauss-elimination-total-pivot-method)")
    st.sidebar.markdown("[LU Decomposition Method](#lu-decomposition-method)")
    st.sidebar.markdown("[PLU Method](#plu-method)")
    st.sidebar.markdown("[Gauss Seidel Method](#gauss-seidel-method)")
    st.sidebar.markdown("[Jacobi Method](#jacobi-method)")
    st.sidebar.markdown("[SOR Method](#sor-method)")

    st.title("Chapter 3: Interpolation")
    st.sidebar.markdown("[Lagrange Interpolation](#lagrange-interpolation)")
    st.sidebar.markdown("[Newton's Divided Difference Interpolation](#newtons-divided-difference-interpolation)")
    st.sidebar.markdown("[Spline Linear](#spline-linear-interpolation)")
    st.sidebar.markdown("[Spline cubic](#spline-cubic-interpolation)")