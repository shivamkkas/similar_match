import streamlit as st
from fuzzywuzzy import process

# Define the array of items
items = ['Algeria','US', 'UK', 'Canada','Zimbabwe','Malaysia ','Germany', 'France','Armenia', 'Japan', 'Australia', 'China', 'India']

# Function to find the closest match
def find_closest_match(user_input, items):
    closest_match, similarity = process.extractOne(user_input, items)
    return closest_match, similarity

# Streamlit app
def main():
    st.title("Find Closest Match")
    user_input = st.text_input("Type a country or item:")
    
    if user_input:
        closest_match, similarity = find_closest_match(user_input, items)
        st.write(f"Closest match: {closest_match}")
        st.write(f"Similarity: {similarity}%")

if __name__ == "__main__":
    main()
