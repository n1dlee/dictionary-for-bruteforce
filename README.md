# Password Generator

This simple Python script generates passwords of varying lengths using digits (0-9) and saves them to a file.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Nodik2006/dictionary-for-bruteforce.git
    cd dictionary-for-bruteforce
    ```

2. Run the script:

    ```bash
    python dictionary.py
    ```

3. Find the generated passwords in the `passwords.txt` file.

## How it Works

The script uses the `itertools.product` function to generate all possible combinations of digits for different password lengths. The passwords are then written to a file named `passwords.txt`.

## Dependencies

- Python 3

