# WhatsApp Business Name API

## Overview

The WhatsApp Business Name API is a Python-based web application that extracts and provides the business name associated with a WhatsApp number. Built using Flask, this API offers a straightforward and efficient way to obtain business information from WhatsApp contacts.

## Features

- Extracts the business name linked to a WhatsApp number.
- Utilizes Flask for a lightweight and scalable web framework.
- Easy-to-use API with a single endpoint for retrieving business names.
- Can be integrated into various applications and services.

## Getting Started

These instructions will help you set up the WhatsApp Business Name API on your local machine for development and testing purposes. To deploy it in a production environment, refer to the deployment section.

### Prerequisites

- Python (3.6 or higher)
- Flask
- BeautifulSoup (for web scraping)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/whatsapp-business-api.git
   cd whatsapp-business-api
2. Install Required dependencies
   ```bash
   pip install -r requirements.txt
3. Run the Flask application:
   ```bash
   flask run
4. Access API
   http://localhost:5000/whatsapp_business
In post request give :
```
{
    "number": "919891226461"
}



