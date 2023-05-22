# [CTF] Capture! Solution

![bilde](https://github.com/SpaceyLad/CTF_solution-Capture/assets/87969837/f3c4145b-0c48-4a27-a00a-b86f7d972e4d)


This is a Python script that was created for the CTF challenge on [TryHackMe](https://tryhackme.com/room/capture). This script is designed to solve the captcha challenge. 

## About

The script enumerates usernames and passwords from a file and attempts to login to the specified URL. If the login page has a captcha, the script will solve it automatically by importing the math question, converting it to a calculatable format, then returning the answer for the next attempt.

# Important note!
This script will solve the task for you. You should try to solve it yourself before trying this as the meaning of CTF challenges is to challenge your skills and learn new things. Feel free to play around with it and modify it as much as you please. Its all about the fun and games :]

## How to Use

1. Modify the `url` variable in the script to match your challenge IP.
2. Exhaust the login attempts until it requires captcha.
3. Run the script.

## Note

Make sure to have the given username.txt and password.txt from the THM page in the same directory as the script.

## Disclaimer

This script was created for educational purposes and is intended to be used in a controlled, ethical environment. Please do not use this script for unauthorized activities.
