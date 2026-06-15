"""
AI Autism Support Toolkit
Main entry point for Streamlit Cloud deployment
"""

import subprocess
import sys

# Run main_app1.py
if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "streamlit", "run", "main_app1.py"])
