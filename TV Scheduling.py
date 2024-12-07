import streamlit as st

def main():
    st.title("Genetic Algorithm Parameter Input")

    # User input for Crossover Rate (CO_R)
    co_r = st.slider(
        label="Crossover Rate (CO_R)",
        min_value=0.0,
        max_value=0.95,
        value=0.8,
        step=0.01
    )

    # User input for Mutation Rate (MUT_R)
    mut_r = st.slider(
        label="Mutation Rate (MUT_R)",
        min_value=0.01,
        max_value=0.05,
        value=0.2,
        step=0.01
    )

    st.write("### Selected Parameters:")
    st.write(f"- **Crossover Rate (CO_R):** {co_r}")
    st.write(f"- **Mutation Rate (MUT_R):** {mut_r}")

if __name__ == "__main__":
    main()
