# Use Python 3.11 as base image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    make \
    mercurial \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /catsoop

# Clone the repository, install, and run tests
RUN git clone https://github.com/El-Guapo2024/catsoop-mirror.git . 
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip3 install -e .
#RUN pytest catsoop/test
# Copy configuration file
COPY config.py /root/.config/catsoop/config.py
RUN chmod 644 /root/.config/catsoop/config.py

# Create course directories
RUN mkdir -p /.local/share/catsoop/courses/number_sense 

# Copy everything except what's in .dockerignore
COPY . /.local/share/catsoop/courses/number_sense/

RUN chmod -R 755 /.local/share/catsoop/courses/number_sense 

# Add Python logging configuration
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/catsoop

# Expose the default CAT-SOOP port
EXPOSE 7667

# Start CAT-SOOP
CMD ["catsoop", "start"] 