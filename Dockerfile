# ───────────────────────────────────────────────
# BASE IMAGE
# ───────────────────────────────────────────────
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Prevent Python from generating .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install essential system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Default command to start FastAPI with auto reload OFF (production)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
