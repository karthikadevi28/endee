🚀 Resume Skill Matcher AI


📌 Project Overview


This project is an AI-based application that suggests suitable job roles based on user-provided skills. It uses text vectorization and similarity matching techniques to identify the most relevant job role.

🎯 Objective


The objective of this project is to:


1.🎓 Help users identify suitable career paths


2.🤖 Demonstrate basic AI concepts like vectorization


3.🔍 Perform similarity matching between skills and job roles



🏗️ System Design



⚙️ Components


1.🧾 User Input Module


  ->Accepts skills from the user




2.🔄 Data Processing Module


->Converts text into vectors using CountVectorizer




3.🧠 Similarity Engine


->Uses cosine similarity to compare user skills with job roles




4.📤 Output Module


->Displays the best matching job role





🤖 Use of Model


This project uses a simple machine learning approach:


1.📊 CountVectorizer for text vectorization


2.📐 Cosine Similarity for matching

📌 Vector Database Justification



Vector representation helps in:


1.🔢 Converting text into numerical format


2.📏 Measuring similarity between user input and job descriptions


3.⚡ Efficient matching of skills



✨ Features


1.👍 Simple and easy to use


2.🧾 Accepts user skill input


3.🎯 Suggests best matching job role


4.🤖 Uses AI-based similarity matching



📊 Dataset


This project uses a sample dataset inspired by the Endee repository.
The dataset contains job roles and their associated skills.


📝 Example:


Data Scientist → python, machine learning


Web Developer → html, css, javascript



▶️ How to Run


🐍 Install Python


📦 Install required library:
pip install -r requirements.txt


▶️ Run the program:
python main.py



💡 Example


Input:


python machine learning


Output:


Suggested Role: Data Scientist

