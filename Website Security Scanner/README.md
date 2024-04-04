[Software Demo Video](https://youtu.be/inOusO2gABc)

# Summary
This Python script is a foundational tool for learning about web application security scanning. It focuses on identifying a common vulnerability - SQL injection.

Key Functionalities:

* User-friendly Input: Prompts the user for the target website URL and validates it for proper format (http:// or https://).

* HTTP Request Sending: Sends HTTP requests to the target URL using various methods (GET by default) and allows including headers and data for more advanced testing scenarios.

* Basic SQL Injection Detection: Tests for potential SQL injection vulnerabilities by injecting a simple test string and comparing the response to a normal request.

# Important Note:

* This is a simplified educational tool. Real-world web application scanners are far more comprehensive and employ a variety of techniques for in-depth testing.

* This basic SQL injection test is for illustrative purposes only. More sophisticated techniques are required for thorough testing.

* This code provides a starting point for understanding how web application security scanners work. You can build upon this foundation to explore more advanced functionalities and test for additional vulnerabilities.

# Development Environment

This project is built using Python and leverages two external libraries:

* Requests: A popular Python library for making HTTP requests. It simplifies sending various HTTP methods (GET, POST, etc.) and handling responses.

* BeautifulSoup4 (Optional): While not used in this base version, BeautifulSoup4 is a parsing library for HTML and XML data ([invalid URL removed]). It can be useful for future enhancements where you might want to extract specific data from the scanned webpages for further analysis.


# Useful Websites

- [OWASP](https://owasp.org/www-project-top-ten/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Beautifulsoupd4](https://pypi.org/project/beautifulsoup4/)

# Future Work

- Program tests for all 10 OWASP web application security risks
- Link to an extension or application
- Work on result formatting to accomadate for all 10 tests