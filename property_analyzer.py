def __init__(self, api_key: Optional[str] = None):
    from dotenv import load_dotenv
    load_dotenv()
    self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
    self.client = Anthropic(api_key=self.api_key)
    self.model = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514")"""
Claude AI Property Analyzer
Analyzes real estate properties using Anthropic's Claude API
"""

import os
from typing import Dict, List, Optional
from anthropic import Anthropic
import json


class PropertyAnalyzer:
    """
    Uses Claude AI to analyze real estate investment properties
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=self.api_key)
        self.model = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514")
        
    def analyze_property(self, property_data: Dict) -> Dict:
        """
        Comprehensive property analysis using Claude
        
        Args:
            property_data: Dict containing property details
            
        Returns:
            Dict with analysis results
        """
        prompt = self._build_analysis_prompt(property_data)
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=4000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Parse Claude's response
        analysis_text = response.content[0].text
        
        return {
            "raw_analysis": analysis_text,
            "property_id": property_data.get("property_id"),
            "address": property_data.get("address"),
            "model_used": self.model
        }
    
    def _build_analysis_prompt(self, property_data: Dict) -> str:
        """Build detailed prompt for Claude"""
        
        prompt = f"""You are a real estate investment analyst for Prophet Homes, a Texas-based 
real estate investment firm focused on fix-and-flip and fix-and-rent properties.

Analyze the following property and provide a comprehensive investment analysis:

PROPERTY DETAILS:
- Address: {property_data.get('address', 'Not provided')}
- Purchase Price: ${property_data.get('purchase_price', 0):,.2f}
- After Repair Value (ARV): ${property_data.get('arv', 0):,.2f}
- Estimated Rehab Cost: ${property_data.get('rehab_cost', 0):,.2f}
- Property Type: {property_data.get('property_type', 'Single Family')}
- Bedrooms: {property_data.get('bedrooms', 'Unknown')}
- Bathrooms: {property_data.get('bathrooms', 'Unknown')}
- Square Footage: {property_data.get('sqft', 'Unknown')}
- Year Built: {property_data.get('year_built', 'Unknown')}
- Condition: {property_data.get('condition', 'Unknown')}
- Neighborhood: {property_data.get('neighborhood', 'Unknown')}

MARKET DATA (if available):
- Market Rent: ${property_data.get('market_rent', 0):,.2f}/month
- Days on Market: {property_data.get('days_on_market', 'Unknown')}
- Comparable Sales: {property_data.get('comps', 'Not provided')}

Please provide a structured analysis with the following sections:

1. EXECUTIVE SUMMARY
   - Overall investment recommendation (Strong Buy / Buy / Hold / Pass)
   - Key strengths and red flags
   - Target investor profile

2. FINANCIAL ANALYSIS
   - Estimated ROI for fix-and-flip
   - Estimated cash-on-cash return for fix-and-rent
   - All-in cost breakdown
   - Potential profit scenarios (conservative, base, optimistic)

3. MARKET ANALYSIS
   - Neighborhood assessment
   - Market trends
   - Comparable property analysis
   - Rental demand (if applicable)

4. RISK ASSESSMENT
   - Construction/rehab risks
   - Market timing risks
   - Exit strategy considerations
   - Holding cost exposure

5. INVESTOR MATCHING CRITERIA
   Based on this property, what type of investor would this be BEST for?
   - Experience level needed
   - Capital requirements
   - Risk tolerance
   - Preferred investment strategy (flip vs rent)
   - Geographic preferences

6. RECOMMENDATIONS
   - Suggested purchase price (if different from asking)
   - Timeline to completion
   - Exit strategy recommendations
   - Specific action items

Format your response in clear sections with specific numbers and actionable insights.
"""
        
        return prompt
    
    def batch_analyze_properties(self, properties: List[Dict]) -> List[Dict]:
        """Analyze multiple properties"""
        results = []
        
        for prop in properties:
            try:
                analysis = self.analyze_property(prop)
                results.append(analysis)
            except Exception as e:
                results.append({
                    "property_id": prop.get("property_id"),
                    "error": str(e)
                })
        
        return results
    
    def extract_investor_criteria(self, analysis: Dict) -> Dict:
        """
        Extract investor matching criteria from Claude's analysis
        Uses a second Claude call to structure the data
        """
        
        prompt = f"""Based on this property analysis, extract the ideal investor criteria 
in JSON format:

{analysis['raw_analysis']}

Return ONLY a JSON object with this structure:
{{
    "experience_level": "beginner|intermediate|advanced",
    "min_capital": <number>,
    "risk_tolerance": "low|medium|high",
    "strategy_preference": ["fix-and-flip", "fix-and-rent", "BRRRR"],
    "target_roi_flip": <number>,
    "target_cash_on_cash_rent": <number>,
    "markets": ["Dallas", "Austin", etc],
    "property_types": ["Single Family", "Duplex", etc]
}}

JSON only, no explanations:"""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        try:
            criteria = json.loads(response.content[0].text)
            return criteria
        except:
            return {"error": "Could not parse criteria"}


# Example usage
if __name__ == "__main__":
    
    # Sample property data
    sample_property = {
        "property_id": "PROP-001",
        "address": "123 Main St, Dallas, TX 75201",
        "purchase_price": 250000,
        "arv": 350000,
        "rehab_cost": 50000,
        "property_type": "Single Family",
        "bedrooms": 3,
        "bathrooms": 2,
        "sqft": 1800,
        "year_built": 1975,
        "condition": "Needs Renovation",
        "market_rent": 2200,
        "neighborhood": "Oak Cliff"
    }
    
    analyzer = PropertyAnalyzer()
    
    print("Analyzing property with Claude AI...")
    analysis = analyzer.analyze_property(sample_property)
    
    print("\n" + "="*80)
    print(analysis['raw_analysis'])
    print("="*80)
    
    print("\nExtracting investor criteria...")
    criteria = analyzer.extract_investor_criteria(analysis)
    print(json.dumps(criteria, indent=2))
