import streamlit as st

def main():
    st.title("Crop Disease Classification and Treatment Recommendation System for Amravati District")
    st.write("Objective: The goal of this project is to develop a robust crop disease classification system using machine learning techniques. The primary objective is to accurately identify and classify diseases affecting various crops, enabling early detection and timely intervention for crop protection.")

    # Create three buttons side by side
    col1, col2, col3 = st.beta_columns(3)  # Using beta_columns to create two columns

    if col1.button("Vegetable Plant"):
        st.success("Website that provide useful information on growing vegetables https://krishi.maharashtra.gov.in/")
        st.write("Click Here --> [Vegetable Plant Website](https://jmukhgbdnz4wjhe3xxqwim.streamlit.app/)")

    if col2.button("Cash Crop"):
        st.success("Website that provide useful information on growing Cotton Plant https://krishi.maharashtra.gov.in/")
        st.write("Click Here --> [Cash Crop Website](https://vs2gugcmvthjkgg3kxinmj.streamlit.app/)")

    if col3.button("Cash Crop (BETA)"):
        st.success("Note - This website may not give you an accurate result because, its under development")
        st.write("Click Here --> [Cash Crop [BETA] Website]( https://cpddpy-92wtupr5nwgiuhb4idnh9q.streamlit.app/)")

if __name__ == "__main__":
    main()
