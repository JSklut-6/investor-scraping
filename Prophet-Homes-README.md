# Prophet Homes Investor Relations System

An open-source, AI-powered real estate investor relations platform that automates property analysis, investor matching, and outreach campaigns.

## 🎯 Overview

This system helps real estate investor relations teams:
- Analyze properties from acquisitions team
- Match properties to investors based on their criteria
- Automate personalized email outreach
- Track deals through the pipeline
- Calculate ROI and investment metrics

Built specifically for fix-and-flip and fix-and-rent investment properties.

## 🏗️ Architecture

```
┌─────────────────┐
│  Acquisitions   │
│   Team Data     │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│   Claude AI Property Analyzer           │
│   - Financial Analysis                  │
│   - Market Research                     │
│   - ROI Calculations                    │
└────────┬────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│   LightFM Recommendation Engine         │
│   - Investor-Property Matching          │
│   - Score-based Ranking                 │
│   - Preference Learning                 │
└────────┬────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│   Email Automation System               │
│   - Personalized Templates              │
│   - Automated Follow-ups                │
│   - Gmail Integration                   │
└────────┬────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│   CRM Pipeline Tracking                 │
│   - Deal Stages                         │
│   - Conversation History                │
│   - Google Sheets Sync                  │
└─────────────────────────────────────────┘
```

## 🚀 Features

### Property Analysis
- **ROI Calculator**: IRR, Cash-on-Cash, Cap Rate, DSCR, GRM
- **Market Analysis**: Comparative analysis, neighborhood trends
- **Cost Estimation**: Rehab costs, holding costs, closing costs
- **Risk Assessment**: Market risk, property condition, financing risk

### Investor Matching
- **Criteria-Based Matching**: Budget, ROI targets, property types, locations
- **Learning Algorithm**: Improves based on past successful matches
- **Scoring System**: Ranks investors by fit (0-100)
- **Preference Tracking**: Updates investor profiles automatically

### Email Automation
- **Dynamic Templates**: Uses Jinja2 for personalization
- **Smart Scheduling**: Optimal send times based on investor behavior
- **Follow-up Sequences**: Automated 3-5 touch campaigns
- **Gmail API Integration**: Tracks opens, replies, engagement

### CRM & Pipeline
- **Deal Stages**: Lead → Qualified → Presentation → Negotiation → Closed
- **Activity Logging**: Calls, emails, meetings automatically tracked
- **Google Sheets Sync**: Real-time data sync for team visibility
- **Reporting Dashboard**: KPIs, conversion rates, velocity metrics

## 🛠️ Technology Stack

- **Backend**: Python 3.10+
- **AI/ML**: Anthropic Claude API, LightFM, Scikit-learn
- **Automation**: n8n (self-hosted)
- **CRM**: Frappe CRM or EspoCRM
- **Database**: PostgreSQL
- **Email**: Gmail API, pyautomail
- **Spreadsheets**: Google Sheets API
- **Containerization**: Docker & Docker Compose

## 📦 Installation

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- Git
- Anthropic API Key
- Google Cloud Project (for Gmail/Sheets APIs)

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/prophet-homes-investor-system.git
cd prophet-homes-investor-system

# 2. Copy environment variables
cp .env.example .env
# Edit .env with your API keys

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Start services with Docker
docker-compose up -d

# 5. Initialize the database
python scripts/init_db.py

# 6. Train the recommendation model (optional - sample data included)
python recommendation-engine/train_model.py

# 7. Test the system
python scripts/test_system.py
```

## 🔑 Configuration

### Environment Variables

```bash
# Claude AI
ANTHROPIC_API_KEY=your_key_here

# Google APIs
GOOGLE_SHEETS_CREDENTIALS=/path/to/credentials.json
GMAIL_CREDENTIALS=/path/to/gmail_credentials.json

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/prophet_homes

# Email Settings
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password

# n8n (optional if using n8n automation)
N8N_WEBHOOK_URL=http://localhost:5678/webhook/investor-matching
```

## 📖 Usage

### 1. Analyze a Property

```python
from claude_analyzer import PropertyAnalyzer

analyzer = PropertyAnalyzer(api_key="your_anthropic_key")

property_data = {
    "address": "123 Main St, Dallas, TX 75201",
    "purchase_price": 250000,
    "arv": 350000,
    "rehab_cost": 50000,
    "property_type": "Single Family"
}

analysis = analyzer.analyze_property(property_data)
print(analysis['roi'])  # Expected ROI
print(analysis['recommendations'])  # AI insights
```

### 2. Match Investors to Property

```python
from recommendation_engine import InvestorMatcher

matcher = InvestorMatcher()
matcher.load_model('models/investor_property_model.pkl')

# Get top 5 investors for this property
matches = matcher.find_best_investors(
    property_id="PROP-12345",
    top_n=5
)

for investor in matches:
    print(f"{investor['name']}: {investor['match_score']}%")
```

### 3. Send Personalized Emails

```python
from email_automation import EmailCampaign

campaign = EmailCampaign(template="property_introduction")

campaign.add_recipients(matches)
campaign.customize_for_each_investor()
campaign.schedule_send(delay_minutes=0)
campaign.schedule_followup(days=3)

results = campaign.execute()
print(f"Sent: {results['sent']}, Failed: {results['failed']}")
```

### 4. Track in CRM

```python
from crm_integration import FrappeCRM

crm = FrappeCRM()

for match in matches:
    crm.create_opportunity(
        investor_id=match['investor_id'],
        property_id="PROP-12345",
        match_score=match['match_score'],
        stage="Qualified",
        expected_close_date="2025-12-31"
    )
```

## 🔄 n8n Workflows

Pre-built workflows included in `/n8n-workflows/`:

1. **Lead Qualification** - Scores new properties from acquisitions
2. **Investor Matching** - Runs matching algorithm automatically
3. **Email Campaigns** - Sends and tracks outreach sequences
4. **CRM Sync** - Keeps Google Sheets and CRM in sync
5. **Daily Digest** - Summary email of activities

Import these into your n8n instance.

## 🧠 Machine Learning Models

### Training the Recommendation Engine

```bash
# Prepare training data (investors.csv + properties.csv + past_matches.csv)
python recommendation-engine/data_processor.py

# Train model
python recommendation-engine/train_model.py \
    --epochs 50 \
    --learning-rate 0.05 \
    --components 30

# Evaluate
python recommendation-engine/evaluate.py
```

Model learns from:
- Past successful matches
- Investor purchase history
- Property characteristics
- Investor preferences (budget, location, ROI target, risk tolerance)

## 📊 Sample Data

Located in `/data/`:
- `investors.csv` - 100 sample investor profiles
- `properties.csv` - 50 sample properties
- `past_matches.csv` - Historical match data for training

## 🤝 Contributing

This is an open-source project built by combining the best tools from the GitHub community:

**Credits:**
- Property Analysis: Based on [crankstorn/real-estate-analysis](https://github.com/crankstorn/real-estate-analysis)
- Recommendation Engine: Built on [lyst/lightfm](https://github.com/lyst/lightfm)
- Email Automation: Adapted from [msinamsina/pyautomail](https://github.com/msinamsina/pyautomail)
- Claude Integration: Inspired by [martinxu9/claude-investor](https://github.com/martinxu9/claude-investor)

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/prophet-homes-investor-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/prophet-homes-investor-system/discussions)
- **Email**: sklutjack@gmail.com

## 🗺️ Roadmap

- [ ] Mobile app for agents
- [ ] Voice call integration (Twilio)
- [ ] SMS campaigns
- [ ] Advanced analytics dashboard
- [ ] Multi-market support
- [ ] Automated property valuation (AVM)
- [ ] Integration with MLS systems
- [ ] WhatsApp integration

## ⚠️ Disclaimer

This is an educational/operational tool. Always conduct thorough due diligence and consult with legal/financial professionals before making investment decisions.

---

**Built with ❤️ for Prophet Homes investor relations team**

*Last Updated: November 2025*
