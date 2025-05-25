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
from Views.spline_quadratic_v import show_quadratic_spline
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
    st.sidebar.markdown("[Spline Quadratic](#spline-quadratic-interpolation)")

    st.sidebar.title("Navigation")

    if st.sidebar.button("Home"):
        st.session_state.page = "main"
    if st.sidebar.button("Graph"):
        st.session_state.page = "graph"
    if st.sidebar.button("Finding roots"):
        st.session_state.page = "roots"
    if st.sidebar.button("Solving systems of equations"):
        st.session_state.page = "systems"
    if st.sidebar.button("Interpolation"):
        st.session_state.page = "interpolation"

    if st.session_state.page == "main":
        main()
    elif st.session_state.page == "graph":
        show_graph()
    elif st.session_state.page == "roots":
        st.title("Finding Roots")
        root_method = st.selectbox(
            "Select a method to find roots:",
            [
                "Bisection Method",
                "False Position Method",
                "Newton's Method",
                "Secant Method",
                "Fixed Point Iteration",
                "Multiple Roots Method"
            ]
        )
        if root_method == "Bisection Method":
            show_bisection()
        elif root_method == "False Position Method":
            show_regula_falsi()
        elif root_method == "Newton's Method":
            show_newton()
        elif root_method == "Secant Method":
            show_secant()
        elif root_method == "Fixed Point Iteration":
            show_fixed_point()
        elif root_method == "Multiple Roots Method":
            show_multiple_roots()

    elif st.session_state.page == "systems":
        st.title("Solving Systems of Equations")
        system_method = st.selectbox(
            "Select a method to solve systems of equations:",
            [
                "Gauss Elimination Method",
                "Gauss Elimination with Partial Pivoting",
                "Gauss Elimination Total Pivot Method",
                "LU Decomposition Method",
                "PLU Method",
                "Gauss Seidel Method",
                "Jacobi Method",
                "SOR Method"
            ]
        )
        if system_method == "Gauss Elimination Method":
            show_gauss_jordan_no_pivot()
        elif system_method == "Gauss Elimination with Partial Pivoting":
            show_gauss_jordan_partial_pivot()
        elif system_method == "Gauss Elimination Total Pivot Method":
            show_gauss_jordan_total_pivot()
        elif system_method == "LU Decomposition Method":
            show_LU_factorization()
        elif system_method == "PLU Method":
            show_PLU_factorization()
        elif system_method == "Gauss Seidel Method":
            show_gauss_seidel()
        elif system_method == "Jacobi Method":
            show_Jacobi()
        elif system_method == "SOR Method":
            show_SOR()

    elif st.session_state.page == "interpolation":
        st.title("Interpolation Methods")
        interpolation_method = st.selectbox(
            "Select an interpolation method:",
            [
                "Lagrange Interpolation",
                "Newton's Divided Difference Interpolation",
                "Spline Linear Interpolation",
                "Spline Cubic Interpolation",
                "Spline Quadratic Interpolation"
            ]
        )
        if interpolation_method == "Lagrange Interpolation":
            show_lagrange()
        elif interpolation_method == "Newton's Divided Difference Interpolation":
            show_newton_divided_diff()
        elif interpolation_method == "Spline Linear Interpolation":
            show_spline()
        elif interpolation_method == "Spline Cubic Interpolation":
            show_cubic_spline()
        elif interpolation_method == "Spline Quadratic Interpolation":
            show_quadratic_spline()


