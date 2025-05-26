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

st.set_page_config(
        page_title="Numerical Methods",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded",
    )

st.markdown("""
    <style>
    /* Fondo general y texto */
    .stApp {
        background-color: #0a192f;  /* azul oscuro */
        color: white;
    }

    /* Sidebar fondo y texto */
    section[data-testid="stSidebar"] {
        background-color: #112240;  /* azul oscuro más claro */
        color: white;
    }

    /* Títulos */
    h1, h2, h3, h4, h5, h6 {
        color: white;
    }

    /* Inputs y selects */
    input, textarea, select {
        color: white !important;
        background-color: #1c2c4c !important;
        border: 1px solid #ffffff33;
    }

    /* Selectbox desplegado */
    .stSelectbox div[role="button"] {
        background-color: #1c2c4c !important;
        color: white !important;
    }

    /* Botones */
    .stButton>button {
        background-color: #2563eb;  /* azul */
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #1e40af;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "main"

def main():
    st.sidebar.subheader("This are the methods available in this app:")
    st.sidebar.subheader("Chapter 1: Finding Roots")
    st.sidebar.markdown("- Bisection Method")
    st.sidebar.markdown("- False Position Method")
    st.sidebar.markdown("- Newton's Method")
    st.sidebar.markdown("- Secant Method")
    st.sidebar.markdown("- Fixed Point Iteration")
    st.sidebar.markdown("- Multiple roots Method")

    st.sidebar.subheader("Chapter 2: Solving Systems of Equations")
    st.sidebar.markdown("- Gauss Elimination Simple Method")
    st.sidebar.markdown("- Gauss Elimination with Partial Pivoting")
    st.sidebar.markdown("- Gauss Elimination Total Pivot Method")
    st.sidebar.markdown("- LU Decomposition Method")
    st.sidebar.markdown("- PLU Method")
    st.sidebar.markdown("- Gauss Seidel Method")
    st.sidebar.markdown("- Jacobi Method")
    st.sidebar.markdown("- SOR Method")

    st.sidebar.subheader("Chapter 3: Interpolation")
    st.sidebar.markdown("- Lagrange Interpolation")
    st.sidebar.markdown("- Newton's Divided Difference Interpolation")
    st.sidebar.markdown("- Spline Linear")
    st.sidebar.markdown("- Spline cubic")
    st.sidebar.markdown("- Spline Quadratic")

    st.header("Numerical Methods App: Menu")
    col1,col2,col3,col4, col5 = st.columns(5)

    with col1:
        if st.button("🏠Home"):
            st.session_state.page = "main"
    with col2:
        if st.button("📈Graph"):
            st.session_state.page = "graph"
    with col3:
        if st.button("Finding roots"):
            st.session_state.page = "roots"
    with col4:
        if st.button("Solving systems of equations"):
            st.session_state.page = "systems"
    with col5:
        if st.button("Interpolation"):
            st.session_state.page = "interpolation"

    if st.session_state.page == "main":
        st.write("In this app you can find the different numerical methods used to solve mathematical problems viewed in class.")
        st.write("Select a method from the menu to get started.")
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

if __name__ == "__main__":
    main()
# This is the main entry point for the application.

