# Subdomain Checker

This is a simple Python script that checks the validity of subdomains by sending HTTP requests to them and checking for a valid response. It is designed to be used with a list of subdomains stored in a text file.

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/subdomain_checker.git
   cd subdomain_checker

2. Make sure you have the requests library installed. You can install it using pip:

   pip install requests

3. Create a text file named subdomains.txt and add the list of subdomains you want to check, one per line.

4. Run the script with the base domain as a command-line argument:
    
   python script.py example.com

   Replace example.com with the base domain you want to check against.

   The script will check each subdomain by sending an HTTP GET request and print the valid domains to the console.

## License

This project is licensed under the MIT License. See the [GPL](LICENSE) file for details.

## Contribution

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or create a pull request.

## Credits

This script was cloned and modified by Onurcan Genc.

## Contact

If you have any questions or need further assistance, feel free to contact me at onurcangencbilkent@gmail.com.