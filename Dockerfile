# ----------------------------
#  Base Image
# ----------------------------
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Disable .pyc and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install essential OS packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc wget && \
    rm -rf /var/lib/apt/lists/*

# ----------------------------
# Copy project files
# ----------------------------
COPY requirements.txt /app/
COPY main.py /app/
COPY email_sender.py /app/
COPY config.py /app/
COPY index.html /app/
COPY .env /app/

# ----------------------------
# Install Python dependencies
# ----------------------------
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# ----------------------------
# Run FastAPI app
# ----------------------------
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
