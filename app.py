import os
import docx
import PyPDF2
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#File Reading Functions
def read_docx(file):
    doc = docx.Document(file)
    return " ".join([para.text for para in doc.paragraphs])

def read_pdf(file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def read_file(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith(".docx"):
        return read_docx(uploaded_file)
    elif uploaded_file.name.endswith(".pdf"):
        return read_pdf(uploaded_file)
    else:
        return ""


# Streamlit UI
st.title("📄 Resume Matcher App")
st.write("Upload a Job Description and multiple Resumes to find the best matches.")


# Upload JD
jd_file = st.file_uploader("Upload Job Description (TXT/DOCX/PDF)", type=["txt", "docx", "pdf"])

# Upload multiple resumes
resume_files = st.file_uploader(
    "Upload Candidate Resumes (TXT/DOCX/PDF)",
    type=["txt", "docx", "pdf"],
    accept_multiple_files=True
)

if jd_file is not None and resume_files:
    # Read JD
    job_description = read_file(jd_file)

    st.subheader("📌 Job Description:")
    st.write(job_description)

    # Read resumes
    resumes = {}
    for file in resume_files:
        text = read_file(file)
        if text.strip():
            resumes[file.name] = text

    if resumes:
        # TF-IDF similarity
        documents = [job_description] + list(resumes.values())
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(documents)
        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

        # Rank resumes
        ranked_resumes = sorted(
            zip(resumes.keys(), similarities),
            key=lambda x: x[1],
            reverse=True
        )

        # Show results
        st.subheader("📊 Matching Resumes:")
        for file_name, score in ranked_resumes:
            st.write(f"✅ {file_name} — Similarity Score: {score:.4f}")
    else:
        st.warning("⚠️ No valid resumes uploaded yet.")