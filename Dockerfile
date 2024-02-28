FROM python:3.10

#DIRECTORY
WORKDIR /passenger

#REQUIRMENTS
RUN pip install discord python-dotenv

#COPY THE FILES
COPY . .

#RUN THE BOT
CMD ["python3", "src/main.py"]