FROM python:3.8

# Install spaCy and download the English model
RUN pip install spacy && python -m spacy download en_core_web_md

# Set the working directory
WORKDIR /app

# Copy the application files
COPY watch_next.py .

# Run the script
CMD ["python", "watch_next.py"]
