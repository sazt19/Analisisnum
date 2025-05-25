import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
from interface import enter_function, calculate_tolerance, graph

def validate_fixed_point_function(x_symbol, f_function, g_function):
    """
    Validate fixed-point iteration requirements

    Args:
        x_symbol (sympy.Symbol): Variable symbol
        f_function (sympy.Expr): Original function f(x)
        g_function (sympy.Expr): Transformed function g(x)

    Returns:
        bool: Validation result
    """
    try:
        # Find roots of f(x)
       # roots = sp.solve(f_function, x_symbol)
        """
        # Check if g(root) = root for all roots of f(x)
        for root in roots:
            transformed_root = g_function.subs(x_symbol, root)
            if not sp.simplify(transformed_root - root).is_zero:
                st.error(f"Error: g(x) does not satisfy the fixed-point condition g(x) = x when f(x) = 0  at x = {root}.")
                return False
        """
        # Check convergence condition |g'(x)| < 1 around the roots
        g_derivative = sp.diff(g_function, x_symbol)
        for root in roots:
            derivative_value = g_derivative.subs(x_symbol, root)
            if abs(derivative_value) >= 1:
                st.warning(f"Warning: Convergence condition |g'(x)| < 1 is not satisfied at root = {root}.")

        return True
    except Exception as e:
        st.error(f"Error: Please check your inputs")
        print(e)
        return False

def show_fixed_point():
    st.markdown("""
    The **Fixed Point Iteration Method** finds roots by transforming $f(x) = 0$ to $x = g(x)$.
    """)
    with st.expander("📘 How the Fixed Point Method Works"):
        st.markdown("""
            **1. Rewrite the Function:**
            - Express $f(x) = 0$ as $x = g(x)$, where $g(x)$ is chosen to simplify computations and ensure convergence.

            **2. Choose an Initial Guess $x_0$:**
            - Select an initial guess $x_0$ close to the suspected root.

            **3. Apply the Iteration Formula:**
        """)
        st.latex(r"""
        x_{n+1} = g(x_n)
        """)
        st.markdown("""
            - Compute successive approximations $x_1, x_2, \dots$ by evaluating $g(x)$ at the previous point.

            **4. Check for Convergence:**
            - Stop the iteration when $|x_{n+1} - x_n|$ is less than a specified tolerance.

            **Convergence Conditions:**
            - The method converges if $|g'(x)| < 1$ for all $x$ in the interval of interest.
        """)
    st.header("Fixed-Point Iteration Method")
    try:
        col1, col2, col3 = st.columns(3)
        with col1:
            x = st.text_input(
                "Enter a Variable Name",
                value = "x",
                help="Enter a variable name to use in the function. Default is 'x'."
                )
        with col2:
        # Input for original function f(x)
            f_input = st.text_input(
                "Original Function f(x): ",
                value="x**2 - 4",
                help="Enter the function f(x) whose root you want to find."
            )
        with col3:
        # Input for transformed function g(x)
            g_input = st.text_input(
            "Transformation g(x): ",
            value="2/x",
            help="Enter g(x) such that g(x) = x at the root of f(x)."
            )

        # Initial guess input
        x0 = st.number_input(
            "Initial guess (x₀)",
            format="%.4f",
            value=2.0,
            step=0.0001,
            help="Provide the initial guess for the root."
        )

        # Tolerance and iteration settings
        tol, niter, tolerance_type = calculate_tolerance()
        st.markdown(f"**Calculated Tolerance:** {tol:.10f}")

        # Parse functions and variable
        x_symbol = sp.symbols(f'{x}')
        f_function = sp.sympify(f_input)
        g_function = sp.sympify(g_input)
    except Exception as e:
        st.error(f"Invalid function input: Please check your inputs")
        return

    """
    # Validate the functions
    if not validate_fixed_point_function(x_symbol, f_function, g_function):
        return
    """
    # Display the functions in LaTeX
    st.subheader("Functions")
    st.latex(f"f({x_symbol}) = {sp.latex(f_function)}")
    st.latex(f"g({x_symbol}) = {sp.latex(g_function)}")

    # Check convergence condition
    derivative = sp.diff(g_function, x_symbol)

    st.subheader("Derivative of g(x):")
    st.latex(derivative)

    # Lambdify the functions for numerical evaluations
    g = sp.lambdify(x_symbol, g_function, "numpy")
    f = sp.lambdify(x_symbol, f_function, "numpy")

    # Fixed-Point Iteration Algorithm
    st.subheader("Results")
    table_data = {"Iteration": [], "xₙ": [], "f(xₙ)": [], "Error": []}
    x_prev = x0
    converged = False

    try:
        for i in range(1, niter + 1):
            x_next = g(x_prev)
            f_value = f(x_next)
            error = abs(x_next - x_prev)

            # Append iteration data
            table_data["Iteration"].append(i)
            table_data["xₙ"].append(x_next)
            table_data["f(xₙ)"].append(f_value)
            table_data["Error"].append(error)

            # Check for divergence
            if np.isinf(x_next) or np.isnan(x_next) or abs(x_next) > 1e6:
                st.error("Method diverged. Try a different initial guess or transformation function g(x).")
                break

            # Check for convergence
            if error < tol:
                converged = True
                break

            x_prev = x_next

            print(converged)

        if converged:

             # Display results table
            result_df = pd.DataFrame(table_data)
            decimals = st.slider(
                "Select number of decimals to display on table",
                min_value=1,
                max_value=10,
                value=4,
                help="Adjust the number of decimal places for the result table."
            )
            result_display = result_df.style.format(f"{{:.{decimals}f}}")
            st.dataframe(result_display, use_container_width=True)

            st.success(f"Root found at x = {x_next:.{decimals}f}, f(x) = {f_value:.{decimals}f}")

    except Exception as e:
        st.error(f"Error: Please check your inputs {e}")

    graph(x,f_input)