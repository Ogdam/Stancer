FROM python:3.11-slim

# Install curl and build-essential for uv
RUN apt-get update && \
    apt-get install -y curl build-essential && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    apt-get remove -y curl build-essential && \
    apt-get autoremove -y && \
    apt-get clean

# Set workdir
WORKDIR /workspace

# Copy the project (the devcontainer will mount this anyway)
COPY . /workspace

# Install Python deps using uv
RUN uv pip install --system -r requirements.txt