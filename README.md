# 🥷 Ninja CI/CD Showcase

> "Move silently, deploy swiftly, leave no bugs behind." - The Ninja Way

[![🥷 Shadow Strike CI](https://github.com/Agent-Lumi/ninja-ci-cd/actions/workflows/ci.yml/badge.svg)](https://github.com/Agent-Lumi/ninja-ci-cd/actions/workflows/ci.yml)
[![🥷 Silent Step CD](https://github.com/Agent-Lumi/ninja-ci-cd/actions/workflows/cd.yml/badge.svg)](https://github.com/Agent-Lumi/ninja-ci-cd/actions/workflows/cd.yml)
[![🥷 Night Watch](https://github.com/Agent-Lumi/ninja-ci-cd/actions/workflows/nightly.yml/badge.svg)](https://github.com/Agent-Lumi/ninja-ci-cd/actions/workflows/nightly.yml)
[![codecov](https://codecov.io/gh/Agent-Lumi/ninja-ci-cd/branch/main/graph/badge.svg)](https://codecov.io/gh/Agent-Lumi/ninja-ci-cd)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A creative, fully-functional CI/CD pipeline showcase with a ninja theme! Demonstrates modern DevOps practices including automated testing, security scanning, containerization, and deployment automation.

## 🥷 What's This?

**Ninja CI/CD** is a demonstration repository that showcases modern CI/CD best practices through a fun, ninja-themed application. It's designed to be:

- 🎯 **Educational**: Learn modern CI/CD patterns through a working example
- ⚡ **Fast**: Lightning-fast pipelines with smart caching and parallelization
- 🔒 **Secure**: Built-in security scanning at every stage
- 🎨 **Creative**: Themed approach makes learning DevOps fun!

## 🏯 Architecture

```
🥷 Ninja CI/CD Pipeline
│
├── 🌙 Shadow Step CI (ci.yml)
│   ├── 🔍 Code Reconnaissance (Linting, formatting)
│   ├── ⚔️ Trial by Combat (Testing across Python versions)
│   ├── 📦 Container Crafting (Docker builds)
│   └── 🔒 Security Ritual (Vulnerability scans)
│
├── 🚀 Silent Step CD (cd.yml)
│   ├── 📜 Scroll of Knowledge (Versioning)
│   ├── 🔨 Forge Production Blade (Build & push)
│   ├── 🚀 Silent Deployment (Zero-downtime deploy)
│   └── 🔔 Ninja Beacon (Notifications)
│
├── 🌃 Night Watch (nightly.yml)
│   ├── 🔮 Crystal Ball Analysis (CodeQL)
│   ├── 🔍 Clan Supply Check (Dependency audit)
│   └── 🐳 Container Seal (Image scanning)
│
└── ⚡ Quick Draw (pr-checks.yml)
    ├── ⚡ Lightning Strike (Fast tests)
    ├── 🔍 Shadow Glance (Quick lint)
    └── 🏷️ Clan Marking (Auto-labeling)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Docker (optional, for containerization)

### Installation

```bash
# Clone the repository
git clone https://github.com/Agent-Lumi/ninja-ci-cd.git
cd ninja-ci-cd

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v --cov=src/ninja
```

### Running the Application

```bash
# Start the web dashboard
python -m ninja.app

# Or with Flask directly
flask --app src/ninja/app run
```

Visit `http://localhost:5000` to see the ninja dashboard! 🥷

## 📁 Project Structure

```
ninja-ci-cd/
├── .github/
│   ├── dependabot.yml              # Dependency automation
│   ├── labeler.yml                 # PR auto-labeling rules
│   └── workflows/
│       ├── ci.yml                  # 🥷 Shadow Strike CI
│       ├── cd.yml                  # 🚀 Silent Step CD
│       ├── nightly.yml             # 🌃 Night Watch
│       └── pr-checks.yml           # ⚡ Quick Draw
├── src/
│   └── ninja/
│       ├── __init__.py             # Ninja package
│       ├── core.py                 # 🥷 Ninja Core
│       ├── skills.py               # ⚔️ Ninja Skills
│       └── app.py                  # 🌐 Web Dashboard
├── tests/
│   ├── __init__.py
│   ├── test_core.py                # Core functionality tests
│   ├── test_skills.py              # Skills tests
│   └── test_app.py                 # Web app tests
├── Dockerfile                      # 🐳 Container definition
├── docker-compose.yml              # Multi-container setup
├── pyproject.toml                  # 📦 Project configuration
├── requirements.txt                # Production dependencies
├── requirements-dev.txt            # Development dependencies
├── .pre-commit-config.yaml         # 🪝 Git hooks
├── README.md                       # 📖 This file
└── docs/
    └── PIPELINE.md                 # 📚 Detailed pipeline docs
```

## 🥷 The Ninja Techniques

Our CI/CD pipeline uses these ninja techniques:

| Technique | Description | Pipeline Phase |
|-----------|-------------|----------------|
| **Shadow Clone** | Parallel test execution | CI - Trial by Combat |
| **Silent Step** | Zero-downtime deployment | CD - Silent Deployment |
| **Smoke Bomb** | Automatic rollback on failure | CD - Silent Deployment |
| **Dragon Fire** | High-performance builds | CI - Container Crafting |
| **Water Walking** | Cross-platform compatibility | CI - Trial by Combat |
| **Mind Transfer** | Configuration as code | All workflows |
| **Rasengan** | Dependency caching | CI/CD - All phases |
| **Chidori** | Lightning-fast tests | PR Checks - Quick Draw |

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Web server port | `5000` |
| `NINJA_CLAN` | Your ninja clan name | `Shadow CI/CD` |
| `NINJA_MODE` | Operation mode (stealth/strike) | `stealth` |

### Secrets Required

The following secrets should be configured in your GitHub repository:

- `DISCORD_WEBHOOK` - Discord notifications (optional)
- `CODECOV_TOKEN` - Code coverage reporting (optional)

## 📊 Pipeline Stages Explained

### 🔍 Phase 1: Code Reconnaissance
- **Black**: Code formatting check
- **isort**: Import sorting verification
- **Flake8**: Linting and style checks
- **Bandit**: Security linting

### ⚔️ Phase 2: Trial by Combat
- **pytest**: Unit and integration tests
- **pytest-cov**: Code coverage reporting
- **pytest-xdist**: Parallel test execution
- **Codecov**: Coverage upload and tracking

### 📦 Phase 3: Container Crafting
- **Docker Build**: Multi-architecture images
- **Container Tests**: Health checks
- **Trivy**: Container vulnerability scanning

### 🔒 Phase 4: Security Ritual
- **Safety**: Dependency vulnerability scanning
- **pip-audit**: Python package auditing
- **CodeQL**: Static code analysis

### 🚀 Phase 5: Silent Deployment
- **Semantic Versioning**: Automatic versioning
- **Container Registry**: GitHub Container Registry
- **GitHub Releases**: Automated release creation
- **Discord Notifications**: Deployment alerts

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src/ninja --cov-report=html

# Run specific test file
pytest tests/test_core.py -v

# Run in parallel (ninja speed!)
pytest tests/ -n auto
```

## 🐳 Docker Usage

```bash
# Build the image
docker build -t ninja-ci-cd .

# Run locally
docker run -p 5000:5000 ninja-ci-cd

# Run with docker-compose
docker-compose up -d
```

## 📈 Monitoring

The application exposes several endpoints for monitoring:

- `GET /` - Dashboard
- `GET /api/health` - Health check
- `GET /api/stats` - Ninja statistics
- `GET /api/techniques` - Available techniques

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by modern CI/CD practices and the stealth of ninjas
- Built with ❤️ by Agent-Lumi
- Special thanks to the GitHub Actions team for their amazing platform

---

> "The ninja who violates the CI/CD pipeline must be punished."

**Ready to become a CI/CD ninja?** 🥷 Clone the repo and start your journey!