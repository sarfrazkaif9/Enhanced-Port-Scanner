# 🔐 Enhanced Port Scanner (Version 2)

An improved **Python-based TCP port scanner** designed for learning **network security**, **VAPT basics**, and **cybersecurity interviews**.
This enhanced version supports **multithreaded scanning**, **service detection**, **Nmap-style output**, and **optional result saving**.

---

## 🚀 Features (Version 2)

- TCP Connect Port Scanning
- Multithreaded scanning for faster results
- Nmap-style output formatting
- Common service name detection (SSH, HTTP, HTTPS, etc.)
- Thread-safe scanning logic
- Optional saving of scan results to file
- Works on Windows, Linux, macOS
- No external dependencies

---

## 🛠️ Technologies Used

- Python 3.x
- socket (standard library)
- concurrent.futures (ThreadPoolExecutor)
- threading (Lock)

---

## 📁 Project Structure

.
├── enhanced_port_scanner_v2.py
├── scan_results.txt   (generated after scan)
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Verify Python Installation

```bash
python --version
```

If Python is not installed, download it from:
https://www.python.org/downloads/

---

### 2️⃣ Setup Project

Place the following files in the same directory:

- `enhanced_port_scanner_v2.py`
- `README.md`

---

## ▶️ Usage

Run the scanner:

```bash
 python advanced_port_scanner.py
```

### Example Input

Target IP / Hostname: `127.0.0.1`  
Start Port: `1`  
End Port: `1000`  

---

### Example Output

```
Starting scan on 127.0.0.1
----------------------------------------

PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   open   http
443/tcp  open   https

Scan completed.
```

---

## 💾 Saving Results

After scanning, you will be prompted:

```
Save results to file? (y/n)
```

If `y` is selected, results are saved to:

```
scan_results.txt
```

If no open ports are found, the tool will display:

```
No open ports found.
```

---

## 🔎 How It Works

1. Creates TCP sockets using `AF_INET` and `SOCK_STREAM`
2. Attempts TCP connections using `connect_ex()`
3. Open ports are identified when connections succeed
4. Uses `ThreadPoolExecutor` for parallel scanning
5. Uses thread locks to safely store results
6. Displays output in Nmap-style tabular format

---

## 🧠 Scan Type

- TCP Connect Scan
- Full TCP handshake
- Accurate but not stealthy
- Suitable for labs and authorized testing

---

## ⚠️ Legal Disclaimer

This tool is intended for **educational and authorized security testing only**.

You must have explicit permission before scanning:
- Servers
- Networks
- Systems you do not own

Unauthorized port scanning may be illegal.

---

## 🔮 Future Enhancements

- Filtered vs closed port detection
- Banner grabbing and version detection
- CIDR / IP range scanning
- Nmap-like CLI arguments (`-p`, `-T4`)
- CSV / JSON report export

---

## 👨‍💻 Author

**Vishnu**  
Cybersecurity Graduate (MCA, 2025)  
Interests: Network Security, VAPT, SOC Operations

---

⭐ If you find this project useful, give it a star on GitHub!
