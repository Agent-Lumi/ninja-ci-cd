# 🥷 Ninja CI/CD Pipeline Documentation

## Overview

This document provides detailed information about the Ninja CI/CD pipeline architecture and workflows.

## Table of Contents

1. [Pipeline Architecture](#pipeline-architecture)
2. [CI Workflow (Shadow Strike)](#ci-workflow)
3. [CD Workflow (Silent Step)](#cd-workflow)
4. [Nightly Scans (Night Watch)](#nightly-scans)
5. [PR Checks (Quick Draw)](#pr-checks)

## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     🥷 Ninja CI/CD                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │   CI     │───▶│   CD     │───▶│ Notify   │              │
│  │ (Shadow  │    │ (Silent  │    │ (Beacon) │              │
│  │  Strike) │    │  Step)   │    │          │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│       │                │                                     │
│       ▼                ▼                                     │
│  ┌──────────┐    ┌──────────┐                              │
│  │  Night   │    │   PR     │                               │
│  │  Watch   │    │  Checks  │                               │
│  │(Nightly) │    │(Quick   │                               │
│  │          │    │  Draw)  │                               │
│  └──────────┘    └──────────┘                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## CI Workflow

### Shadow Strike CI (`ci.yml`)

The main CI workflow runs on every pull request and push to main/develop branches.

#### Phase 1: Code Reconnaissance
- **Black**: Code formatting
- **isort**: Import organization
- **Flake8**: Linting
- **Bandit**: Security linting

#### Phase 2: Trial by Combat
- Tests across Python 3.10, 3.11, 3.12
- Coverage reporting with pytest-cov
- Parallel execution with pytest-xdist

#### Phase 3: Container Crafting
- Multi-stage Docker builds
- Health checks
- Artifact generation

#### Phase 4: Security Ritual
- Safety vulnerability scanning
- pip-audit dependency check
- Trivy container scanning

## CD Workflow

### Silent Step CD (`cd.yml`)

Automated deployment workflow triggered on main branch pushes.

#### Phase 1: Scroll of Knowledge
- Semantic versioning
- Git tag extraction
- Release notes generation

#### Phase 2: Forge Production Blade
- Multi-architecture builds (amd64, arm64)
- GitHub Container Registry push
- Docker layer caching

#### Phase 3: Silent Deployment
- Zero-downtime deployment
- Health verification
- Rollback on failure

#### Phase 4: Ninja Beacon
- GitHub Releases creation
- Discord notifications
- Deployment manifest upload

## Nightly Scans

### Night Watch (`nightly.yml`)

Scheduled security scans run at midnight UTC.

#### Scans Performed:
1. **CodeQL Analysis**: Static code analysis
2. **Dependency Audit**: Vulnerable package detection
3. **Container Scan**: Image vulnerability scanning
4. **Secret Detection**: Exposed credential detection

### Alerting:
- Automatic GitHub issue creation on failure
- Email notifications (optional)
- Slack/Discord webhooks (optional)

## PR Checks

### Quick Draw (`pr-checks.yml`)

Fast feedback on pull requests with automatic labeling.

#### Checks:
1. **Lightning Strike**: Fast pytest execution
2. **Shadow Glance**: Quick lint checks
3. **Clan Marking**: Auto-labeling based on changed files
4. **Mission Briefing**: PR description validation

### Auto-Labels:
- `python` - Python code changes
- `docker` - Dockerfile changes
- `tests` - Test file changes
- `ci-cd` - Workflow changes
- `documentation` - README/docs changes
- Size labels (xs, s, m, l, xl) based on PR size

## Workflow Triggers

| Workflow | Trigger | When |
|----------|---------|------|
| Shadow Strike CI | `push`, `pull_request` | Any branch |
| Silent Step CD | `push` | Main branch only |
| Night Watch | `schedule` | Midnight UTC daily |
| Quick Draw | `pull_request` | On PR open/sync |

## Secrets Required

Configure these in your GitHub repository settings:

- `DISCORD_WEBHOOK`: Discord notification URL
- `CODECOV_TOKEN`: Codecov upload token
- `GITHUB_TOKEN`: Auto-provided

## Best Practices Demonstrated

### 1. Security First
- Multi-layer security scanning
- Secret detection in pre-commit hooks
- Container vulnerability scanning
- Dependency auditing

### 2. Speed Optimization
- Parallel test execution
- Docker layer caching
- Matrix builds
- Conditional job execution

### 3. Quality Gates
- Code coverage thresholds
- Lint checks
- Type hints (optional)
- Pre-commit hooks

### 4. Observability
- Detailed job summaries
- Artifact uploads
- Health checks
- Deployment manifests

## Troubleshooting

### Common Issues:

**Tests failing locally but passing in CI**
- Check Python version (CI tests 3.10, 3.11, 3.12)
- Ensure all dependencies installed: `pip install -e ".[dev]"`

**Docker build fails**
- Check Docker daemon running
- Verify Dockerfile syntax: `docker build -t test .`

**Security scans flagging false positives**
- Review and update `.bandit` configuration
- Add `# nosec` comments for intentional patterns
- Update `pyproject.toml` exclusions

## Contributing

To add a new workflow:

1. Create YAML file in `.github/workflows/`
2. Follow ninja naming convention
3. Add to this documentation
4. Test with `act` locally if possible

---

*"A well-crafted pipeline strikes without warning and deploys without error."* 🥷
