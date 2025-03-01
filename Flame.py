import streamlit as st

def remove_common_letters(name1, name2):
    name1_list = list(name1)
    name2_list = list(name2)

    for letter in name1[:]:
        if letter in name2_list:
            name1_list.remove(letter)
            name2_list.remove(letter)

    return "".join(name1_list), "".join(name2_list)

def flames_game(count):
    
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]

    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames.pop()

    return flames[0]

# Streamlit UI
st.set_page_config(page_title="FLAMES Game", page_icon="🔥", layout="centered")

st.title("FLAMES Relationship Calculator")
st.write("Enter two names and find out your relationship status!")
name1 = st.text_input("Enter the first name", "").strip()
name2 = st.text_input("Enter the second name", "").strip()
if st.button("Calculate"):
    if name1 and name2:
        name1_cleaned, name2_cleaned = name1.replace(" ", "").lower(), name2.replace(" ", "").lower()
        name1_cleaned, name2_cleaned = remove_common_letters(name1_cleaned, name2_cleaned)
        count = len(name1_cleaned) + len(name2_cleaned)
        result = flames_game(count)
        st.success(f"The relationship between {name1.capitalize()} and {name2.capitalize()} is: {result}")
    else:
        st.error("Please enter both names before calculating.")
st.markdown("---")
st.markdown("**FLAMES Game** is just for fun! Enjoy! 😊")
