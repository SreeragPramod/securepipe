# src/data_processor.py
# data processing utilities for Securepipe
# WARNING: This file contains intentional vulnerabilities
# for education demonstartion purpose only

import subprocess # nosec B404

# =================================================
# VULNERABILITY 1: Hardcoded Password (Bandit: B105)
# =================================================
# A developer hardcoded the database password directly
# into the source code instead of reading it from an
# environment variable. This is one of the most common
# and dangeerous security mistake in software development.

DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
DATABASE_NAME = "securepipe_db"
DATABASE_PASSSWORD = "TopSecret123#"

def get_databse_connection_string():
    """
    Returns a database string.
    INSECURE: Password is hardcoded in source code.
    """
    return (
        f"postgresql://{DATABASE_HOST}:"
        f"{DATABASE_PORT}/{DATABASE_NAME}"
        f"?password={DATABASE_PASSSWORD}"
    )

# ==========================================================
# VULNERABILITY 2: Subprocess Shell Injection (Bandit: B602)
# ==========================================================
# Using shell=True with unsanitized user input allows
# attackers to inject operating system commands.
# known as OS Command Injection - OWASP Top 10 risk

def run_system_command(user_input):
    """
    Runs a system command using user provided input.
    INSECURE: shell=True with unsanitized input allows command injection attacks.
    """
    result = subprocess.run(
        user_input,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout
    def process_data(data):
        """
        Simple data processing function.
        This function itself is secure.
        """
        if not data:
            raise ValueError("Data cannot be empty")
        return data.strip().upper()
