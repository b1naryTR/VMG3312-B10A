# VMG3312-B10A Unauthenticated RCE Vulnerability

## Overview:
This README file describes the steps to reproduce an Unauthenticated Remote Code Execution (RCE) vulnerability in the Zyxel VMG3312-B10A router. The vulnerability allows an attacker to execute arbitrary code on the target system without any authentication.

## Description:
The vulnerability is caused by a lack of input validation in the "diagAddr" parameter of the "diagnostic-general.cgi" script. An attacker can exploit this vulnerability by sending a specially crafted HTTP request to the router's web server. The attacker can execute arbitrary code with the privileges of the web server process.

## Impact:
An attacker can exploit this vulnerability to execute arbitrary code on the target system. This can result in the compromise of sensitive data, unauthorized access to the router, and possible lateral movement within the network.

## Prerequisites:
To exploit this vulnerability, an attacker needs to have access to the router's web interface. The vulnerable device is Zyxel VMG3312-B10A.

Steps to reproduce:

Install Python 3 and the "requests" library.
Copy the POC code provided above to a Python file.
Replace the "ip", "username", and "password" values in the code with the appropriate values for the target router.
Run the Python code.
Enter the command to execute on the target system when prompted by the code.
The command will be executed on the target system.

## Mitigation:
It is recommended to update the firmware to the latest version as soon as possible.

Alternatively, administrators can block external access to the router's web interface or implement access controls to limit the exposure of the vulnerability.

## Disclaimer:
This vulnerability was discovered by Ibrahim Tekin and reported to Zyxel. The information provided in this README file is for educational purposes only. The author is not responsible for any misuse or damage caused by the exploitation of this vulnerability. It is the responsibility of the user to ensure that any actions taken comply with all applicable laws and regulations.
