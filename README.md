# Coldplay Band Overview App

This app provides an overview of the band Coldplay, including their discography, a brief "About Us" section, and a "Contact Us" page. The goal of this app is to give fans a quick and user-friendly way to explore the band's history, music, and background.

Follow the instructions below to set up and run the app using either a virtual environment (venv) or Docker.

## Setup and Run with venv

1. Clone the repository:
git clone <repository-url>
cd <repository-name>


2. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate # For Linux and macOS
.\venv\Scripts\activate # For Windows


3. Install the required packages:
pip install -r requirements.txt


4. Set environment variables, such as API keys and secrets (replace the placeholders with the actual values):
export SECRET_KEY=<django-insecure-cedsj)%tp^xs8#s_hxxo#u@kfwv3n9phm=z8s@q=7*k6n0_0ll>


5. Run the Django development server:
python manage.py runserver


6. Open a web browser and visit `http://localhost:8000/` to access the application.

## Setup and Run with Docker

1. Clone the repository:
git clone <repository-url>
cd <repository-name>


2. Build the Docker image:
docker build -t <image-name> .


3. Run the Docker container (replace the placeholders with the actual values):
docker run -it -p 8000:8000 -e SECRET_KEY=<django-insecure-cedsj)%tp^xs8#s_hxxo#u@kfwv3n9phm=z8s@q=7*k6n0_0ll> <image-name>


4. Open a web browser and visit `http://localhost:8000/` to access the application.


 ## END