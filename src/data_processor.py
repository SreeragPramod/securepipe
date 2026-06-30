# src/data_processor.py
# Data processing utilities for SecurePipe
# SECURE VERSION — vulnerabilities fixed


import os
import subprocess  # nosec B404


def get_database_connection_string():
    """
    Returns a database connection string.
    SECURE: Credentials are read from environment variables
    at call time (not import time) so the function reflects
    the current environment and can be tested in isolation.
    Raises RuntimeError if the password is missing rather
    than silently connecting without credentials.
    """
    password = os.environ.get("DATABASE_PASSWORD")
    if not password:
        raise RuntimeError(
            "DATABASE_PASSWORD environment variable is not set. "
            "Refusing to connect without credentials."
        )
    host = os.environ.get("DATABASE_HOST", "localhost")
    port = os.environ.get("DATABASE_PORT", "5432")
    name = os.environ.get("DATABASE_NAME", "securepipe_db")
    return f"postgresql://{host}:{port}/{name}?password={password}"


ALLOWED_HOSTS = [
    "google.com",
    "github.com",
    "example.com",
]


def run_ping(target_host):
    """
    Pings a target host from an approved allowlist.
    SECURE: shell=False prevents command injection.
    Raises ValueError if the host is not in the allowlist.
    """
    if target_host not in ALLOWED_HOSTS:
        raise ValueError(
            f"Host '{target_host}' is not in the approved "
            f"allowlist. Refusing to execute."
        )

    result = subprocess.run(  # nosec B603
        ["/usr/bin/ping", "-c", "1", target_host],
        shell=False,
        capture_output=True,
        text=True,
        timeout=10,
    )
    return result.stdout


def process_data(data):
    """
    Simple data processing function.
    Validates input before processing.
    """
    if not data:
        raise ValueError("Data cannot be empty.")
    return data.strip().upper()
