import os
import fitz
import docx
import pandas as pd
import nltk
import tkinter as tk
from tkinter import filedialog, messagebox
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("stopwords")
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text.lower()

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text.lower()

def process_resumes(folder_path, keywords):
    resumes = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if file.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            continue
        resumes.append((file, text))

    if not resumes:
        messagebox.showwarning("No Resumes Found", "No valid resumes found in the folder.")
        return None

    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform([resume[1] for resume in resumes])
    keyword_vector = tfidf_vectorizer.transform([keywords.lower()])
    similarity_scores = (tfidf_matrix * keyword_vector.T).toarray().flatten()
    sorted_resumes = sorted(zip(resumes, similarity_scores), key=lambda x: x[1], reverse=True)
    df = pd.DataFrame([(r[0][0], round(r[1] * 100, 2)) for r in sorted_resumes], columns=["Candidate", "Match Score (%)"])
    
    return df

def select_folder():
    folder_path = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(0, folder_path)

def scan_resumes():
    folder_path = entry_folder.get()
    keywords = entry_keywords.get()
    if not folder_path or not keywords:
        messagebox.showwarning("Missing Input", "Please select a folder and enter keywords.")
        return

    results = process_resumes(folder_path, keywords)
    if results is not None:
        results.to_csv("shortlisted_resumes.csv", index=False)
        messagebox.showinfo("Success", "Resumes processed! Check shortlisted_resumes.csv")

root = tk.Tk()
root.title("AI Resume Screener")

tk.Label(root, text="Resume Folder:").grid(row=0, column=0, padx=10, pady=5)
entry_folder = tk.Entry(root, width=50)
entry_folder.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_folder).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Keywords:").grid(row=1, column=0, padx=10, pady=5)
entry_keywords = tk.Entry(root, width=50)
entry_keywords.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Scan Resumes", command=scan_resumes).grid(row=2, column=1, pady=10)

root.mainloop()