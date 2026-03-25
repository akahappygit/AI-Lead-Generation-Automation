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
n8n (workflow automation)
Docker (containerization)
Railway (deployment)
Webhooks / APIs

## Workflow
See [Workflow JSON](./workflows/Lead%20Scraper.json)

##  Automation Flow

This workflow performs end-to-end lead processing:

1. Receives input via Webhook API
2. Scrapes / processes lead data
3. Stores leads in Google Sheets
4. Triggers Twilio automation:

Automated voice calling (Twilio)
WhatsApp messaging (Twilio API)

## Integrations Used

- Twilio (Voice Call Automation)
- Twilio WhatsApp API
- Google Sheets (Data Storage)
-  Webhooks (API trigger)
  
##  Workflow Overview

Webhook → Data Processing → Google Sheets → Twilio Call → WhatsApp Message → Response


##  Live Demo API 

Endpoint
https://n8n-production-3c1c.up.railway.app/webhook/demo ( demo production link )
Method
GET
Sample Response ( json )
{
  "status": "success",
  "project": "AI Lead scrapper",
  "message": "Workflow is live"
}

##  Note
Live Production link : https://n8n-production-3c1c.up.railway.app
Credentials are not included for security reasons.
Please configure your own API keys before running.
