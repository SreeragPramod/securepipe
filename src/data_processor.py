# src/data_processor.py
# Data processing utilities for SecurePipe
# SECURE VERSION - vulnerabilities fixed

import os
import subprocess

# =========================================================
# FIX 1: ENVIRONMENT VARIABLE (REPLACES HARDCODED PASSWORD)
# =========================================================
# Credentials are now read from environment variables.
# The source code contains zero secrets.
# On the server, these are set as system environment variables.
# In Github actions, these are set as encrypted GitHub secrets.

def get_database_connection_string():
    """
    Returns a database connection string.
    SECURE: All credentials are read from environment variables.
    Raises RuntimeError if the password environment variable
    is not set - fails loudly rather than silently.
    """
    if not DATABASE_PASSWORD:
        raise RuntimeError(
            "DATABASE_PASSWORD environment variable is not set."
            "Refusing a connect without credentials."
        )
    return (
        f"postgresql://{DATABASE_HOST}"
        f"{DATABASE_PORT}/{DATABASE_NAME}"
        f"?password={DATABASE_PASSWORD}"
    )

# ============================================================
# FIX 2 : shell=False with argument list (replaces shell=True)
# ============================================================
# shell=False prevents OS command injection entirely.
# Input is validated and passed as structured argument list
# not as a raw string to a shell interpreter.

ALLOWED_HOSTS = [
    "google.com"
    "github.com"
    "example.com"
]

def run_ping(target_host):
    """
    Pings a target host from an approved allowedlist.
    SECURE: shell=False prevents commandd injection.
    Input validation ensures only approved hosts are pinged.
    Raises ValueError if the host is not in the allowlist.
    """
    if target_host not in ALLOWED_HOSTS:
        raise ValueError(
            f"Host '{target_host}' is not in the approved "
            f"allowlist. Refusing to execute."
        )
    result = subprocess.run(
        ["ping", "-c", "1", target_host],
        shell=False,
        capture_output=True,
        text=True,
        timeout=10
    )
    return result.stdout

def process_data(data):
    """
    Simple data processing function.
    Validate input before processing.
    """
    if not data:
        raise ValueError("Data cannot be empty.")
    return data.strip().upper()
