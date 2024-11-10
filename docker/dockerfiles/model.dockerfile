# Use Ubuntu as the base image
FROM ubuntu:20.04

# Set environment variable to non-interactive to disable prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update and install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    ca-certificates \
    libeigen3-dev \
    libssl-dev \
    libsndfile1 \
    libopencv-dev \
    locales \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

RUN pip install torchaudio[sox_io]
# Install PyTorch and other Python dependencies
RUN pip install --no-cache-dir \
    torch \
    torchaudio \
    transformers \
    assemblyai \
    num2words \
    matplotlib \
    nltk \
    ipython

# Set working directory
WORKDIR /app

# Copy your application files
COPY speech-model /app/speech-model
COPY docker/entrypoints/pytorch.sh /root
RUN chmod +x /root/pytorch.sh