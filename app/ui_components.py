import streamlit as st
from PIL import Image
import io

ICON = "🥗"

# Page config with icon
st.set_page_config(page_title="NutriScan AI", page_icon=ICON, layout="centered")

def show_header():
    col1, col2 = st.columns([1, 8])
    with col1:
        # Show the icon as a big emoji (you can adjust font-size via HTML)
        st.markdown(f"<h1 style='font-size:48px; margin-bottom:0;'>{ICON}</h1>", unsafe_allow_html=True)
        # Or replace above with image if you have a logo
    with col2:
        st.markdown(
            "<h1 style='margin-bottom: 0;'>NutriScan AI - Food Nutritional Analyzer</h1>", 
            unsafe_allow_html=True
        )

def upload_image_ui():
    return st.file_uploader("Upload Food Image", type=["jpg", "jpeg", "png"])

def prompt_input_ui():
    default_prompt = """You are a certified nutritionist and expert in dietary analysis. Carefully analyze the uploaded food image using visual cues.

# Perform the following tasks step-by-step:

# ---

# ### 1. Food Identification
# - List all clearly identifiable food items on the plate.
# - If an item is ambiguous or unclear, label it as "uncertain" or "not clear".

# ### 2. Portion Size Estimation
# - Estimate the portion size for each item (e.g., grams, cups, slices).
# - Infer preparation methods if possible (e.g., grilled, fried, boiled).

# ### 3. Nutritional Breakdown
# For each food item, estimate the following:
# - **Calories (kcal)**
# - **Protein (g)**
# - **Carbohydrates (g)**
# - **Sugars (g)**
# - **Fats (g)**
# - **Saturated Fats (g)**
# - **Fiber (g)**
# - **Sodium (mg)**
# - **Water content (%)** (if visually estimable)

# Clearly state if values are approximations or unclear.

# ---

# ### 4. Health Assessment
# For each item:
# - Assess whether it is **beneficial**, **neutral**, or **potentially unhealthy**.
# - Mention suitability for common diets (e.g., vegan, keto, diabetic-friendly, low-sodium).
# - Recommend **alternative ingredients or preparation methods** if needed (e.g., steamed instead of fried).
# - Use evidence-based dietary advice.

# ---

# ### 5. Summarization
# At the end, provide a concise summary that includes:
# - An overall **health rating** of the meal (e.g., "Generally healthy", "Balanced but needs improvement", "Not ideal for regular consumption").
# - Key takeaways regarding the **meal's nutritional balance**.
# - **Suggestions to improve** the dish, including:
#   - What to add (e.g., healthy fats like olive oil, more fiber via vegetables or whole grains)
#   - What to remove or reduce (e.g., refined carbs, excess sauces, fried items)

# ---

# ### 6. Format
# - Use a **structured table** for the food items and their nutritional info.
# - Use **bullet points** for health observations and suggestions.
# - Be visually clear, practical, and informative.
# - Add disclaimers where estimation is used due to image limitations.

# Focus on accuracy, clarity, and actionable health insights.
"""
    return st.text_area("📝 Enter your prompt", value=default_prompt, height=100)

def display_results(result: str, uploaded_file):
    st.markdown("### 🖼️ Uploaded Image")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # st.image(image, use_container_width=True)
        st.image(image, caption="Your Meal", use_container_width=True)

    st.markdown("### 🤖 Analysis Results")
    st.write(result)
