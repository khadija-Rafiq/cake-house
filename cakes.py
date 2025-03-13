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
    ("https://lh7-us.googleusercontent.com/deUjCibeWOmmP61DEhu8yXmJdLWee_zshcSJwDuMTnCuopoc9MMLbZ-YnS7sHmzfQCjPutJ1XW7Xp1k-y50_1Z2R4bfV1kTyvDqiqt3qv6j0m1yAxjHphWuIPrwNyhbB99NpjJyX33rAetGo17Jm6ZzYDprtYA", "Rs. 1500"),
    ("https://cdn.discordapp.com/attachments/1308751107971092500/1349654249025437757/IMG-20250113-WA0044_3.jpg?ex=67d3e2f8&is=67d29178&hm=5f5b282e05744b92f609faf006afa7e3888c1aefbcb7102994575e0ca68aedd9&", "Rs. 1800"),
    ("https://cdn.discordapp.com/attachments/1308751107971092500/1349651644417052732/Screenshot_20250313-123945.png?ex=67d3e08b&is=67d28f0b&hm=4a8a858ff3d6881f0517e3f3c936fe18546f1e392dad3fe5ab5022d96937ba14&", "Rs. 1500"),
    ("https://cdn.discordapp.com/attachments/1308751107971092500/1349651090030727178/Snapchat-127766736_1.jpg?ex=67d3e007&is=67d28e87&hm=965a7a01f2f1261896bb1dc1b1b3865b34aaad160ae6c699c5bf2d60e0f79cef&", "Rs. 1600"),
    ("https://cdn.discordapp.com/attachments/1308751107971092500/1349651090244898838/IMG_20240905_204533_275.jpg?ex=67d3e007&is=67d28e87&hm=9578b817f21e811c4ab625dda04d680594a1223db5fa0d25e8dd59ba1016fc59&", "Rs. 1500"),
    ("https://d3cif2hu95s88v.cloudfront.net/live-site-2016/product-image/2023/16744611114-350x350.jpg", "Rs. 1700"),
    ("https://cdn.discordapp.com/attachments/1308751107971092500/1349661401546887168/Snapchat-315069217_1.jpg?ex=67d3e9a1&is=67d29821&hm=a96603ef431af8db7e50ed5416519f33d6279e97365e33e1d8726954e9f2183e&", "Rs. 1600"),
    ("https://media.discordapp.net/attachments/1308751107971092500/1349661402293604374/Snapchat-292868761_1.jpg?ex=67d3e9a1&is=67d29821&hm=73fd58611007ed4c46fa51fa9f9ad28acfd3814837936f6d71e70e2d67f13e05&=&format=webp&width=492&height=421", "Rs. 1800"),
    ("https://media.discordapp.net/attachments/1308751107971092500/1349661402553516032/Snapchat-104276027_2.jpg?ex=67d3e9a1&is=67d29821&hm=07efb334a720807de3d168200fcabe6d73556cbcc9998c46fa064c68bfa2a280&=&format=webp&width=397&height=421", "Rs. 1500"),
    ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9vhj6z20ofBQB--EjrF9DCdUsyeaaPN1ZRg&s", "Rs. 1600"),
    ("https://cdn.discordapp.com/attachments/1308751107971092500/1349676283956564008/Screenshot_20250313-132915_1.png?ex=67d3f77d&is=67d2a5fd&hm=5d3001d90febd7fed67a3cda123ae6c1fa3e176d25ab8833e1010d8caf6737d3&","Rs, 1500"),
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
