import streamlit as st

# Website Configuration
st.set_page_config(page_title="Khadija's Homemade Cakes", page_icon="🎂", layout="wide")

# Stylish Header
st.markdown(
    """
    <h1 style='text-align: center; color: #FF4081; font-size: 50px;'>Welcome to Khadija's Homemade Cakes 🎂</h1>
    <h3 style='text-align: center; color: #FF7043; font-size: 30px;'>Freshly Baked with Love</h3>
    <p style='text-align: center; color: #4A148C; font-size: 20px; background-color: #FFE0B2; padding: 15px; border-radius: 15px; font-weight: bold;'>Indulge in the richness of our soft, creamy, and freshly baked cakes. 
    Made with premium ingredients and a touch of love, our cakes are perfect for every occasion. 
    Order now and experience the ultimate delight! 🍰</p>
    """,
    unsafe_allow_html=True
)

# Display Cake Images with Prices
st.write("### Our Special Cakes")

images = [
    ("./images/chocolate.jpg", "Rs. 1500"),
    ("./images/cake_02.jpg", "Rs. 1800"),
    ("./images/cake_03.png", "Rs. 1500"),
    ("./images/cake_04.jpg", "Rs. 1600"),
    ("./images/image_05.jpg", "Rs. 1500"),
    ("https://d3cif2hu95s88v.cloudfront.net/live-site-2016/product-image/2023/16744611114-350x350.jpg", "Rs. 1700"),
    ("./images/cake_07.jpg", "Rs. 1600"),
    ("./images/cake_08.jpg", "Rs. 1800"),
    ("./images/swsqaxkj.png", "Rs. 1500"),
    ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9vhj6z20ofBQB--EjrF9DCdUsyeaaPN1ZRg&s", "Rs. 1600"),
    ("./images/cake_09.png","Rs, 1500"),
    
]

# Dynamically create rows with 3 images per row
for i in range(0, len(images), 3):
    cols = st.columns(3)  # Creates a row of 3 columns
    for j in range(3):
        if i + j < len(images):  # Ensure we don't go out of bounds
            with cols[j]:
                st.image(images[i + j][0], use_container_width=True)
                st.markdown(f"<p style='text-align: center; font-size: 18px; color: #4A148C; font-weight: bold;'>Price: {images[i + j][1]}</p>", unsafe_allow_html=True)
                st.markdown(f"""
                <div style='text-align: center; margin-top: 10px;'>
                    <a href='https://docs.google.com/forms/d/1sIDamgbGWFkZHRDwEam7chyw1gV14ATRc8c9nbC2y80/viewform' 
                       target='_blank' 
                       style='text-decoration: none;'>
                        <button style='background-color: #FF4081; color: white; padding: 10px 20px; font-size: 18px; border: none; border-radius: 10px; cursor: pointer; transition: 0.3s;'>
                            🛒 Order Now
                        </button>
                    </a>
                </div>
          """, unsafe_allow_html=True)




# Footer Section
st.markdown("""
    <hr style='border: 2px solid #FF4081;'>
    <p style='text-align: center; color: #4A148C; font-size: 18px; font-weight: bold;'>
        © 2025 Khadija's Homemade Cakes | Made with ❤️ by Khadija
    </p>
    <p style='text-align: center; font-size: 16px;'>
        📞 Contact: <a href='tel:+923001234567' style='color: #FF4081; text-decoration: none;'>0314-3504308</a> | 
        📧 Email: <a href='mailto:khadijascakes@gmail.com' style='color: #FF4081; text-decoration: none;'>dijaduaa@gmail.com</a>
    </p>
    <p style='text-align: center; font-size: 16px;'>
        📍 Location: Karachi, Pakistan
    </p>
""", unsafe_allow_html=True)










