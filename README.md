# Typing Focus & Stress Analyzer

This project measures typing behavior (timing between keys, backspace usage, pauses) to estimate a rough “Focus Score” from 0–100. It records keystrokes locally into a CSV file and then analyzes it. Nothing is uploaded or sent anywhere.


## How to Install and 

```bash
# 1. Download the project
git clone https://github.com/nahumfikre/typing-focus.git
cd typing-focus

# 2. Create and activate a virtual environment using venv
python3 -m venv env
# macOS / Linux:
source env/bin/activate
# Windows:
env\Scripts\activate

# 3. Install required libraries
pip install -r requirements.txt

# 4. (macOS ONLY) → Allow keyboard tracking
# Go to: System Settings → Privacy & Security → Input Monitoring
# Enable "Terminal" or "VS Code", then restart Terminal

# 5. Run the typing recorder (it logs keystrokes to /data/)
python typing_logger.py
# When you're done typing, press CTRL + C to stop
# It saves a file like: data/session_2025-11-02_153312.csv

# 6. Analyze that typing session and get a Focus Score
python analyze_session.py data/session_2025-11-02_153312.csv
