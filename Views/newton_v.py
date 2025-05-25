import streamlit as st
import sympy as sp
from interface import enter_function, calculate_tolerance, graph
from methods.newton import get_derivative, newton

def show_newton():

    st.markdown("""
    The **Newton-Raphson Method** is an iterative numerical technique used to find roots of a differentiable function 
    ${f(x)}$. It uses the tangent line at a given point to approximate the root of the function.

    This method is faster than the Bisection Method but requires the function to be differentiable and a good initial guess.
    """)

    with st.expander("📘 How the Newton-Raphson Method Works"):
        st.markdown("""
        **1. Choose an Initial Guess ${x_0}$ close to the suspected root**

        **2. Apply the Iteration Formula:**
        """)
        st.latex(r"""
        x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
        """)
        st.markdown("""
        - Here, ${f'(x_n)}$ is the derivative of ${f(x)}$ evaluated at ${x_n}$.
        - Compute the next approximation ${x_{n+1}}$.

        **3. Check for Convergence:**
        - Stop if ${|f(x_{n+1})|}$ is sufficiently close to zero or ${|x_{n+1} - x_n|}$ is less than a specified tolerance.

        **4. Repeat:**
        - Use ${x_{n+1}}$ as the new approximation and iterate until convergence.

        **Convergence:**
        - The Newton-Raphson Method converges quadratically if the initial guess ${x_0}$ is close to the root.
        - However, it may fail if ${f'(x_n) = 0}$ or if the initial guess is far from the root.
        """)


    try:
        st.header("Newton-Raphson Method")

        x, function_input = enter_function()



        x0 = st.number_input(
        "Initial Point (x_0)",
        format="%.4f",
        value = 0.1,
        step = 0.0001,
        help="The first initial guess for the root. It is a value where the function is evaluated."
        )


        tol, niter, tolerance_type = calculate_tolerance()
        st.markdown(f"**Calculated Tolerance:** {tol:.10f}")

        x = sp.symbols(f'{x}')
        function = sp.sympify(function_input)
        derivative = get_derivative(function)

        st.subheader("Function")
        st.latex(f"f({x}) = {sp.latex(function)}")
        st.subheader("Derivative")
        st.latex(f"f({x}) = {sp.latex(sp.sympify(derivative))}")

        function = sp.lambdify(x, sp.sympify(function_input), 'numpy')
        derivative = sp.lambdify(x, derivative, 'numpy')


        result = newton(x0, niter, tol, tolerance_type, function,  derivative)
        if result["status"] == "error":
            st.error(result["message"])
            return
        else:
            result = result["table"]

            # Add a slider to choose the number of decimals to display
        decimals = st.slider(
            "Select number of decimals to display on table",
            min_value=1,
            max_value=10,
            value=4,
            help="Adjust the number of decimal places for the result table."
        )
        # Format the dataframe to display the selected number of decimals
        result_display = result.style.format(f"{{:.{decimals}f}}")  # Use f-string to format dynamically

        mid = result.iloc[-1]['x_n']
        if function(mid) < 0 + tol:

            st.subheader("Results")
            st.dataframe(result_display, use_container_width=True)
            st.success(f"Root found at x = {mid:.{decimals}f}: f({mid:.{decimals}f}) = {function(mid):.{decimals}f}")
        else:
            st.warning(f"Method did not converge, potentially because of a discontinuity in the function.")


    except Exception as e:
        print(e)
        st.error("Error: Check your input")
    graph(x, function_input)