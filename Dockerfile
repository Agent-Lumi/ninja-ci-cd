# 🐳 Ninja CI/CD Container
# Multi-stage build for production-ready ninja applications

FROM python:3.12-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    NINJA_CLAN="Shadow CI/CD" \
    NINJA_MODE="stealth"

# Create non-root ninja user
RUN groupadd -r ninja && useradd -r -g ninja ninja

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 🥷 Builder stage
FROM base AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install requirements
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY pyproject.toml .

# Install the package
RUN pip install --user --no-cache-dir -e .

# 🥷 Production stage
FROM base AS production

# Copy installed packages from builder
COPY --from=builder /root/.local /home/ninja/.local

# Set PATH
ENV PATH=/home/ninja/.local/bin:$PATH

# Copy application code
COPY --from=builder /app/src ./src
COPY --from=builder /app/pyproject.toml .

# Set ownership
RUN chown -R ninja:ninja /app /home/ninja

# Switch to non-root user
USER ninja

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/api/health || exit 1

# Expose port
EXPOSE 5000

# 🥷 Launch the ninja application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--threads", "2", "--timeout", "60", "--access-logfile", "-", "--error-logfile", "-", "ninja.app:app"]

# 🥷 Development stage
FROM base AS development

# Install dev dependencies
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy source code
COPY . .

# Install in editable mode
RUN pip install -e ".[dev]"

EXPOSE 5000

CMD ["flask", "--app", "src/ninja/app", "run", "--host=0.0.0.0", "--debug"]