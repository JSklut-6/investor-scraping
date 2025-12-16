# How to Upload This Project to GitHub

## Option 1: Using GitHub Desktop (Easiest)

1. **Download GitHub Desktop**
   - Go to https://desktop.github.com/
   - Install and sign in with your GitHub account

2. **Create Repository**
   - Open GitHub Desktop
   - File → New Repository
   - Name: `prophet-homes-investor-system`
   - Local Path: Choose where this project folder is
   - Click "Create Repository"

3. **Publish to GitHub**
   - Click "Publish repository" button
   - Choose: Public or Private
   - Click "Publish repository"

**Done!** Your code is now on GitHub.

---

## Option 2: Using Command Line

### First Time Setup

```bash
# Navigate to project directory
cd prophet-homes-investor-system

# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Prophet Homes Investor Relations System"

# Create repository on GitHub.com first, then:
git remote add origin https://github.com/YOUR_USERNAME/prophet-homes-investor-system.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Create Repository on GitHub.com

1. Go to https://github.com/new
2. Repository name: `prophet-homes-investor-system`
3. Description: "AI-powered real estate investor relations system"
4. Choose Public or Private
5. **Don't** check "Add README" (we already have one)
6. Click "Create repository"
7. Copy the URL and use in commands above

---

## Option 3: Import Existing Folder

1. **On GitHub.com:**
   - Click "+" → New repository
   - Name: `prophet-homes-investor-system`
   - Create repository

2. **In Terminal:**
   ```bash
   cd prophet-homes-investor-system
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/prophet-homes-investor-system.git
   git push -u origin main
   ```

---

## What Files to Include

### ✅ Include These:
- All `.py` files
- `README.md`
- `requirements.txt`
- `.env.example` (template only)
- `docker-compose.yml`
- `/docs` folder
- `/data` folder (sample data only)

### ❌ Don't Include These:
- `.env` (contains your API keys!)
- `*.pkl` (trained models - too large)
- `*.pyc` (Python bytecode)
- `/venv` (virtual environment)
- `__pycache__/`
- `/logs`

### Create `.gitignore` File

Create a file named `.gitignore` in the project root:

```gitignore
# Environment
.env
.env.local
*.env

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
*.egg-info/

# Models (too large for git)
*.pkl
*.h5
*.pb
models/*.pkl

# Logs
*.log
logs/
*.log.*

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Database
*.db
*.sqlite
*.sqlite3

# Docker
docker-compose.override.yml

# Large files
*.csv.gz
*.zip
*.tar.gz

# Credentials
credentials.json
token.json
*-credentials.json
```

---

## Make Repository Public or Private?

### Public Repository (Recommended)
**Pros:**
- Free unlimited hosting
- Others can contribute
- Good for portfolio
- Open source community benefits

**Cons:**
- Anyone can see the code
- Need to be careful with API keys

### Private Repository
**Pros:**
- Code stays confidential
- Good for proprietary systems

**Cons:**
- Limited free private repos on some plans

**For Prophet Homes:** Consider starting private, then making public after removing any sensitive business logic.

---

## Protect Your API Keys

**CRITICAL:** Never commit API keys to GitHub!

### Before Pushing:

1. **Check `.env` is in `.gitignore`:**
   ```bash
   cat .gitignore | grep .env
   ```

2. **Remove `.env` if accidentally added:**
   ```bash
   git rm .env --cached
   git commit -m "Remove .env file"
   ```

3. **Verify before pushing:**
   ```bash
   git status
   # Make sure .env is NOT listed
   ```

### If You Accidentally Pushed Keys:

1. **Immediately rotate your API keys**
   - Anthropic: https://console.anthropic.com/
   - Google: https://console.cloud.google.com/

2. **Remove from history:**
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch .env" \
     --prune-empty --tag-name-filter cat -- --all
   
   git push origin --force --all
   ```

---

## Ongoing Updates

### After Making Changes:

```bash
# See what changed
git status

# Add changes
git add .

# Commit with message
git commit -m "Add email template improvements"

# Push to GitHub
git push
```

### Creating Branches for Features:

```bash
# Create new feature branch
git checkout -b feature/sms-integration

# Make changes, commit
git add .
git commit -m "Add SMS notification feature"

# Push branch
git push -u origin feature/sms-integration

# On GitHub: Create Pull Request
# After review: Merge to main
```

---

## Collaboration Setup

### Allow Team Access:

1. Go to repository on GitHub
2. Settings → Collaborators
3. Add team members by username
4. They can now clone and contribute

### Team Workflow:

```bash
# Team member clones
git clone https://github.com/YOUR_USERNAME/prophet-homes-investor-system.git
cd prophet-homes-investor-system

# Create their own .env file
cp .env.example .env
# Add their own API keys

# Before starting work
git pull

# After changes
git add .
git commit -m "Description of changes"
git push
```

---

## GitHub Repository Settings

### Recommended Settings:

1. **Add Description:**
   - "AI-powered investor relations system for Prophet Homes real estate"

2. **Add Topics:**
   - `real-estate`
   - `investor-relations`
   - `claude-ai`
   - `python`
   - `n8n`
   - `crm`
   - `recommendation-system`

3. **Add README Badges:**
   ```markdown
   ![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
   ![License](https://img.shields.io/badge/license-MIT-green.svg)
   ![Status](https://img.shields.io/badge/status-active-success.svg)
   ```

4. **Enable Issues:**
   - Settings → Features → Check "Issues"

5. **Add License:**
   - Add LICENSE file with MIT license

---

## Showcase Your Work

### For Your Resume/Portfolio:

1. **Pin Repository:**
   - Go to your GitHub profile
   - Click "Customize pins"
   - Select this repo

2. **Add Demo Screenshots:**
   - Create `/screenshots` folder
   - Add images to README

3. **Record Demo Video:**
   - Use Loom or OBS
   - Show system in action
   - Link in README

4. **Write Blog Post:**
   - Medium article about building it
   - Link to GitHub repo

---

## Need Help?

**Git Issues:**
- https://docs.github.com/en/get-started

**Collaborating:**
- https://docs.github.com/en/pull-requests

**GitHub Desktop:**
- https://docs.github.com/en/desktop

---

## Quick Command Reference

```bash
# Check status
git status

# Pull latest changes
git pull

# Add all files
git add .

# Commit with message
git commit -m "Your message"

# Push to GitHub
git push

# View commit history
git log

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Create branch
git checkout -b branch-name

# Switch branches
git checkout main
```

---

**You're ready to upload to GitHub!** 🚀

Choose your method above and get started.

If you get stuck, just ask for help!
