
# API Fuzzer Tool

A simple Python tool for fuzzing API endpoints using a wordlist. This tool helps you test multiple API endpoints by sending HTTP GET requests derived from a base API URL and a wordlist file.

## Features

- Makes HTTP GET requests to API endpoints constructed from a base URL and a wordlist.
- Handles connection timeouts and request exceptions.
- Simple to use and customizable.

## Installation & Prerequisites

This tool requires Python 3.x and the `requests` library.

1. Clone the repository:
    ```bash
    git clone https://github.com/neerajkataria01/fuzzify.git
    cd fuzzify
    ```

2. Install the required dependencies using `pip`:
    ```bash
    pip install requests
    ```

## Usage

1. Run the script:
    ```bash
    python fuzzer.py
    ```

2. You will be prompted to enter:
   - The base API URL (e.g., `https://api.example.com`).
   - The path to your wordlist file (a text file containing endpoints to test, one per line).

3. The script will then test the endpoints derived from the base URL and wordlist and output the status codes, response content, and any warnings.
