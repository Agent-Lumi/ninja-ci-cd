# Contributing to 🥷 Ninja CI/CD

Thank you for your interest in contributing! This document provides guidelines for contributing to the Ninja CI/CD showcase.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR-USERNAME/ninja-ci-cd.git`
3. Create a virtual environment: `python -m venv .venv`
4. Activate it: `source .venv/bin/activate`
5. Install dev dependencies: `pip install -e ".[dev]"`
6. Install pre-commit hooks: `pre-commit install`

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Write clean, readable code
- Follow PEP 8 style guidelines
- Add tests for new functionality
- Update documentation as needed

### 3. Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src/ninja --cov-report=html

# Run specific test file
pytest tests/test_core.py -v
```

### 4. Check Code Quality

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint
flake8 src/ tests/

# Security check
bandit -r src/
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "🥷 Add your feature description"
```

### 6. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Commit Message Convention

Use emoji prefixes for commit messages:

- 🥷 `:ninja:` - New feature
- 🐛 `:bug:` - Bug fix
- 📚 `:books:` - Documentation
- ⚡ `:zap:` - Performance improvement
- 🔒 `:lock:` - Security fix
- ⬆️ `:arrow_up:` - Dependency update
- 🧪 `:test_tube:` - Test changes
- ♻️ `:recycle:` - Refactoring

## Code Standards

### Python Style

- Follow PEP 8
- Use type hints where appropriate
- Maximum line length: 88 characters
- Use docstrings for all public functions/classes

### Testing

- Write tests for all new functionality
- Maintain 80%+ code coverage
- Use pytest fixtures for test setup
- Name tests descriptively: `test_function_name_scenario`

### Documentation

- Update README.md if adding features
- Update docs/PIPELINE.md for CI/CD changes
- Add docstrings to new modules/functions
- Keep CHANGELOG.md updated

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Ensure all CI checks pass
3. Request review from maintainers
4. Address review feedback
5. Squash commits if requested
6. Your PR will be merged once approved!

## Reporting Issues

When reporting bugs, please include:

- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS)
- Relevant log output

## Questions?

Feel free to open an issue for questions or join discussions!

---

*Remember: A true ninja writes code that is clean, tested, and well-documented.* 🥷
