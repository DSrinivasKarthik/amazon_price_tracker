# Amazon Price Tracker
---
The Amazon Price Tracker is a Python application that allows users to track the price of a specific product on Amazon and receive email notifications when the price falls within a predefined budget.

## Features

- User-friendly interface for login and registration.
- Scrape product details from Amazon URLs.
- Track and store historical price data in CSV format.
- Display a graphical representation of price changes over time.

## Installation

1. Clone this GitHub repository to your local machine.

   ```bash
   git clone https://github.com/DSrinivasKarthik/amazon_price_tracker.git

2. Navigate to the project directory.

   ```bash
   cd amazon-price-tracker

3. Install the required Python libraries by running:

   ```bash
    pip install -r requirements.txt

## Usage

1. Run the reg_login.py script to start the application.

   ```bash
    python reg_login.py

2. The application will present options for user login and registration.

3. After login or registration, the user can provide an Amazon URL for a product they want to track and set a budget.

4. The application will scrape the product details and store historical price data in a CSV file.

5. Users can view the graphical representation of price changes over time using the graph_work.py script.

## Files

- reg_login.py: Implements user registration and login functionality using a Tkinter-based GUI. Stores user credentials and manages authentication.

- mainone.py: Scrape product details from Amazon URLs, track historical price data, and send email notifications when the price is within the budget.

- graph_work.py: Generate and display a graphical representation of price changes over time using the Matplotlib library.

## Notes

- This project is for educational purposes only and should be used responsibly.

- Ensure that you have enabled "Less Secure Apps" in your Gmail account settings to use the email notification feature.





