import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
import json
import base64
import plotly.graph_objects as go
import random
import string
from PIL import Image
import smtplib
from email.mime.text import MIMEText


# Page configuration
st.set_page_config(page_title="Trieu Nguyen Khac", layout="wide")

# --- Custom Styling ---
st.markdown('<a name="home"></a>', unsafe_allow_html=True)

st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .project-box {
            padding: 1.5rem;
            background-color: #ffffff;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)



# Sidebar Navigation
# st.sidebar.title("🚀 Navigation")
# page = st.sidebar.radio("Go to", ["🏠 About me", "🛠️ Skills", "📂 Projects", "✉️ Contact"])

st.markdown('<h1 style="text-align: center;">Trieu Nguyen Khac</h1>', unsafe_allow_html=True)

AboutMe, Skills, Projects, Contact = st.tabs(["🏠 About me", "🛠️ Skills", "📂 Projects", "✉️ Contact"])

# --- Home Page ---
with AboutMe:
    # Profile section with images and info in 3 columns
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.image("./images/aboutme/avatar1.jpg")
        st.markdown("<h3 style='text-align: center;'>Who am I?</h3>", unsafe_allow_html=True)
        st.markdown("""
        I'm **TRIEU NGUYEN KHAC**, a lifelong learner with a passion for turning raw data into powerful, actionable insights. I love building scalable data pipelines, designing efficient systems, and bringing order to complexity. 
        
        My educational journey:
        - 🎓 Studying **Information Systems** at VNUHCM-University of Science
        - 💯 GPA: 3.30/4.00
        - 📅 Graduation: 08/2025

        """)

    with col2:
        st.image("./images/aboutme/avatar2.jpg")
        st.markdown("<h3 style='text-align: center;'>What I do?</h3>", unsafe_allow_html=True)
        st.markdown("""
        When I'm in flow, I'm building things I love:
        - 🧠 Designing data pipelines that scale  
        - 🛠️ Building apps for real-world insights — from meals to air quality to finance  
        - ⚙️ Automating with Airflow, Spark, and Docker  
        """)
        st.markdown("""
        When I'm not coding, I'm recharging in my own ways:
        - 🎧 Getting lost in music
        - 🏃‍♂️ Running 5Ks to reset and refocus
        - ⚽ Playing soccer — where teamwork comes alive
        """)

    with col3:
        st.image("./images/aboutme/avatar3.jpg")
        st.markdown("<h3 style='text-align: center;'>Why I do it?</h3>", unsafe_allow_html=True)
        # st.subheader("Why I do it?")
        st.markdown("""
        Because I believe in **building things that matter**.

        Whether it's cleaning messy data or shipping a working app, I find purpose in solving real-world problems with calm, creative engineering.

        I aspire to design systems that help others — not just smarter, but **kinder** ones.
        """)
        
    

    st.divider()
    st.markdown('<h3 style="text-align: center;">My Favorite Quote</h3>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.markdown("""
        <div style="text-align: center;">
        <div style="display: inline-block; text-align: left;">
        "You are the greatest project<br>
        you'll ever work on. <br>
        Restart, reset, refocus,<br>
        as many times as you need."<br>
        </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="text-align: center;">
        <div style="display: inline-block; text-align: left;">
        "To see a world in a grain of sand  <br>
        And a heaven in a wild flower,   <br>
        Hold infinity in the palm of your hand  <br>
        And eternity in an hour." <br>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="text-align: center;">
        <div style="display: inline-block; text-align: left;">
        "No result? Keep working.<br>
        Bad result? Keep working.<br>
        Great result? Keep working."<br>
        Consistency is key."<br>
        </div>
        </div>
        """, unsafe_allow_html=True)
    st.divider()
    
    
# --- Skills Page ---
with Skills:
    # st.title("🧠 My Skillset")
    st.markdown("<h1 style='text-align: center;'>🧠 My Skillset 🧠</h1>", unsafe_allow_html=True)

    # --- Technical Skills Section ---
    # st.subheader("💻 Technical Skills")
    st.markdown("### ⚙️ Programming Languages & Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Languages**")
        st.markdown("""
        ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
        ![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=postgresql&logoColor=white)
        ![C#](https://img.shields.io/badge/C%23-239120?style=flat&logo=c-sharp&logoColor=white)
        ![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=flat&logo=c%2B%2B&logoColor=white)
        """)

        st.markdown("**Libraries**")
        st.markdown("""
        ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
        ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
        ![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat&logo=apache-spark&logoColor=white)
        ![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat&logo=apache-kafka&logoColor=white)
        """)

    with col2:
        st.markdown("**Workflow & DevOps**")
        st.markdown("""
        ![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat&logo=apache-airflow&logoColor=white)
        ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
        ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
        """)
        
        st.markdown("**Productivity Tools**")
        st.markdown("""
        ![Notion](https://img.shields.io/badge/Notion-000000?style=flat&logo=notion&logoColor=white)
        ![Slack](https://img.shields.io/badge/Slack-4A154B?style=flat&logo=slack&logoColor=white)
        ![Trello](https://img.shields.io/badge/Trello-0052CC?style=flat&logo=trello&logoColor=white)
        """)

    st.divider()

    st.markdown("### 🛠️ Data Engineering")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Databases**")
        st.markdown("""
        ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
        ![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=flat&logo=microsoft-sql-server&logoColor=white)
        ![Oracle DB](https://img.shields.io/badge/Oracle_DB-F80000?style=flat&logo=oracle&logoColor=white)
        ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
        ![Neo4j](https://img.shields.io/badge/Neo4j-008CC1?style=flat&logo=neo4j&logoColor=white)
        """)

        st.markdown("**Big Data Technologies**")
        st.markdown("""
        ![Apache Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat&logo=apache-kafka&logoColor=white)
        ![Apache Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat&logo=apache-spark&logoColor=white)
        ![Hadoop](https://img.shields.io/badge/Hadoop-66CCFF?style=flat&logo=apache-hadoop&logoColor=black)
        """)

    with col2:        
        st.markdown("**Visualization**")
        st.markdown("""
        ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
        ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=power-bi&logoColor=black)
        """)
        
        # st.markdown("**Cloud Platforms**")
        # st.markdown("""
        # ![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white) (S3, CloudFront)
        # """)

    # --- Soft Skills Section ---
    st.divider()
    st.subheader("🤝 Soft Skills")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- 🗣️ **Communication**: Clear and effective communication")
        st.markdown("- 🤝 **Teamwork**: Collaborative in teams")
    with col2:
        st.markdown("- 👀 **Attention to Detail**: Thorough and precise in work")
        st.markdown("- 🔄 **Adaptability**: Quick to adjust and learn")

    st.divider()


# --- Projects Page ---
with Projects:

    # st.markdown("<h1 style='text-align: center;'>💼 Projects 💼</h1>", unsafe_allow_html=True)
    
    proj1, proj2, proj3, proj4 = st.tabs(["🍽️ BESTIE", "🌫️ US AQI Analysis", "💳 Credit Card System", "Live Weather Event Alert"])
    
    # ========== PROJECT 1 ==========
    with proj1:
        st.markdown(
            """
            <div style='display: flex; flex-direction: column; align-items: center; margin-bottom: 0.5rem;'>
                <h3 style='text-align: center; margin-bottom: 0.2rem;'>🍽️ BESTIE - Personal Meal Planner 🍽️</h3>
                <span style='color: #888; font-size: 1rem;'>(Jan 2025 - Present)</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### ❓ What should I eat today?")
            st.markdown("""
            A simple question that millions of people ask every day — whether for health, convenience, or curiosity.

            **BESTIE** is your smart personal assistant for daily meal planning.  
            It doesn't just tell you what to eat — it learns your preferences and helps you eat better.
        """)
        with col2:
            st.markdown("### 🤖 How does BESTIE help?")
            st.markdown("""
            Recommends personalized meal plans based on your dietary goals, allergies, and taste. <br>
            Uses machine learning to generate optimized, diverse meal combos. <br>
            Automates data processing from food databases to nutritional analysis to planning.
            """, unsafe_allow_html=True)
        st.divider()
        st.markdown(""" <h3 style='text-align: center;'>Just set your goal — BESTIE handles the rest.</h3>""", unsafe_allow_html=True)
        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔧 What's under the hood?")
            st.markdown("""
            - Designed a **hybrid database architecture** integrating **PostgreSQL** & **MongoDB** for scalability  
            - Built a **recommendation engine** using machine learning for personalization  
            - Improved data quality with **automated validation and standardization**  
            - Designed a **cloud-native microservices architecture** with Docker & Kubernetes  

            **Technologies:**  
            ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
            ![Java](https://img.shields.io/badge/Java-007396?style=flat&logo=java&logoColor=white)
            ![Rust](https://img.shields.io/badge/Rust-000000?style=flat&logo=rust&logoColor=white)
            ![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat&logo=flutter&logoColor=white)
            ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
            ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
            ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
            """)
        with col2:
            st.markdown("### 📊 What's inside the database?")

            st.markdown("""
            - **Dishes:**  
                - Over **2,000+ Vietnamese dishes**  
                - Covers a wide range of **categories** (main courses, side dishes, desserts, snacks, beverages, etc.)  
                - Sourced from multiple reputable Vietnamese recipe collections and food databases  
            - **Ingredients:**  
                - Every ingredient is annotated with **comprehensive nutrition data** (calories, macronutrients, vitamins, minerals, etc.)  
                - Supports **multiple measurement units** (grams, ml, pieces, cups, etc.) for flexible planning and accurate tracking  
            """)

        # Reordered categories for better logical grouping and flow
        category_types = [
            "Daily Menu",         # General, everyday meals
            "Weekend",            # Special/weekend menus
            "Savory Dishes",      # General savory category
            "Stir-fried Dishes",  # Cooking method
            "Seafood",            # Main ingredient group
            "Fish",               # Subgroup of seafood
            "Shrimp",             # Subgroup of seafood
            "Pork",               # Main ingredient group
            "Eggs",               # Main ingredient group
            "Mushrooms"           # Main ingredient group
        ]
        category_counts = [1087, 950, 612, 298, 332, 284, 284, 417, 362, 360]

        # Create DataFrame
        category_df = pd.DataFrame({
            "Category": category_types,
            "Count": category_counts
        })
        fig1 = px.pie(category_df, names="Category", values="Count", title="Vietnamese Dish Diversity by Category")
        st.plotly_chart(fig1, use_container_width=True)

        # Nutrition data coverage
        nutrition_df = pd.DataFrame({
            "Nutrient": [
                "Calories", "Protein", "Fat", "Carbs",
                "Fiber", "Calcium", "Iron", 
                "Phosphorous", "Vitamin C", "Vitamin A"
            ],
            "Coverage (%)": [100, 100, 100, 100, 85.07, 83.77, 76.52, 74.20, 69.13, 56.52]
        })

        fig3 = px.bar(
            nutrition_df,
            x="Nutrient",
            y="Coverage (%)",
            title="Nutrition Data Coverage per Ingredient",
            text="Coverage (%)"
        )
        st.plotly_chart(fig3, use_container_width=True)


        st.markdown("<h3 style='text-align: center;'>🖼️ Application Snapshots</h3>", unsafe_allow_html=True)       
        # Convert image to base64
        def get_base64_image(path):
            with open(path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()

        # Load image paths
        image_paths = [
            "./images/projects/bestie/screen1.png",
            "./images/projects/bestie/screen2.png",
            "./images/projects/bestie/screen3.png",
            "./images/projects/bestie/screen4.png",
            "./images/projects/bestie/screen5.png",
            "./images/projects/bestie/screen6.png"
        ]

        # Convert images to base64 strings
        images_base64 = [get_base64_image(p) for p in image_paths]

        # HTML + JS for Swiper carousel with embedded base64 images
        carousel_html = f"""
        <link rel="stylesheet" href="https://unpkg.com/swiper@10/swiper-bundle.min.css" />

        <style>
        .swiper {{
            width: 100%;
            height: 400px;
            margin-bottom: 10px;
        }}
        .swiper-slide {{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .swiper-slide img {{
            max-height: 360px;
            width: auto;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        </style>

        <div class="swiper mySwiper">
        <div class="swiper-wrapper">
            {''.join([f'<div class="swiper-slide"><img src="data:image/png;base64,{b64}" /></div>' for b64 in images_base64])}
        </div>
        <div class="swiper-pagination"></div>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
        </div>

        <script src="https://unpkg.com/swiper@10/swiper-bundle.min.js"></script>
        <script>
        const swiper = new Swiper(".mySwiper", {{
            slidesPerView: 3,
            spaceBetween: 20,
            loop: true,
            pagination: {{
            el: ".swiper-pagination",
            clickable: true,
            }},
            navigation: {{
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
            }},
            breakpoints: {{
            0: {{ slidesPerView: 1 }},
            768: {{ slidesPerView: 2 }},
            1024: {{ slidesPerView: 3 }},
            }}
        }});
        </script>
        """

        
        # Render carousel
        components.html(carousel_html, height=450, scrolling=False)
        
        st.divider()
       
        
    # ========== PROJECT 2 ==========
    with proj2:
        st.markdown(
            """
            <div style='display: flex; flex-direction: column; align-items: center; margin-bottom: 0.5rem;'>
                <h3 style='text-align: center; margin-bottom: 0.2rem;'>🌫️ US AQI Analysis 🌫️</h3>
                <span style='color: #888; font-size: 1rem;'>(Sep 2024 - Dec 2024)</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        

        # --- Overview & Technologies Section (2 columns) ---
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("### ❓ What is this project about?")
            st.markdown("""
            The **US AQI Analysis** project focuses on collecting, processing, and analyzing Air Quality Index (AQI) data across 10 US states.  
            The goal is to provide actionable insights into air quality trends, pollutant sources, and regional differences, supporting both public awareness and policy-making.
            """)
        with col2:
            st.markdown("### 🛠️ Which technologies are used?")
            st.markdown("""
            <div style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center;">
                <img src="https://img.shields.io/badge/SSIS-CC2927?style=flat&logo=microsoft-sql-server&logoColor=white" />
                <img src="https://img.shields.io/badge/SSAS-CC2927?style=flat&logo=microsoft-sql-server&logoColor=white" />
                <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
                <img src="https://img.shields.io/badge/SQL%20Server-CC2927?style=flat&logo=microsoft-sql-server&logoColor=white" />
                <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=power-bi&logoColor=black" />
            </div>
            <br>
            <a href="https://github.com/trieuvisaooo/US_AQI_Analysis" target="_blank" style="text-decoration: none;">
                <span style="margin-left: 8px; font-size: 1.2rem; vertical-align: middle;">👉</span>
                <img src="https://img.shields.io/badge/GitHub_Repo-181717?style=flat&logo=github&logoColor=white" />
            </a>
            """, unsafe_allow_html=True)

        st.divider()

        # --- Database Description Section ---
        st.markdown("<h3 style='text-align: center;'>🗄️ How is the data organized?</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Data Warehouse:**  
                - Centralized storage for AQI data from EPA sources  
                - Star schema with fact tables for daily AQI readings and dimension tables for states, cities, pollutants, time, and AQI category (e.g., Good, Moderate)  
                - Supports OLAP cubes for fast, multidimensional analysis  
            """)
        with col2:
            st.markdown("""
            - **Data Volume:**  
                - Hundreds of thousands of records over multiple years  
                - Includes pollutant breakdowns (PM2.5, PM10, O₃, NO₂, SO₂, CO)  
            """)

        st.divider()

        # --- ETL Pipeline Section ---
        st.markdown("<h3 style='text-align: center;'>🔄 How does the ETL pipeline work?</h3>", unsafe_allow_html=True)
        st.markdown("""
        The ETL pipeline for AQI data is simple and robust, moving data through four key stages:

        <div style="margin-top: 1.5em; margin-bottom: 1em;">
            <b>Pipeline Architecture:</b>
        </div>
        """, unsafe_allow_html=True)


        # Add icons to each stage label
        etl_nodes = [
            "🌐 Source",
            "🧹 Stage",
            "📦 NDS",
            "📊 DDS"
        ]
        etl_descriptions = [
            "Collect AQI data",
            "Store raw data",
            "Clean, validate & standardize",
            "Analytics & reporting"
        ]
        etl_colors = ["#4F8DFD", "#00B894", "#FDCB6E", "#E17055"]

        fig_etl_flow = go.Figure(data=[go.Sankey(
            arrangement="snap",
            node=dict(
                pad=30,
                thickness=32,
                line=dict(color="#e0e0e0", width=2),
                label=etl_nodes,
                customdata=etl_descriptions,
                hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
                color=etl_colors,
                x=[0.01, 0.33, 0.66, 0.99],
                y=[0.5, 0.5, 0.5, 0.5]
            ),
            link=dict(
                source=[0, 1, 2],
                target=[1, 2, 3],
                value=[1, 1, 1],  # Ignore incoming/outgoing counts, just show flow
                color=["rgba(79,141,253,0.25)", "rgba(0,184,148,0.25)", "rgba(253,203,110,0.25)"],
                label=[
                    "", "", ""
                ],
                hovertemplate="<b>%{source.label} → %{target.label}</b><extra></extra>"
            )
        )])
        fig_etl_flow.update_layout(
            title=dict(
                text="<b>ETL Pipeline Flow: Source → Stage → NDS → DDS</b>",
                font=dict(size=20, color="#2d3436"),
                x=0.5,
                xanchor="center"
            ),
            font=dict(size=15, color="#2d3436"),
            margin=dict(l=10, r=10, t=60, b=10),
            height=340,
            plot_bgcolor="#fafbfc",
            paper_bgcolor="#fafbfc"
        )
        st.plotly_chart(fig_etl_flow, use_container_width=True)

        # Short, icon-enhanced descriptions for each ETL stage
        st.markdown("""
        <div style="display: flex; flex-wrap: wrap; gap: 2em; margin-top: 1.5em; margin-bottom: 0.5em;">
            <div style="flex: 1; min-width: 220px; background: #f5fafd; border-radius: 12px; padding: 1em 1.2em; box-shadow: 0 2px 8px #e3e3e3;">
                <b style="color:#4F8DFD;">🌐 Source</b><br>
                <span style="color:#555;">
                    <ul style="margin:0 0 0 1em; padding:0;">
                        <li>Collect raw AQI data from CSV files</li>
                    </ul>
                </span>
            </div>
            <div style="flex: 1; min-width: 220px; background: #f7fcf9; border-radius: 12px; padding: 1em 1.2em; box-shadow: 0 2px 8px #e3e3e3;">
                <b style="color:#00B894;">🧹 Stage</b><br>
                <span style="color:#555;">
                    <ul style="margin:0 0 0 1em; padding:0;">
                        <li>Store data in SQL Server</li>
                        <li>Minimal transformation: only basic checks and metadata tagging</li>
                    </ul>
                </span>
            </div>
            <div style="flex: 1; min-width: 220px; background: #fff9f3; border-radius: 12px; padding: 1em 1.2em; box-shadow: 0 2px 8px #e3e3e3;">
                <b style="color:#FDCB6E;">📦 NDS</b><br>
                <span style="color:#555;">
                    <ul style="margin:0 0 0 1em; padding:0;">
                        <li>Clean and validate raw data entries</li>
                        <li>Perform detailed transformations and normalize formats</li>
                    </ul>
                </span>
            </div>
            <div style="flex: 1; min-width: 220px; background: #fff6f5; border-radius: 12px; padding: 1em 1.2em; box-shadow: 0 2px 8px #e3e3e3;">
                <b style="color:#E17055;">📊 DDS</b><br>
                <span style="color:#555;">
                    <ul style="margin:0 0 0 1em; padding:0;">
                        <li>Transform data into star-schema model</li>
                        <li>Support analytics and dashboard reporting</li>
                    </ul>
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.divider()
        
        st.markdown("<h3 style='text-align: center;'>🖼️ Visual Insights</h3>", unsafe_allow_html=True)
        # Convert image to base64
        def get_base64_image(path):
            with open(path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()

        # Load image paths and captions (with position info)
        image_info = [
            {
                "path": "./images/projects/usaqi/dashboard1.jpg",
                "caption": "• Max & Min AQI per State per Quarter - Seasonal Variation Analysis •"
            },
            {
                "path": "./images/projects/usaqi/dashboard2.jpg",
                "caption": "• Mean & Std Dev of AQI by State per Quarter - Outlier Detection •"
            },
            {
                "path": "./images/projects/usaqi/dashboard3.jpg",
                "caption": "• Days & Average AQI at 'Very Unhealthy' or 'Worse' - per State & County •"
            },
            {
                "path": "./images/projects/usaqi/dashboard4.jpg",
                "caption": "• Days per AQI Category in HI, AK, IL, DE - Air Quality Breakdown •"
            },
            {
                "path": "./images/projects/usaqi/dashboard5.jpg",
                "caption": "• Quarterly Mean AQI in HI, AK, IL, DE - Regional Comparison •"
            },
            {
                "path": "./images/projects/usaqi/dashboard6.jpg",
                "caption": "• Regional AQI Heatmap - Annual Average by Area •"
            }
        ]


        # Convert images to base64 strings and pair with captions
        images_base64 = [get_base64_image(info["path"]) for info in image_info]
        captions = [info["caption"] for info in image_info]

        # HTML + JS for Swiper carousel with embedded base64 images and captions
        carousel_html = f"""
        <link rel="stylesheet" href="https://unpkg.com/swiper@10/swiper-bundle.min.css" />

        <style>
        .swiper {{
            width: 100%;
            height: 100vh;
            max-height: 600px;
            margin-bottom: 10px;
            border-radius: 10px;
            background: #f8f8f8;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .swiper-slide {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
        }}
        .swiper-slide img {{
            max-width: 100%;
            max-height: 75vh;
            height: auto;
            width: auto;
            display: block;
            margin: 0 auto;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            background: #fff;
        }}
        .swiper-caption {{
            font-size: 1.05rem;
            color: #333;
            text-align: center;
            margin-top: 0.5rem;
            background: rgba(255,255,255,0.92);
            border-radius: 6px;
            padding: 0.3rem 0.8rem;
            max-width: 95%;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}
        </style>

        <div class="swiper mySwiper">
        <div class="swiper-wrapper">
            {''.join([
                f'<div class="swiper-slide"><img src="data:image/png;base64,{b64}" /><div class="swiper-caption">{captions[i]}</div></div>'
                for i, b64 in enumerate(images_base64)
            ])}
        </div>
        <div class="swiper-pagination"></div>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
        </div>

        <script src="https://unpkg.com/swiper@10/swiper-bundle.min.js"></script>
        <script>
        const swiper = new Swiper(".mySwiper", {{
            spaceBetween: 10,
            loop: true,
            centeredSlides: true,
            slidesPerView: 1,
            pagination: {{
                el: ".swiper-pagination",
                clickable: true,
            }},
            navigation: {{
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            }},
        }});
        </script>
        """
        
        # Render carousel
        components.html(carousel_html, height=450, scrolling=False)
        
        st.divider()


    # ========== PROJECT 3 ==========
    with proj3:
        # Project Title and Date
        st.markdown(
            """
            <div style='display: flex; flex-direction: column; align-items: center; margin-bottom: 0.5rem;'>
                <h3 style='text-align: center; margin-bottom: 0.2rem;'>💳 Simulated Credit Card Transaction System 💳</h3>
                <span style='color: #888; font-size: 1rem;'>(Nov 2024 - Dec 2024)</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns([1, 1])

        with col1:
            # 1. Project Description
            st.markdown("### ❓ What is this project?")
            st.markdown(
                """
                This project simulates a real-time credit card transaction system, designed to process, store, and analyze massive volumes of financial data. 
                It demonstrates how modern data engineering tools can be orchestrated to detect trends, automate ETL, and provide actionable insights for fraud detection and business intelligence.
                """
            )

        with col2:
            # 2. Technologies Used (with icons, like project 2)
            st.markdown("### 🚀 Which technologies are used?")
            tech_icons = {
                "Kafka": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apachekafka/apachekafka-original-wordmark.svg",
                "Spark": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apache/apache-original-wordmark.svg",
                "Hadoop": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/hadoop/hadoop-original-wordmark.svg",
                "Airflow": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apacheairflow/apacheairflow-original-wordmark.svg",
                "Power BI": "https://img.icons8.com/color/48/000000/power-bi.png"
            }
            tech_names = list(tech_icons.keys())
            tech_cols = st.columns(len(tech_names))
            for i, tech in enumerate(tech_names):
                with tech_cols[i]:
                    st.markdown(
                        f"<div style='text-align:center'>"
                        f"<img src='{tech_icons[tech]}' width='48' style='margin-bottom:0.2rem;'/><br>"
                        f"<span style='font-size:1rem'>{tech}</span>"
                        f"</div>",
                        unsafe_allow_html=True
                    )
            st.markdown(
                """
                <div style="text-align: center;">
                    <a href="https://github.com/trieuvisaooo/Simulated_Credit_Card_Transaction_System" target="_blank" style="text-decoration: none;">
                        <span style="margin-left: 8px; font-size: 1.2rem; vertical-align: middle;">👉</span>
                        <img src="https://img.shields.io/badge/GitHub_Repo-181717?style=flat&logo=github&logoColor=white"/>
                        <span style="margin-right: 8px; font-size: 1.2rem; vertical-align: middle;">👈</span>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        # 3. Pipeline Architecture
        st.markdown("<h3 style='text-align: center;'>🛤️ How Does the Data Flow Through the Pipeline?</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            The architecture below shows how simulated credit card transactions flow through the data pipeline, from real-time ingestion to analytics and visualization.
            """
        )

        # Add a short legend for clarity
        st.markdown(
            """
            <div style="display: flex; flex-wrap: wrap; gap: 2em; justify-content: center; margin-top: 1em;">
                <div style="text-align:center;"><span style="font-size:1.3em;">💳</span><br><span style="color:#FF9800;">Kafka</span><br><span style="font-size:0.9em;color:#888;">Ingestion</span></div>
                <div style="text-align:center;"><span style="font-size:1.3em;">⚡</span><br><span style="color:#00B894;">Spark</span><br><span style="font-size:0.9em;color:#888;">Processing</span></div>
                <div style="text-align:center;"><span style="font-size:1.3em;">🐘</span><br><span style="color:#607D8B;">Hadoop</span><br><span style="font-size:0.9em;color:#888;">Storage</span></div>
                <div style="text-align:center;"><span style="font-size:1.3em;">🛫</span><br><span style="color:#1976D2;">Airflow</span><br><span style="font-size:0.9em;color:#888;">Orchestration</span></div>
                <div style="text-align:center;"><span style="font-size:1.3em;">📊</span><br><span style="color:#F2C811;">Power BI</span><br><span style="font-size:0.9em;color:#888;">Visualization</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Define nodes with improved layout and color
        nodes = {
            "Kafka":   {"pos": (0.08, 0.5), "icon": "💳", "desc": "Ingestion", "color": "#FF9800"},
            "Spark":   {"pos": (0.26, 0.5), "icon": "⚡", "desc": "Stream Processing", "color": "#00B894"},
            "Hadoop":  {"pos": (0.44, 0.5), "icon": "🐘", "desc": "Storage", "color": "#607D8B"},
            "Airflow": {"pos": (0.44, 0.8), "icon": "🛫", "desc": "ETL Orchestration", "color": "#1976D2"},
            "PowerBI": {"pos": (0.7, 0.5), "icon": "📊", "desc": "Visualization", "color": "#F2C811"},
        }

        # Draw nodes as styled markers with annotation for better clarity
        node_traces = []
        for name, info in nodes.items():
            x, y = info["pos"]
            node_traces.append(go.Scatter(
                x=[x], y=[y],
                mode="markers+text",
                marker=dict(
                    size=70,
                    color=info["color"],
                    opacity=0.18,
                    line=dict(width=2, color=info["color"]),
                    symbol="circle"
                ),
                text=f"{info['icon']}<br><b style='color:{info['color']}'>{name}</b><br><span style='font-size:13px;color:#555;'>{info['desc']}</span>",
                hoverinfo="text",
                textposition="middle center",
                textfont=dict(size=18, color="#222"),
                showlegend=False
            ))

        # Draw arrows with improved style and arrowheads
        arrow_shapes = []

        def add_arrow(x0, y0, x1, y1, color, width=3, head_size=0.018):
            arrow_shapes.append(dict(
                type="line",
                x0=x0, y0=y0, x1=x1, y1=y1,
                line=dict(color=color, width=width, dash="solid"),
                opacity=0.9,
                layer="below"
            ))
            # Arrowhead
            dx = x1 - x0
            dy = y1 - y0
            length = (dx**2 + dy**2) ** 0.5
            if length == 0:
                return
            ux, uy = dx / length, dy / length
            # Perpendicular
            px, py = -uy, ux
            # Arrowhead points
            tip = (x1, y1)
            left = (x1 - head_size * ux + head_size * 0.6 * px, y1 - head_size * uy + head_size * 0.6 * py)
            right = (x1 - head_size * ux - head_size * 0.6 * px, y1 - head_size * uy - head_size * 0.6 * py)
            arrow_shapes.append(dict(
                type="path",
                path=f'M {tip[0]},{tip[1]} L {left[0]},{left[1]} L {right[0]},{right[1]} Z',
                fillcolor=color,
                line=dict(width=0),
                layer="above"
            ))

        # Main pipeline arrows
        add_arrow(nodes["Kafka"]["pos"][0]+0.035, nodes["Kafka"]["pos"][1], nodes["Spark"]["pos"][0]-0.035, nodes["Spark"]["pos"][1], "#FF9800")
        add_arrow(nodes["Spark"]["pos"][0]+0.035, nodes["Spark"]["pos"][1], nodes["Hadoop"]["pos"][0]-0.035, nodes["Hadoop"]["pos"][1], "#00B894")
        add_arrow(nodes["Hadoop"]["pos"][0]+0.035, nodes["Hadoop"]["pos"][1], nodes["PowerBI"]["pos"][0]-0.035, nodes["PowerBI"]["pos"][1], "#F2C811")
        # Airflow to Hadoop (down)
        add_arrow(nodes["Airflow"]["pos"][0], nodes["Airflow"]["pos"][1]-0.035, nodes["Hadoop"]["pos"][0], nodes["Hadoop"]["pos"][1]+0.035, "#1976D2", width=2)
        # Airflow to PowerBI (diagonal)
        add_arrow(nodes["Airflow"]["pos"][0]+0.03, nodes["Airflow"]["pos"][1]-0.03, nodes["PowerBI"]["pos"][0]-0.035, nodes["PowerBI"]["pos"][1]+0.035, "#1976D2", width=2)

        # No annotations needed (no text and icon)
        annotations = []

        # Create figure
        fig = go.Figure()

        # Add node traces
        for trace in node_traces:
            fig.add_trace(trace)

        # Add arrows and layout
        fig.update_layout(
            shapes=arrow_shapes,
            annotations=annotations,
            xaxis=dict(visible=False, range=[0, 0.8]),
            yaxis=dict(visible=False, range=[0, 1]),
            height=440,
            margin=dict(l=10, r=10, t=60, b=10),
            plot_bgcolor="#f7fafd",
            paper_bgcolor="#f7fafd",
            title=dict(
                text="<b>Credit Card Transaction Data Pipeline</b>",
                x=0.5, xanchor="center",
                font=dict(size=22, color="#2d3436")
            )
        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        # 4. Transformation, Storage, and Automation
        st.markdown("<h3 style='text-align: center;'>🔄 How Are Transactions Ingested, Processed, Stored, and Visualized?</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            - **Ingestion:** Kafka reads transaction data line-by-line from CSV files and sends it to a predefined topic at random intervals between 1-3 seconds.
            - **Real-time Processing:** Spark Streaming immediately processes data as it arrives from Kafka, performing filtering, transformation and calculations.
            - **Storage:** Processed data is saved into Hadoop (HDFS), serving as a central repository for further statistical analysis and visualization.
            - **Visualization:** Power BI connects to Hadoop (via CSV files) to generate insightful, descriptive analytics and interactive dashboards.
            - **Automation:** Airflow schedules daily refreshes of Power BI datasets, ensuring that reports are always up-to-date with the latest data.
            """
        )


        st.divider()

        # 5. Sample Data
        st.markdown("<h3 style='text-align: center;'>🧐 What Does a Raw Transaction Look Like?</h3>", unsafe_allow_html=True)

        # Realistic sample data based on provided example
        sample_data = pd.DataFrame({
            "User": [0]*10,
            "Card": [0]*10,
            "Year": [2002]*10,
            "Month": [9]*10,
            "Day": [1,1,2,2,3,3,4,4,5,5],
            "Time": ["06:21", "06:42", "06:22", "17:45", "06:23", "13:53", "05:51", "06:09", "06:14", "09:35"],
            "Amount": ["$134.09", "$38.48", "$120.34", "$128.95", "$104.71", "$86.19", "$93.84", "$123.50", "$61.72", "$57.10"],
            "Merchant": [
                "3527213246127876953",  # Walmart
                "727612092139916043",   # Ralphs
                "3414527459579106770",  # Macy's
                "5817218446178736267",  # CVS Pharmacy
                "7146670748125200898",  # Shell Gas
                "4055257078481058705",  # Pep Boys
                "1234567890123456789",  # Starbucks
                "9876543210987654321",  # Amazon
                "1928374655647382910",  # Target
                "5647382910123456789"   # Home Depot
            ],
            "Merchant City": [
                "La Verne",
                "Monterey Park",
                "Los Angeles",
                "San Diego",
                "La Verne",
                "Pasadena",
                "Santa Monica",
                "Irvine",
                "Anaheim",
                "Burbank"
            ],
            "Merchant State": [
                "CA", "CA", "CA", "CA", "CA", "CA", "CA", "CA", "CA", "CA"
            ],
            "Zip": [
                91750.0, 91754.0, 90001.0, 92101.0, 91750.0, 91101.0, 90401.0, 92612.0, 92801.0, 91501.0
            ],
            "MCC": [
                5300,   # Discount Stores
                5411,   # Grocery Stores
                5651,   # Clothing Stores
                5912,   # Drug Stores
                5541,   # Service Stations
                7538,   # Auto Repair
                5814,   # Fast Food Restaurants
                5942,   # Book Stores
                5311,   # Department Stores
                5200    # Home Supply
            ],
            "Errors?": [None]*10,
            "Is Fraud?": ["No"]*10
        })
        st.dataframe(sample_data, use_container_width=True, hide_index=True)

        

        st.divider()

        # 6. Visual Insights
        st.markdown("<h3 style='text-align: center;'>📈 What Surprising Insights Can We Discover?</h3>", unsafe_allow_html=True)
        st.markdown("Let's explore daily transaction volumes and merchant trends from the simulated data:")

        # Simulate a larger transaction dataset for demonstration
        np.random.seed(42)
        merchants = [
            "Walmart", "Ralphs", "Macy's", "CVS Pharmacy", "Shell Gas",
            "Pep Boys", "Starbucks", "Amazon", "Target", "Home Depot"
        ]
        dates = pd.date_range("2024-06-01", periods=90, freq="D")
        n_samples = 500
        simulated_data = pd.DataFrame({
            "Date": np.random.choice(dates, n_samples),
            "Merchant": np.random.choice(merchants, n_samples),
            "Amount": np.round(np.random.uniform(5, 500, n_samples), 2)
        })
        simulated_data["Day"] = simulated_data["Date"].dt.day
        simulated_data["Month"] = simulated_data["Date"].dt.month
        simulated_data["Year"] = simulated_data["Date"].dt.year

        # 1. Total amount and transaction count per Merchant
        merchant_summary = simulated_data.groupby("Merchant").agg(
            Total_Amount=("Amount", "sum"),
            Transaction_Count=("Amount", "count")
        ).reset_index().sort_values("Total_Amount", ascending=False)
        st.markdown("#### 🏪 Merchant Summary (Total Amount & Transaction Count)")
        st.dataframe(merchant_summary, use_container_width=True, hide_index=True)

        # 2. Daily statistics: total amount and transaction count per day
        daily_stats = simulated_data.groupby("Date").agg(
            Total_Amount=("Amount", "sum"),
            Transaction_Count=("Amount", "count")
        ).reset_index()
        fig_daily = px.bar(
            daily_stats, x="Date", y="Total_Amount",
            title="Total Transaction Amount by Day",
            labels={"Total_Amount": "Total Amount (VND)", "Date": "Date"},
            color="Total_Amount", color_continuous_scale="Blues"
        )
        st.plotly_chart(fig_daily, use_container_width=True)

        # 3. Monthly statistics: total amount and transaction count per month
        monthly_stats = simulated_data.groupby(["Year", "Month"]).agg(
            Total_Amount=("Amount", "sum"),
            Transaction_Count=("Amount", "count")
        ).reset_index()
        monthly_stats["Month_Year"] = monthly_stats["Year"].astype(str) + "-" + monthly_stats["Month"].astype(str).str.zfill(2)
        fig_monthly = px.bar(
            monthly_stats, x="Month_Year", y="Total_Amount",
            title="Total Transaction Amount by Month",
            labels={"Total_Amount": "Total Amount (VND)", "Month_Year": "Month-Year"},
            color="Total_Amount", color_continuous_scale="Greens"
        )
        st.plotly_chart(fig_monthly, use_container_width=True)

        # 4. Yearly statistics: total amount and transaction count per year
        yearly_stats = simulated_data.groupby("Year").agg(
            Total_Amount=("Amount", "sum"),
            Transaction_Count=("Amount", "count")
        ).reset_index()
        fig_yearly = px.bar(
            yearly_stats, x="Year", y="Total_Amount",
            title="Total Transaction Amount by Year",
            labels={"Total_Amount": "Total Amount (VND)", "Year": "Year"},
            color="Total_Amount", color_continuous_scale="Oranges"
        )
        st.plotly_chart(fig_yearly, use_container_width=True)

        # 5. Pie chart: Transaction count by Merchant
        merchant_counts = simulated_data["Merchant"].value_counts().reset_index()
        merchant_counts.columns = ["Merchant", "Count"]
        fig_merchant_pie = px.pie(
            merchant_counts, names="Merchant", values="Count",
            title="Transaction Count Distribution by Merchant"
        )
        st.plotly_chart(fig_merchant_pie, use_container_width=True)

        st.divider()


    with proj4:
        # 🌩️ Live Weather Event Alert System
        st.markdown(
            """
            <div style='display: flex; flex-direction: column; align-items: center; margin-bottom: 0.5rem;'>
                <h3 style='text-align: center; margin-bottom: 0.2rem;'>⛈️ Live Weather Event Alert System ⛈️</h3>
                <span style='color: #888; font-size: 1rem;'>(May 2025 - Present)</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)
        with col1:
            # --- Features and Description ---
            st.markdown("### ❓ What is this project?")
            st.markdown(
                """
                A real-time system that ingests weather data from the OpenWeatherMap API, detects extreme weather events using Spark Structured Streaming, pushes notifications via email, and visualizes alerts in a live Streamlit dashboard.
                """
            )
            
        with col2:
            st.markdown("### 🛠️ Which technologies are used?")
            st.markdown("""
            <div style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center;">
                <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
                <img src="https://img.shields.io/badge/Apache%20Kafka-231F20?style=flat&logo=apache-kafka&logoColor=white" />
                <img src="https://img.shields.io/badge/Apache%20Spark-E25A1C?style=flat&logo=apachespark&logoColor=white" />
                <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white" />
                <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white" />
                <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" />
            </div>
            <br>
            <a href="https://github.com/trieuvisaooo/live-weather-event-alert" target="_blank" style="text-decoration: none;">
                <span style="margin-left: 8px; font-size: 1.2rem; vertical-align: middle;">👉</span>
                <img src="https://img.shields.io/badge/GitHub_Repo-181717?style=flat&logo=github&logoColor=white" />
                <span style="margin-right: 8px; font-size: 1.2rem; vertical-align: middle;">👈</span>
            </a>
            """, unsafe_allow_html=True)            

        st.divider()
        st.markdown("<h3 style='text-align: center;'>🚀 Which features does it have?</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            - 🔄 Real-time ingestion of weather data from multiple cities  
            - 🧠 Stream processing and event detection with Apache Spark  
            - 🔔 Email notifications for extreme weather (e.g., heatwave, storm)  
            - 📊 Interactive dashboard built with Streamlit  
            - 🐳 Fully containerized with Docker and docker-compose
            """
        )

        st.divider()

        # --- Tech Stack Table ---
        st.markdown("### 📦 Tech Stack")
        st.markdown(
            """
            <table style="width:100%; font-size:1.05rem;">
                <thead>
                    <tr>
                        <th style="text-align:left;">Layer</th>
                        <th style="text-align:left;">Tools</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>Ingestion</td><td>Python + OpenWeatherMap API</td></tr>
                    <tr><td>Messaging</td><td>Apache Kafka</td></tr>
                    <tr><td>Processing</td><td>Apache Spark (Structured Streaming)</td></tr>
                    <tr><td>Notification</td><td>SMTP (Gmail) or AWS SES</td></tr>
                    <tr><td>Dashboard</td><td>Streamlit</td></tr>
                    <tr><td>Storage</td><td>PostgreSQL</td></tr>
                    <tr><td>Deployment</td><td>Docker, Docker Compose</td></tr>
                </tbody>
            </table>
            """, unsafe_allow_html=True
        )

        st.divider()

        # --- Architecture Diagram and Text ---
        st.markdown("<h3 style='text-align: center;'>🧩 Architecture</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <img src="https://raw.githubusercontent.com/trieuvisaooo/live-weather-event-alert/main/docs/architecture.png" alt="System Architecture" style="max-width: 90%; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);"/>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown(
            """
        <pre style="background:#f8f8f8; border-radius:8px; padding:1rem; font-size:1rem;">
        [Weather API] --> [Ingestion Script] --> Kafka (weather_raw)
                                                |
                                        Spark Streaming Job
                                                ↓
                                    Stores in PostgreSQL database
                                                ↓
                                Detects Alert Events (storm, heat, etc.)
                                                ↓
                            Kafka (weather_alerts) --> Streamlit Dashboard
                                                ↓
                                    Sends Email via SES / SMTP
        </pre>
            """, unsafe_allow_html=True
        )

        st.divider()

        # --- Demo & Screenshots ---
        st.markdown("<h3 style='text-align: center;'>📸 Demo & Screenshots</h3>", unsafe_allow_html=True)
        images_urls = [
            "https://raw.githubusercontent.com/trieuvisaooo/live-weather-event-alert/main/docs/demo_dashboard.png",
            "https://raw.githubusercontent.com/trieuvisaooo/live-weather-event-alert/main/docs/demo_telegram.png",
            "https://raw.githubusercontent.com/trieuvisaooo/live-weather-event-alert/main/docs/demo_map.png"
        ]
        captions = [
            "Live Dashboard: Real-time event feed and analytics",
            "Email Notification: Instant severe weather alerts",
            "Interactive Map: Visualize affected areas"
        ]
        img_cols = st.columns(len(images_urls))
        for i, url in enumerate(images_urls):
            with img_cols[i]:
                st.image(url, caption=captions[i], use_container_width=True)

        st.divider()


# --- Contact Page ---
with Contact:
    # st.header("🤝 Let's Connect!", anchor=False)
    st.markdown("<h1 style='text-align: center;'>🤝 Let's Connect! 🤝</h1>", unsafe_allow_html=True)
    
    # Create two columns for contact info
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📱 Social Links")
        st.markdown("""
        Connect with me on social media:
        
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/khactrieu74/)
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/trieuvisaooo/)
        [![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/nktrieu/)
        """)
        
        st.markdown("### 📧 Direct Contact")
        st.markdown("""
        Send me an email at: [![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:khactrieu.work.2025@gmail.com)
        """)
        
    with col2:
        st.markdown("### 💌 Send Me a Message")
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name", placeholder="Trieu")
            email = st.text_input("Your Email", placeholder="khactrieu.work.2025@gmail.com")
            subject = st.text_input("Subject", placeholder="Let's collaborate!")
            message = st.text_area("Message", placeholder="Hi there, I'd love to discuss...")
            
            submitted = st.form_submit_button("📤 Send Message", use_container_width=True)
            
            if submitted:
                if not name or not email or not message:
                    st.error("🚫 Please fill in all required fields!")
                else:
                    try:
                        # Email configuration
                        sender_email = "trieulaobao@gmail.com"
                        receiver_email = "khactrieu.work.2025@gmail.com"
                        password = st.secrets["email_password"]
                        
                        # Create message with improved formatting
                        msg = MIMEText(f"""
                        💌 New Message from Portfolio Website
                        
                        👤 From: {name}
                        📧 Email: {email}
                        📝 Subject: {subject}
                        
                        Message:
                        {message}
                        """)
                        
                        msg['Subject'] = f'Portfolio Contact: {subject} - from {name}'
                        msg['From'] = sender_email
                        msg['To'] = receiver_email
                        
                        # Send email
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                            smtp_server.login(sender_email, password)
                            smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
                        
                        st.success("✨ Message sent successfully! I'll get back to you soon.")
                        st.balloons()
                    except Exception as e:
                        st.error("❌ Oops! Something went wrong. Please try again later or contact me directly via email.")

st.markdown("""
    <div style='text-align: right;'>
        <a href="#home" style='
            background-color: #2c3e50;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        '>⬆️ Back to Top</a>
    </div>
""", unsafe_allow_html=True)
