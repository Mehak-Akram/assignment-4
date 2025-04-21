import streamlit as st
import random
import time

def naive_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

st.title("🔍 Naive vs Binary Search Performance Checker")

st.write("""
Compare the speed of **Naive Search** and **Binary Search** on a random list!

- **Naive Search** checks each item one-by-one.
- **Binary Search** quickly narrows down a sorted list.

Pick a list size and number to search — see which one wins! 🚀
""")

list_size = st.slider("Select List Size", 1000, 100000, 10000, step=1000)

search_target = st.number_input(
    "Enter Number to Search (between 1 and list size)",
    min_value=1,
    max_value=list_size,
    value=min(5000, list_size)
)

random_list = random.sample(range(1, list_size + 1), list_size)
sorted_list = sorted(random_list)

if st.button("Run Search Test"):

    start_naive = time.time()
    result_naive = naive_search(random_list, search_target)
    end_naive = time.time()
    naive_time = end_naive - start_naive

    start_binary = time.time()
    result_binary = binary_search(sorted_list, search_target)
    end_binary = time.time()
    binary_time = end_binary - start_binary

    st.subheader("📊 Results:")
    st.write(f"**Naive Search:** {'Found at index ' + str(result_naive) if result_naive != -1 else 'Not Found'}")
    st.write(f"**Time Taken:** {naive_time:.6f} seconds")

    st.write("---")

    st.write(f"**Binary Search:** {'Found at index ' + str(result_binary) if result_binary != -1 else 'Not Found'}")
    st.write(f"**Time Taken:** {binary_time:.6f} seconds")

    st.write("---")

    winner = "Binary Search 🏆" if binary_time < naive_time else "Naive Search 🏆"
    st.subheader(f"🥁 And the winner is: **{winner}**!")


#footer

st.markdown("""
---
<div style="text-align:center">
    Made with ❤️ by Mehak Akram | © 2025 🚀
</div>
""", unsafe_allow_html=True)
