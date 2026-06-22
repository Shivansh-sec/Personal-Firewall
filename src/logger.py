"""
logger.py
----------

Centralized logging module for the Personal Firewall project.

Features:
- Logs to file and console
- INFO, WARNING, ERROR support
- Automatic log directory creation
- Reusable across all project modules
"""

import logging
import os


class FirewallLogger:
    """Centralized logger for the Personal Firewall project."""

    def __init__(self):
        self.log_directory = "logs"
        self.log_file = os.path.join(self.log_directory, "firewall.log")

        # Create logs directory if it doesn't exist
        os.makedirs(self.log_directory, exist_ok=True)

        # Create logger
        self.logger = logging.getLogger("PersonalFirewall")

        # Prevent duplicate handlers if imported multiple times
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            # File handler
            file_handler = logging.FileHandler(
                self.log_file,
                encoding="utf-8"
            )
            file_handler.setFormatter(formatter)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def info(self, message: str):
        """Log informational message."""
        self.logger.info(message)

    def warning(self, message: str):
        """Log warning message."""
        self.logger.warning(message)

    def error(self, message: str):
        """Log error message."""
        self.logger.error(message)

    def separator(self):
        """Add visual separator in logs."""
        self.logger.info("=" * 60)


# Singleton instance used throughout the application
firewall_logger = FirewallLogger()