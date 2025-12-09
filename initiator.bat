@echo off
echo Step1: Setting up virtual environment
call C:\Users\abhis\PycharmProjects\Django_learning\.venv\Scripts\activate.bat

echo Step2: Moving to original Directory
cd firstproject

echo Step3: Running the Server
python manage.py runserver