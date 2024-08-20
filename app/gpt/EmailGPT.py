import requests
import json
from groq import Groq

import config




def fetch_info_from_link(url):
    """
    Fetch information from a given URL. This function can be customized to extract specific information.

    Args:
        url (str): The URL containing the information about the individual.

    Returns:t
        str: The extracted information.
    """
    response = requests.get(url)
    if response.status_code == 200:
        # Here you can parse the HTML and extract the needed information using BeautifulSoup or any other method.
        return response.text  # Replace with actual parsing and extraction logic
    else:
        return None


def generate_custom_email(email_text, recipient_name, recipient_email, extracted_info, tone):
    """
    Tailor the email to the recipient using the provided information and tone.

    Args:
        email_text (str): The original email text.
        recipient_name (str): The name of the email recipient.
        recipient_email (str): The email address of the recipient.
        extracted_info (str): Information extracted from the provided link.
        tone (str): The tone to be applied to the email (e.g., "professional", "friendly", "formal").

    Returns:
        str: The customized email text.
    """
    prompt = f"""
    The following is an email template that needs to be customized for {recipient_name} ({recipient_email}). 
    Here's some information about them: {extracted_info}. 
    Apply a {tone} tone to the email.

    Original Email:
    {email_text}

    Tailored Email:
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )

    tailored_email = response.choices[0].text.strip()
    return tailored_email


if __name__ == "__main__":
    # Input email text
    email_text = "Dear [Recipient], I would like to discuss an opportunity that I believe could be beneficial for both of us. Please let me know your availability."

    # Input recipient details
    recipient_name = "John Doe"
    recipient_email = "john.doe@example.com"
    info_url = "https://www.example.com/john-doe-profile"

    # Fetch the information from the provided link
    extracted_info = fetch_info_from_link(info_url)

    if extracted_info:
        # Define the desired tone
        tone = "friendly"

        # Generate the tailored email
        customized_email = generate_custom_email(email_text, recipient_name, recipient_email, extracted_info, tone)

        # Print the tailored email
        print("Customized Email:\n", customized_email)
    else:
        print("Failed to retrieve information from the provided URL.")