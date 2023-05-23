# Virus Scanner

This project is a command-line virus scanner implemented in Python. It scans files within a specified directory and its subdirectories for known virus signatures and performs basic heuristics analysis to identify potentially malicious code.
Features

   Scans files for known virus signatures: The scanner compares the content of each file with a predefined list of virus signatures. If a signature is found in a file, it is flagged as potentially infected.

   Heuristics analysis: In addition to signature-based scanning, the scanner performs a basic heuristics analysis. It checks if the file contains the string "eval(" using string decoding and identifies it as potentially malicious code.

   Recursive directory scanning: The scanner traverses through the specified directory and its subdirectories to scan all files present within them.

## Usage

    Run the script: Execute the script using a Python interpreter.

    Provide directory path: Enter the path of the directory you want to scan when prompted by the script.

    Scanning process: The scanner will scan each file within the specified directory and its subdirectories. If a file is detected as infected or contains potentially malicious code, the scanner will display a corresponding message indicating the issue.

## Disclaimer

This virus scanner is intended for educational purposes and basic virus detection. It utilizes a predefined list of virus signatures and performs simple heuristics analysis. It may not detect all types of malware or provide advanced protection. For comprehensive virus protection, it is recommended to use professional antivirus software.

Note: The predefined list of virus signatures can be updated with additional signatures for better detection capabilities.
## Requirements

    Python 3.x
    Operating System: Windows, Linux, macOS

## Contributions

Contributions to this project are welcome. If you have any suggestions, improvements, or bug fixes, please feel free to submit a pull request.
License

This project is licensed under the MIT License.

Please note that this project does not guarantee complete virus detection and it is advisable to exercise caution and use reliable antivirus software for comprehensive protection
