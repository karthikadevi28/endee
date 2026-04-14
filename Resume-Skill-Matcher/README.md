🚀 **Resume Skill Matcher AI**

 📌 **Project Overview**
This project is an AI-based application that suggests suitable job roles based on user-provided skills. It uses text vectorization and similarity matching techniques to identify the most relevant job role.



🎯 **Objective**
The objective of this project is to:
- 🎓 Help users identify suitable career paths  
- 🤖 Demonstrate basic AI concepts like vectorization  
- 🔍 Perform similarity matching between skills and job roles  



🏗️** System Design**

⚙️ Components
1. 🧾 User Input Module  
   - Accepts skills from the user  

2. 🔄 Data Processing Module  
   - Converts text into vectors using CountVectorizer  

3. 🧠 Similarity Engine  
   - Uses cosine similarity to compare user skills with job roles  

4. 📤 Output Module  
   - Displays the best matching job role  



 🤖 **Use of Model**
This project uses a simple machine learning approach:
- 📊 CountVectorizer for text vectorization  
- 📐 Cosine Similarity for matching  


📌** Vector Database Justification**
     Vector representation helps in:
       - 🔢 Converting text into numerical format  
       - 📏 Measuring similarity between user input and job descriptions  
       - ⚡ Efficient matching of skills  



✨ **Features**
- 👍 Simple and easy to use  
- 🧾 Accepts user skill input  
- 🎯 Suggests best matching job role  
- 🤖 Uses AI-based similarity matching  



📊 **Dataset**
This project uses a sample dataset inspired by the Endee repository.  
The dataset contains job roles and their associated skills.

 📝 Example:
- Data Scientist → python, machine learning  
- Web Developer → html, css, javascript  



▶️ **How to Run**
1. 🐍 Install Python  
2. 📦 Install required library:  
   pip install -r requirements.txt  
3. ▶️ Run the program:  
   python main.py  



💡 Example

**Input:**  
python machine learning  

**Output:**  
Suggested Role: Data Scientist
