import streamlit as st

# Title for the interface
st.title("Genetic Algorithm Parameter Input")

# Description
st.write("""
This interface allows you to configure the parameters for the Genetic Algorithm.
You can adjust the crossover rate (CO_R) and mutation rate (MUT_R) within the specified ranges.
""")

# Input parameters with default values and ranges
CO_R = st.slider(
    label="Crossover Rate (CO_R)",
    min_value=0.0,
    max_value=0.95,
    value=0.8,
    step=0.01
)

MUT_R = st.slider(
    label="Mutation Rate (MUT_R)",
    min_value=0.01,
    max_value=0.05,
    value=0.02,
    step=0.001
)

# Display the selected values
st.write("### Selected Parameters")
st.write(f"- **Crossover Rate (CO_R):** {CO_R}")
st.write(f"- **Mutation Rate (MUT_R):** {MUT_R}")

# Placeholder for future integration with genetic algorithm logic
st.write("""
The values will be applied to the genetic algorithm logic once integrated.
""")
