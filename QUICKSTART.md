# ⚡ Prophet Homes Investor System - QUICK START

## Get Running in 5 Minutes

### Step 1: Get Your API Key (2 minutes)

1. Go to https://console.anthropic.com/
2. Sign up (if needed)
3. Create API key
4. Copy it

### Step 2: Setup (2 minutes)

```bash
# Download/clone this repository
cd prophet-homes-investor-system

# Create environment file
cp .env.example .env

# Edit .env and add your API key
nano .env
# Add: ANTHROPIC_API_KEY=sk-ant-your-key-here
# Save and exit (Ctrl+X, Y, Enter)

# Install dependencies
pip install anthropic pandas numpy scikit-learn lightfm
```

### Step 3: Test It! (1 minute)

```bash
# Test property analysis
python claude-analyzer/property_analyzer.py
```

**You should see Claude analyze a sample property!**

---

## What You Just Built

This system can:

✅ **Analyze Properties** - Claude AI reviews properties and calculates ROI  
✅ **Match Investors** - AI finds the best investors for each property  
✅ **Automate Emails** - Send personalized outreach automatically  
✅ **Track Pipeline** - CRM integration with Google Sheets/Frappe

---

## Next Steps

### For Prophet Homes Team

**1. Add Your Data (10 minutes)**

Create `data/investors.csv`:
```csv
investor_id,name,email,budget_min,budget_max,preferred_markets,target_roi
INV001,John Smith,john@example.com,200000,400000,"Dallas,Austin",15
INV002,Jane Doe,jane@example.com,150000,350000,Dallas,18
```

Create `data/properties.csv`:
```csv
property_id,address,purchase_price,arv,rehab_cost,property_type,market
PROP001,123 Main St Dallas,250000,350000,50000,Single Family,Dallas
PROP002,456 Oak Ave Austin,300000,425000,60000,Single Family,Austin
```

**2. Train Matching Model (5 minutes)**

```bash
python recommendation-engine/train_model.py
```

**3. Run Your First Campaign**

```python
from claude_analyzer.property_analyzer import PropertyAnalyzer
from recommendation_engine.matcher import InvestorMatcher
from email_automation.sender import EmailCampaign

# Analyze new property
analyzer = PropertyAnalyzer()
property = {
    'address': '789 Pine St, Dallas, TX',
    'purchase_price': 275000,
    'arv': 375000,
    'rehab_cost': 45000,
    'property_type': 'Single Family',
    'market': 'Dallas'
}
analysis = analyzer.analyze_property(property)

# Find best investors
matcher = InvestorMatcher()
matcher.load_model('models/investor_matcher.pkl')
top_investors = matcher.find_best_investors('PROP001', top_n=5)

# Send emails
campaign = EmailCampaign()
campaign.add_recipients(top_investors)
campaign.customize_for_each_investor(property, {
    'agent_name': 'Jack Sklut',
    'agent_email': 'sklutjack@gmail.com',
    'agent_phone': '509-850-8369'
})
results = campaign.execute()

print(f"✓ Campaign sent to {results['sent']} investors!")
```

---

## Production Setup (Optional)

### Use Docker for Full System

```bash
docker-compose up -d
```

This starts:
- PostgreSQL database
- n8n automation platform
- API server
- Dashboard (optional)

Access:
- API: http://localhost:8000
- n8n: http://localhost:5678 (admin/prophet_admin_123)

### Connect Gmail (Optional)

1. Get Google Cloud credentials
2. Enable Gmail API
3. Download JSON credentials
4. Update `.env`:
   ```bash
   GOOGLE_CREDENTIALS_PATH=/path/to/credentials.json
   GMAIL_USER_EMAIL=your@email.com
   ```

---

## Customization

### Change Email Templates

Edit: `email-automation/templates/property_introduction.html`

### Adjust ROI Calculations

Edit: `.env`
```bash
DEFAULT_VACANCY_RATE=0.05      # Change to 0.08 for 8%
DEFAULT_MAINTENANCE_RATE=0.10  # Change to 0.12 for 12%
```

### Tune Matching Algorithm

Edit: `.env`
```bash
MIN_MATCH_SCORE=60        # Require 60%+ match
TOP_N_RECOMMENDATIONS=5   # Show top 5 investors
LIGHTFM_COMPONENTS=30     # Model complexity (higher = more patterns)
```

---

## Common Use Cases

### Scenario 1: Weekly Property Batch

```bash
# Every Monday morning:
1. Export properties from acquisitions spreadsheet
2. Run: python scripts/batch_analyze.py data/this_week.csv
3. Review matches in Google Sheets
4. Approve and send emails
```

### Scenario 2: Hot Property Alert

```bash
# For urgent/great deals:
1. Analyze property immediately
2. Find top 3 investors (high match scores)
3. Call them first
4. Send follow-up emails to next 10
```

### Scenario 3: Investor Follow-up

```bash
# Re-engage inactive investors:
1. Find investors who haven't responded in 30 days
2. Get their top property matches
3. Send "We miss you" campaign with 3 new opportunities
```

---

## Tips for Prophet Homes

1. **Start Small**: Test with 5-10 investors first
2. **Track Everything**: Use Google Sheets to log all interactions
3. **Call Before Email**: Personal call + follow-up email = best results
4. **Update Model Monthly**: Retrain with new match data
5. **A/B Test**: Try different email templates and track open rates

---

## Troubleshooting

**"No module named 'anthropic'"**
```bash
pip install anthropic
```

**"API key not found"**
- Check `.env` file exists
- Verify `ANTHROPIC_API_KEY=sk-ant-...` is set

**"Model not found"**
```bash
python recommendation-engine/train_model.py
```

---

## Get Help

- **Documentation**: See `docs/SETUP.md` for full guide
- **GitHub Issues**: Report bugs or request features
- **Email**: sklutjack@gmail.com

---

## What's Next?

☐ Upload your investor database  
☐ Train model on historical data  
☐ Set up n8n automation workflows  
☐ Connect Gmail for real email sending  
☐ Integrate with Prophet Homes CRM  
☐ Add Twilio for SMS campaigns  
☐ Build mobile app for agents  

**Ready to revolutionize investor relations at Prophet Homes!** 🚀

---

Built with ❤️ for Prophet Homes  
Last Updated: November 2025
