# Subdomain Checker

This is a simple Python script that checks the validity of subdomains by sending HTTP requests to them and checking for a valid response. It is designed to be used with a list of subdomains stored in a text file.

## Disclaimer

**Use this tool responsibly and at your own risk.**

- This software is intended solely for educational and informational purposes. The authors and contributors disclaim any liability for misuse, damage, or legal consequences arising from its use.

- You are solely responsible for ensuring that your use of this tool complies with all applicable laws and regulations. Only employ this tool on systems and resources for which you possess explicit permission or legal authorization.

- Please review the [GPL](LICENSE) file for comprehensive details on the software's licensing terms.

- Always exercise ethical and responsible usage of this tool, respecting the privacy and security of others. The authors emphasize that they bear no responsibility for misuse or unauthorized usage of this tool.

- By utilizing this tool, you acknowledge and accept all associated risks and responsibilities.


## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/subdomain_checker.git
   cd subdomain_checker

2. Make sure you have the requests library installed. You can install it using pip:

   ```bash
   pip install requests

3. Create a text file named subdomains.txt and add the list of subdomains you want to check, one per line.

4. Run the script with the base domain as a command-line argument:
   
   ```python
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