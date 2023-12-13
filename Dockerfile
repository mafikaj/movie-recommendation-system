FROM python:3.9

# Set the working directory
WORKDIR /app

# Install spaCy version 3.0.6 and download model
RUN pip install spacy==3.0.6
RUN python -m spacy download en_core_web_md

# Copy your source code into the container
COPY . /app

# Command to run your script
CMD ["python", "watch_next.py"]
