# Prophet Homes Investor System - Setup Guide

## 🚀 Quick Start (5 Minutes)

### 1. Clone or Download Repository

```bash
git clone https://github.com/yourusername/prophet-homes-investor-system.git
cd prophet-homes-investor-system
```

### 2. Set Up Environment

```bash
# Copy environment template
cp .env.example .env

# Edit with your API keys
nano .env  # or use your favorite editor
```

**Required API Keys:**
- Anthropic API Key (get from https://console.anthropic.com/)
- Google Cloud credentials for Gmail/Sheets (optional for testing)

### 3. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 4. Test the System

```bash
# Test property analyzer
python claude-analyzer/property_analyzer.py

# Test recommendation engine  
python recommendation-engine/matcher.py

# Test email system (simulated without Gmail API)
python email-automation/sender.py
```

---

## 🐳 Docker Deployment (Recommended for Production)

### Start All Services

```bash
# Start everything with one command
docker-compose up -d

# Check status
docker-compose ps
```

**Services will be available at:**
- API: http://localhost:8000
- n8n Automation: http://localhost:5678
- Streamlit Dashboard: http://localhost:8501 (if enabled)
- PostgreSQL: localhost:5432

### Stop Services

```bash
docker-compose down

# With data cleanup
docker-compose down -v
```

---

## 📋 Detailed Setup Steps

### Step 1: Get Anthropic API Key

1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Navigate to API Keys
4. Create new key
5. Copy to `.env` file as `ANTHROPIC_API_KEY`

### Step 2: Set Up Google APIs (Optional but Recommended)

#### Gmail API Setup

1. Go to https://console.cloud.google.com/
2. Create new project: "Prophet Homes Investor System"
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Download credentials as JSON
6. Save to project directory
7. Update `.env` with path: `GOOGLE_CREDENTIALS_PATH=/path/to/credentials.json`

#### Google Sheets API Setup

1. In same Google Cloud project
2. Enable Google Sheets API
3. Use same OAuth credentials
4. Create a Google Sheet for tracking
5. Copy Sheet ID from URL
6. Update `.env`: `GOOGLE_SHEETS_ID=your-sheet-id`

### Step 3: Configure Database

#### Option A: PostgreSQL (Production)

```bash
# If using Docker Compose, it's automatic
# Otherwise, install PostgreSQL and run:

createdb prophet_homes_db
psql prophet_homes_db < data/schema.sql
```

#### Option B: SQLite (Development)

```bash
# Just update .env
DATABASE_URL=sqlite:///./prophet_homes.db

# Initialize
python scripts/init_db.py
```

### Step 4: Set Up n8n (Optional)

```bash
# Already included in docker-compose.yml

# Access at http://localhost:5678
# Default credentials:
#   Username: admin
#   Password: prophet_admin_123

# Import workflows from n8n-workflows/ directory
```

### Step 5: Train Recommendation Model

```bash
# Using sample data
python recommendation-engine/train_model.py

# Or with your data
python recommendation-engine/train_model.py \
    --interactions data/your_interactions.csv \
    --epochs 50
```

---

## 🔧 Configuration Guide

### Environment Variables Explained

#### Core Settings

```bash
# Claude AI
ANTHROPIC_API_KEY=sk-ant-...          # Required
CLAUDE_MODEL=claude-sonnet-4-20250514  # Default model

# Database
DATABASE_URL=postgresql://...          # Required

# Email
GMAIL_USER_EMAIL=your@email.com        # For outreach
MAX_EMAILS_PER_HOUR=50                 # Rate limiting
```

#### Recommendation Engine

```bash
LIGHTFM_COMPONENTS=30      # Model complexity (higher = more patterns)
LIGHTFM_EPOCHS=50          # Training iterations
MIN_MATCH_SCORE=60         # Minimum score to recommend (0-100)
TOP_N_RECOMMENDATIONS=5    # How many investors to match per property
```

#### Property Analysis

```bash
DEFAULT_VACANCY_RATE=0.05         # 5% vacancy assumption
DEFAULT_MAINTENANCE_RATE=0.10     # 10% maintenance
DEFAULT_PROPERTY_MGMT_FEE=0.08    # 8% management fee
```

---

## 📊 Sample Data Setup

### Load Sample Investors and Properties

```bash
# Sample data is in /data directory
python scripts/load_sample_data.py

# This creates:
# - 100 sample investors
# - 50 sample properties  
# - 200 historical interactions
```

### Or Use Your Own Data

Required CSV format:

**investors.csv:**
```csv
investor_id,name,email,phone,budget_min,budget_max,experience_level,risk_tolerance,strategy_preference,preferred_markets
INV001,John Smith,john@example.com,555-0001,200000,400000,intermediate,medium,fix-and-flip,"Dallas,Austin"
```

**properties.csv:**
```csv
property_id,address,purchase_price,arv,rehab_cost,property_type,market,bedrooms,bathrooms,sqft
PROP001,123 Main St Dallas TX,250000,350000,50000,Single Family,Dallas,3,2,1800
```

**interactions.csv:**
```csv
investor_id,property_id,interaction_type,date
INV001,PROP001,viewed,2025-01-15
INV001,PROP002,purchased,2025-02-01
```

---

## 🔄 Complete Workflow Example

### Scenario: New Property from Acquisitions Team

```bash
# 1. Analyze property with Claude
python -c "
from claude_analyzer.property_analyzer import PropertyAnalyzer

analyzer = PropertyAnalyzer()
analysis = analyzer.analyze_property({
    'address': '456 Oak St, Dallas, TX',
    'purchase_price': 275000,
    'arv': 375000,
    'rehab_cost': 45000
})
print(analysis['raw_analysis'])
"

# 2. Find matching investors
python -c "
from recommendation_engine.matcher import InvestorMatcher

matcher = InvestorMatcher()
matcher.load_model('models/investor_matcher.pkl')

matches = matcher.find_best_investors('PROP_NEW', top_n=5)
for m in matches:
    print(f'{m[\"investor_id\"]}: {m[\"match_score\"]}%')
"

# 3. Send personalized emails
python -c "
from email_automation.sender import EmailCampaign

campaign = EmailCampaign()
campaign.add_recipients(matches)
campaign.customize_for_each_investor(property_data, agent_data)
results = campaign.execute()
print(f'Sent: {results[\"sent\"]} emails')
"

# 4. Track in CRM (Google Sheets or Frappe)
python -c "
from crm_integration.sheets_sync import SheetsSync

sync = SheetsSync()
sync.log_outreach(property_id, matches, results)
"
```

---

## 🎯 Integration with Prophet Homes

### Connect to Your Acquisitions Data

1. **Option A: Google Sheets Integration**
   - Acquisitions team updates Google Sheet
   - n8n workflow triggers on new row
   - Automatically analyzes and matches

2. **Option B: Email Integration**
   - Forward acquisition emails to system
   - n8n parses email content
   - Extracts property data automatically

3. **Option C: API Integration**
   - Prophet Homes CRM sends webhook
   - API receives property data
   - Processes and matches automatically

### Example n8n Workflow

```yaml
Trigger: New row in Google Sheet "Acquisitions"
↓
Node 1: Extract property data
↓
Node 2: HTTP Request to analyze_property endpoint
↓
Node 3: HTTP Request to find_best_investors endpoint
↓
Node 4: Generate personalized emails
↓
Node 5: Send via Gmail API
↓
Node 6: Log to Google Sheets "Outreach Tracker"
```

---

## 🧪 Testing

### Run All Tests

```bash
pytest tests/
```

### Test Individual Components

```bash
# Property analyzer
pytest tests/test_property_analyzer.py

# Recommendation engine
pytest tests/test_matcher.py

# Email system
pytest tests/test_email.py
```

---

## 🐛 Troubleshooting

### Common Issues

#### "anthropic module not found"
```bash
pip install --upgrade anthropic
```

#### "Gmail API quota exceeded"
- Check daily sending limits (default: 500/day for free Gmail)
- Reduce MAX_EMAILS_PER_HOUR in .env
- Consider upgrading to Google Workspace

#### "Model file not found"
```bash
# Train the model first
python recommendation-engine/train_model.py
```

#### "PostgreSQL connection failed"
```bash
# Check if PostgreSQL is running
docker-compose ps

# Restart database
docker-compose restart postgres
```

---

## 📈 Monitoring & Maintenance

### View Logs

```bash
# Docker logs
docker-compose logs -f

# API logs
tail -f logs/prophet_homes.log

# n8n execution logs
# Access via web interface: http://localhost:5678/workflows
```

### Database Backups

```bash
# Backup PostgreSQL
docker-compose exec postgres pg_dump -U prophet_user prophet_homes_db > backup.sql

# Restore
docker-compose exec -T postgres psql -U prophet_user prophet_homes_db < backup.sql
```

### Update Model

```bash
# Retrain with new data monthly
python recommendation-engine/train_model.py \
    --interactions data/interactions_$(date +%Y%m).csv \
    --epochs 50

# Save with date
mv models/investor_matcher.pkl models/investor_matcher_$(date +%Y%m%d).pkl
```

---

## 🚀 Production Deployment

### Deploy to AWS/GCP/Azure

1. Set up cloud database (RDS/Cloud SQL)
2. Deploy Docker containers to ECS/Cloud Run/AKS
3. Configure environment variables in cloud console
4. Set up load balancer and SSL certificates
5. Configure monitoring and alerting

### Scaling Considerations

- **For <100 properties/month**: Single server is fine
- **For 100-1000 properties/month**: Add Redis caching, scale API horizontally
- **For >1000 properties/month**: Consider Kubernetes, separate microservices

---

## 📞 Support

**Need Help?**
- GitHub Issues: [repo]/issues
- Email: sklutjack@gmail.com
- Prophet Homes Internal: Slack #investor-relations-tech

**Next Steps:**
1. Complete this setup
2. Load your actual investor/property data
3. Train model on historical matches
4. Start with small test campaign
5. Scale gradually

---

Last Updated: November 2025
