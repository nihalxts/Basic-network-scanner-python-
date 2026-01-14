📌 Description

This project is a simple network port scanner built using Python.
It scans a given IP address and checks which TCP ports are open.
The project was created to understand IP addresses, ports, services, TCP connections, and basic networking concepts in a safe environment.

🎯 Features

Scan a target IP address for open TCP ports

Detect running services based on open ports

Works safely on localhost (127.0.0.1)

Beginner‑friendly and easy to understand

🛠️ Technologies Used

Python 3

socket library (built‑in Python module)

🚀 How It Works

The program creates a TCP socket

Tries to connect to specific ports on a target IP

If the connection is successful, the port is marked as OPEN

If not, the port is considered CLOSED or FILTERED

▶️ Usage

Clone or download the repository

Open terminal inside the project folder

Run the script:

python network_scanner.py


Enter the target IP address when prompted

Example for testing: 127.0.0.1

📸 Sample Output
=== Basic Network Scanner ===
Enter target IP (example: 127.0.0.1): 127.0.0.1

Scanning 127.0.0.1...

Port 8000 is OPEN

Scan completed.

🔐 Safe Usage Notice

This project is strictly for educational purposes

Only scan:

Your own device

Localhost (127.0.0.1)

Systems you have permission to test

Unauthorized scanning of external systems is illegal

📚 What I Learned

How IP addresses and ports work

Basics of TCP connections

How port scanning is performed

How firewalls affect port visibility

Practical use of Python sockets

🌱 Future Improvements

Port range input

Faster scanning using threading

Save scan results to a file

Basic service name detection

👤 Author

Nihal
BCA Final Year Student
Aspiring Cybersecurity Professional

⭐ Acknowledgment

This project was built as part of self‑learning in networking and cybersecurity fundamentals.
