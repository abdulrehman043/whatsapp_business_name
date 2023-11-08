from bs4 import BeautifulSoup
import requests


def get_whatsapp_business_name(number):
    """
    Get the WhatsApp Business name associated with a given phone number.

    Args:
        number (str): The phone number for which you want to retrieve the WhatsApp Business name.
            The number should be in the format '91XXXXXXXXXX' (e.g., '9198XXXXX1').

    Returns:
        str: The WhatsApp Business name if found, or 'default' if not found.

    Example:
        >>> get_whatsapp_business_name('919891226461')
        'WhatsApp Business Name'  # Example WhatsApp Business name

    Note:
        This function sends a request to the WhatsApp Business API and parses the response
        to extract the business name associated with the provided phone number. If a name
        is found, it is returned; otherwise, 'default' is returned.

    Raises:
        Any exceptions raised during the HTTP request using the `requests` library.

    """
    url = f'https://api.whatsapp.com/send/?phone={number}&text&type=phone_number&app_absent=0'
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')

    name = soup.find('h3', class_='_9vd5 _9scb _9scr')

    if name is not None:
        return name.text
    else:
        return 'default'



