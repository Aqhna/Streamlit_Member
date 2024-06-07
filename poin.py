import pandas as pd
import streamlit as st
import base64

# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Function to convert image to base64 for background use
def get_img_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Main function
def main():
    # Load CSV file
    @st.cache_data  # Cache the dataframe for faster access
    def load_data(file_path):
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return pd.DataFrame()
        
    #Ganti alamat data yang sesuai
    file_path = "/Streamlit_member/member.csv"
    df = load_data(file_path)

    # Convert logo image to base64
    logo_path = "/Streamlit_member/Lampiran/logo1.jpg"
    logo_base64 = get_base64_image(logo_path)

    # Sidebar logo
    st.sidebar.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Sidebar title with background
    st.sidebar.markdown(
        """
        <h1 style='
            text-align: center; 
            font-size: 30px; 
            background-color: #FFC000; 
            padding: 5px; 
            border-radius: 1px;
        '>MENU</h1>
        """, 
        unsafe_allow_html=True
    )
    # Replace 'sidebar2.png' with the path to your sidebar image
    img_base65 = get_img_as_base64("/Streamlit_member/Lampiran/back10.png")
    img_base64 = get_img_as_base64("/Streamlit_member/Lampiran/back1.png")

    # Use base64 image data as sidebar background
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url('data:image/png;base64,{img_base64}');
        background-size: cover;
    }}

    [data-testid="stHeader"]  {{ 
        background-color: rgba(0, 0, 0, 0)
    }}

    [data-testid="stSidebar"] {{
        background-image: url('data:image/png;base64,{img_base65}');
        background-size: cover;
        color: white; /* Change text color on sidebar */
    }}

    /* Bold text in sidebar */
    .css-1d391kg p {{
        font-weight: bold;
    }}

    /* Enlarge and center sidebar title */
    .css-1d391kg h1 {{
        text-align: center;
        font-size: 30px;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Sidebar menu
    menu = st.sidebar.radio("-", ("Data Pembelian", "Katalog Promo", "Katalog Point" ))

    if menu == "Data Pembelian":
        
        # Main content with background title
        st.markdown(
            """
            <h1 style='
                text-align: Left; margin-bottom: 50px;
                font-size: 30px; 
                background-color: #FFC000; 
                padding: 5px; 
                border-radius: 1px;
            '>Data Pembelian</h1>
            """, 
            unsafe_allow_html=True
        )
         # Sidebar with selectbox for kode member
        kode_member = st.selectbox("Pilih Kode Member", sorted(df['Kode Member'].unique()))
        st.write(f"Tampilan data pembelian untuk Kode Member: {kode_member}")
        
    

        # Filter dataframe based on selected kode member
        filtered_df = df[df['Kode Member'] == kode_member]

        # Display data pembelian
        st.write(filtered_df)

        # Calculate total jumlah belanja and total poin
        total_belanja = filtered_df['Total Belanja'].sum()
        total_point = filtered_df['Point'].sum()

        # Display total jumlah belanja and total poin
        st.write(f"Total Jumlah Belanja: {total_belanja}")
        st.write(f"Total Point: {total_point}")

        # Redeem Points
        st.header("Cairkan Point?")
        st.write("Hubungi CS 08XX XXXX XXXX atau Langsung Datangi Toko")

    elif menu == "Katalog Point":
        # Example catalog items with images
        katalog = {
            "Topi": {"points": 200, "image": "/Streamlit_member/Lampiran/image1.jpg"},
            "Totebag": {"points": 400, "image": "/Streamlit_member/Lampiran/image2.jpg"},
            "Kipas": {"points": 1000, "image": "/Streamlit_member/Lampiran/image3.jpg"},
            "Kompor": {"points": 2000, "image": "/Streamlit_member/Lampiran/image4.jpg"},
            "Macbook M1": {"points": 100000, "image": "/Streamlit_member/Lampiran/image5.jpg"}
        }

        # Display all catalog items
        st.markdown(
            """
            <h1 style='
                text-align: Left; margin-bottom: 20px;
                font-size: 30px; 
                background-color: #FFC000; 
                padding: 5px; 
                border-radius: 1px;
            '>Katalog Point</h1>
            """, 
            unsafe_allow_html=True
    )

        st.markdown("Berikut adalah daftar barang-barang yang dapat ditukar dengan point:")

        for item, details in katalog.items():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(details["image"], width=150)  # Adjust width as needed
            with col2:
                st.markdown(
                    f"""
                    <div style='display: flex; align-items: center; height: 100%; font-size: 20px;'>
                        {item} - {details['points']} Poin
                    </div>
                    """, 
                    unsafe_allow_html=True
                )

    elif menu == "Katalog Promo":
        # Example discount catalog items with images
        sembako_katalog = {
            "Beras Jasmine 5 Kg": {"original_price": 84000, "discounted_price": 74000, "image": "/Streamlit_member/Lampiran/promo1.jpg"},
            "Bimoli 2 L": {"original_price": 58000, "discounted_price": 42000, "image": "/Streamlit_member/Lampiran/promo2.jpg"},
            "Gulaku 500 Gr": {"original_price": 13000, "discounted_price": 8700, "image": "/Streamlit_member/Lampiran/promo3.jpg"},
            "Terigu Segitiga Biru 1 Kg": {"original_price": 18000, "discounted_price": 13000, "image": "/Streamlit_member/Lampiran/promo4.jpg"},
            "Khong Ghuan": {"original_price": 140000, "discounted_price": 127000, "image": "/Streamlit_member/Lampiran/promo5.jpg"}
        }

        # Display all discount catalog items
        st.markdown(
            """
            <h1 style='
                text-align: Left; margin-bottom: 20px;
                font-size: 30px; 
                background-color: #FFC000; 
                padding: 5px; 
                border-radius: 1px;
            '>Katalog Promo</h1>
            """, 
            unsafe_allow_html=True
        )
        st.markdown("Berikut adalah daftar barang-barang promo terbatas!!!!:")


        for item, details in sembako_katalog.items():
            st.markdown(
                f"""
                <div style='display: flex; align-items: center; margin-bottom: 20px;'>
                    <div style='flex: 1;'>
                        <img src="data:image/png;base64,{get_base64_image(details['image'])}" width="150">
                    </div>
                    <div style='flex: 2;'>
                        <h3>{item}</h3>
                        <p>Harga Asli: Rp {details['original_price']}</p>
                        <p>Harga Diskon: Rp {details['discounted_price']}</p>
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )
        
         # Example "Beli 2 Gratis 1" catalog items with images
        beli_2_gratis_1_katalog = {
            "Pantene PRO-V 70 Ml": {"harga": 21000, "image": "/Streamlit_member/Lampiran/Promo6.jpg"},
            "Kecap Manis Bango 135 Ml": {"harga": 12000, "image": "/Streamlit_member/Lampiran/promo7.jpg"},
            "Kapal Api Special Mix 360 Gr": {"harga": 35000, "image": "/Streamlit_member/Lampiran/promo8.jpg"}
        }

        for item, details in beli_2_gratis_1_katalog.items():
            st.markdown(
                f"""
                <div style='display: flex; align-items: center; margin-bottom: 20px;'>
                    <div style='flex: 1;'>
                        <img src="data:image/png;base64,{get_base64_image(details['image'])}" width="150">
                    </div>
                    <div style='flex: 2;'>
                        <h3>{item}</h3>
                        <p>Harga: Rp {details['harga']}</p>
                        <p>Promo: Beli 2 Gratis 1</p>
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
if __name__ == "__main__":
    main()
