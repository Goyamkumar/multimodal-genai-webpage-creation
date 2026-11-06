# Multimodal Generative AI for Webpage Creation with Text and Image

B.E. final year project (Artificial Intelligence & Data Science),
Thadomal Shahani Engineering College, University of Mumbai, 2023-24.

## Overview
A Streamlit web app that uses the Google Gemini API to generate text
responses from typed prompts and from uploaded images. It is a first step
towards AI-assisted webpage content creation, where text and image
understanding are combined in one tool.

## Features
- **Homepage** with navigation to the two models
- **Text model:** enter a prompt and get a generated response
- **Image-to-text model:** upload a JPG/PNG image, add an optional prompt,
  and get a description or answer about the image
- Multipage Streamlit interface with image preview and on-screen responses

## Tech Stack
Python, Streamlit, Google Gemini API (<add model names, e.g. text and vision>)

## Project Structure
- `Homepage.py`: landing page and navigation
- `pages/1_Text to Text Model.py`: text generation page
- `pages/2_Image to Text Model.py`: image understanding page
- `requirements.txt`: dependencies

## Evaluation
We surveyed 11 users:
- 73% rated ease of understanding 4 or 5 out of 5
- 73% rated effectiveness for webpage creation 4 or 5 out of 5
- 7 of 11 (64%) found it helpful in the context of web development

Small sample, so treat these as early feedback.

## Screenshots
## Homepage
<img width="1280" height="596" alt="image" src="https://github.com/user-attachments/assets/0aa34e7c-e3ea-4f2d-8704-fb11020d0c9c" />



## Text to Text output
<img width="1280" height="599" alt="image" src="https://github.com/user-attachments/assets/c881e89e-1490-4e95-a3a8-b24f7e885810" />


## Image to Text output
<img width="1280" height="565" alt="image" src="https://github.com/user-attachments/assets/1b6f2fd1-0222-417c-b6c8-9a0fde37a7f9" />



## How to Run
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Get a Gemini API key from Google AI Studio
4. Create a `.env` file in the project folder: `GOOGLE_API_KEY=your_key_here`
5. Run: `streamlit run Homepage.py`
6. Open http://localhost:8501

## Limitations and Future Work
- Currently generates text from text and images; it does not generate
  complete webpages
- Future work: voice input, layout generation, CMS integration,
  collaborative editing

## Team
- Ved Gadge
- Goyam Jain
- Vedant Kadam
- Saris Singh

Supervisor: Dr. G. T. Thampi
