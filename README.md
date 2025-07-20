
# 📄 About This Project
OCR Mind is an intelligent document scanner and entity extractor designed to scan business cards and automatically identify key information such as Name, Designation, Phone Number, Email, Organization, Website, and Location.

This project combines the power of Computer Vision and Natural Language Processing (NLP) to automate the extraction of structured data from unstructured scanned images. It was built by me as a student project to challenge and upgrade my machine learning and full-stack development skills.

Since this is a prototype trained on a relatively small dataset of just over 300 manually labeled business card samples, the system may not always provide highly accurate, algorithmically calculated coordinates when wrapping or cropping certain images. However, it consistently delivers impressive results when it comes to extracting and analyzing key data, especially in clean or moderately structured card layouts.

This is why the interface also allows you to manually select the coordinates for wrapping the image — ensuring precision even when automated cropping has limitations.

The NER (Named Entity Recognition) model used in this project was trained from scratch using completely raw business card data. The data was cleaned, processed, and labeled through multiple stages of preprocessing and formatting. We used BIO tagging (Begin, Inside, Outside) to annotate each entity in the dataset accurately. This structured format allowed the model to learn and generalize entity recognition from highly diverse business card layouts.


---
# ⚙️ How It Works
 ### 1. Image Upload and Region Selection:
Once a user uploads a business card image, the web interface provides four movable corner points, just like in professional document scanner apps. These draggable circles allow users to manually select the wrap or focus area of the card to remove unwanted borders, shadows, or distortions. This ensures the OCR engine works only on the relevant region of the document, greatly improving accuracy.


### 2. Image Preprocessing (Computer Vision):
The selected region is passed through various image processing techniques using OpenCV:

- Perspective transformation to flatten the image
- Grayscale conversion, thresholding, and noise removal
- Text enhancement to improve OCR clarity

### 3. Text Extraction with OCR:
The cleaned and preprocessed image is sent to Pytesseract, a Python wrapper for Google's Tesseract OCR engine. It converts the image into raw text that will then be passed to the NLP pipeline.


### 4. NER-Based Entity Extraction (NLP):
The extracted text is processed using a custom-trained Named Entity Recognition (NER) model built with SpaCy. We used BIO tagging (Begin-Inside-Outside) to manually label around 300 business card samples for training. This model is trained to identify specific categories like:
B-NAME, B-EMAIL, B-PHONE, B-DESIGNATION, B-WEBSITE, etc.


### 5. Display and Output:
Once the text is parsed, the extracted entities are shown in a structured table format. The interface also optionally highlights the recognized fields using Displacy, SpaCy’s visualization tool.


---
# 📌Why This Matters
Business cards may appear simple, but in reality, they are highly unstructured and vary significantly in design, layout, and content. Manually extracting relevant information like names, emails, phone numbers, and company details is both time-consuming and error-prone. Automating this process not only enhances accuracy but also boosts productivity, especially in large-scale scenarios.
This kind of automation can be a game-changer for several industries. It enables seamless integration with Customer Relationship Management (CRM) tools, improves lead management workflows, helps build searchable digital business card directories, and serves as a foundation for intelligent contact management systems. By leveraging OCR and Named Entity Recognition (NER), we take a step toward digitizing and organizing real-world information efficiently.


---
# 🔗 Built With
* Python, Flask – Backend processing & routing
* OpenCV, Pytesseract – Image handling and OCR
* SpaCy – Custom NER model
* HTML, CSS, Bootstrap, JavaScript – Web interface & interactivity
* Draggable Canvas JS logic – For selecting card region manually

---
# 🧬 Future Improvements
While this is currently a prototype trained on 300 manually labeled business cards, the system is built with scalability in mind. Here’s how it can be improved further:

1. Train the NER model on a larger, more diverse dataset for higher accuracy across different layouts, fonts, and languages
2. Support for other document types like invoices, ID cards, shipping bills, and forms
3. Integrate deep learning OCR engines like EasyOCR or PaddleOCR for better text recognition
4. Add auto-cropping with edge detection so users don’t need to manually adjust the corners every time
5. Deploy as a cloud-based API or full-stack SaaS tool for real-world business integration

---
# 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or improve.

---
# 🐛 Issues

If you find any bugs or issues, feel free to open a [GitHub Issue]([https://github.com/Aakarsh-Narang/OCRMind/issues](https://github.com/Aakarsh-Narang/OCRMind)).


---
# 🚀 Installation Guide

Follow these steps to run OCRMind on your local machine.

#

##  Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- Git
- pip (Python package installer)
- Tesseract OCR installed and added to your PATH  
  👉 [Download Tesseract OCR](https://github.com/tesseract-ocr/tesseract)


#
## 📦 Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Aakarsh-Narang/OCRMind.git
cd OCRMind
```
### 2. Create two Virtual Environments 
1 virtual enviroonment is for Python backend and 1 for flask WebApp

```bash
python -m venv venv
venv\Scripts\activate
```
###  3. Install Required Dependencies
For python backend and OCR Model install
```bash
pip install -r requirements.txt
pip install -r requirements_.txt
```
For Flask Web App install
```bash
pip install -r requirementsApp.txt
```

### 4. Run the Flask App
```bash
python main.py
```
The app will start on:
http://127.0.0.1:5000

Open it in your browser.

### 5. Upload a Business Card
* Upload an image file of a business card
* Adjust the corners to select the card region
* Click to scan and extract entities
