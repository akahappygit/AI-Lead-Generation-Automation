# AI Lead Scraper Automation (n8n)

Automation workflow built using n8n.

## Features 
- End-to-end lead scraping automation
- Webhook-based API trigger
- Google Sheets data storage integration
- Twilio Voice Call automation
- Twilio WhatsApp messaging automation
- Cloud deployed on Railway

## Tech Stack
- n8n (workflow automation)
- Docker (containerization)
- Railway (deployment)
- Webhooks / APIs

## How to Use
1. Download the JSON file
2. Import into n8n
3. Add your API credentials (Twilio, Google Sheets, etc.)
4. Run the workflow
   
## Workflow
See [Workflow JSON](https://github.com/akahappygit/n8n-workflow-test/blob/main/workflows/Lead%20Scraper.json)
##  Workflow Overview (images)
![Workflow]([assets/workflow1.png](https://github.com/akahappygit/AI-Lead-Generation-Automation/blob/8c08b303ac9b996a2c0016260878fa11b5848f73/assets/workflow1.png))

## 📞 Twilio Integration (image)
![Twilio]([assets/twilioconfiguration.png](https://github.com/akahappygit/AI-Lead-Generation-Automation/blob/8c08b303ac9b996a2c0016260878fa11b5848f73/assets/twilio%20configuration.png))

## 📊 Output (Google Sheets- image)
![Sheets]((https://github.com/akahappygit/AI-Lead-Generation-Automation/blob/7311ca7263d27c66c57d78523d73361243e5c756/assets/google%20sheet.png)))

##  Automation Flow

This workflow performs end-to-end lead processing:

1. Receives input via Webhook API
2. Scrapes / processes lead data
3. Stores leads in Google Sheets
4. Triggers Twilio automation:

- Automated voice calling (Twilio)
- WhatsApp messaging (Twilio API)

## Integrations Used

- Twilio (Voice Call Automation)
- Twilio WhatsApp API
- Google Sheets (Data Storage)
- Webhooks (API trigger)
  
##  Workflow Overview

Webhook → Data Processing → Google Sheets → Twilio Call → WhatsApp Message → Response

## Note

Live Application: 
https://n8n-production-3c1c.up.railway.app  

Credentials (Twilio, Google Sheets, etc.) are excluded for security reasons.  
Please configure your own API keys before running the workflow.

## Voice Agent 
Eleven Labs Voice agent Link : https://elevenlabs.io/app/talk-to?agent_id=agent_3501kkyxstrrfr38cpzk63vp9wcz&branch_id=agtbrch_6801kkyxsvh1fs88ataxvw0yec00
This AI coversational voice agent used for a professional and efficient Lead Qualification that is mainly talk to users for general FAQS regarding the leads generated via n8n to convert if scaleable will connect twilio to eleven labs for efficient automation tool 


##  Live Demo API 

**Endpoint(Demo API):**  
https://n8n-production-3c1c.up.railway.app/webhook/demo  

**Method:**  
GET  

**Sample Response:**

``` json
{
  "status": "success",
  "project": "AI Lead Scraper",
  "message": "Workflow is live"
}



