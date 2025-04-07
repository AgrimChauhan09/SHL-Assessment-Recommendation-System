# # app.py
# import streamlit as st
# import pandas as pd

# # from knowledge_graph import SHLKnowledgeGraph  # Assuming this class has the recommend_assessments method
# from knowledge_graph_and_training.knowledge_graph import SHLKnowledgeGraph


# st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

# st.title("SHL Assessment Recommendation System")
# st.write("Enter competencies to get recommended assessments.")

# # Load your model/data
# @st.cache_resource
# def load_knowledge_graph():
#     return SHLKnowledgeGraph('cleaned_data.csv')  # your cleaned CSV

# kg = load_knowledge_graph()

# # Input competencies
# competencies = st.text_input("Enter competencies (comma-separated):", placeholder="e.g., communication, leadership, teamwork")

# if st.button("Recommend Assessments"):
#     if competencies.strip() == "":
#         st.warning("Please enter at least one competency.")
#     else:
#         # Preprocess input
#         competencies_list = [comp.strip() for comp in competencies.split(",")]
        
#         # Get recommendations
#         try:
#             recommendations = kg.recommend_assessments(competencies_list)  # Assuming this method exists
#             if recommendations:
#                 st.success("Assessments Recommended:")
#                 for idx, assessment in enumerate(recommendations, 1):
#                     st.write(f"{idx}. {assessment}")
#             else:
#                 st.error("No matching assessments found. Try different competencies.")
#         except Exception as e:
#             st.error(f"Error while recommending: {e}")



# main.py
import streamlit as st
import pandas as pd

# Import from the renamed folder
from knowledge_graph_and_training.knowledge_graph import SHLKnowledgeGraph

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

st.title("SHL Assessment Recommendation System")
st.write("Enter competencies to get recommended assessments.")

# Load your model/data
@st.cache_resource
def load_knowledge_graph():
    return SHLKnowledgeGraph('knowledge_graph_and_training/cleaned_data.csv')  # Adjusted path

kg = load_knowledge_graph()

# Input competencies
competencies = st.text_input(
    "Enter competencies (comma-separated):",
    placeholder="e.g., communication, leadership, teamwork"
)

if st.button("Recommend Assessments"):
    if competencies.strip() == "":
        st.warning("Please enter at least one competency.")
    else:
        # Preprocess input
        competencies_list = [comp.strip() for comp in competencies.split(",")]
        
        # Get recommendations
        try:
            recommendations = kg.recommend_assessments(competencies_list)
            if recommendations:
                st.success("Assessments Recommended:")
                for idx, assessment in enumerate(recommendations, 1):
                    st.write(f"{idx}. {assessment}")
            else:
                st.error("No matching assessments found. Try different competencies.")
        except Exception as e:
            st.error(f"Error while recommending: {e}")
