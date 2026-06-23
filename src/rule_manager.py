"""
rule_manager.py
---------------

Handles firewall rule management.

Features:
- Add blocked IP addresses
- Remove blocked IP addresses
- Add blocked ports
- Remove blocked ports
- Validate IP addresses
- Save rules persistently
- Load rules from configuration file
"""

import json
import ipaddress
from pathlib import Path


class RuleManager:

    def __init__(self):
        self.project_root = Path(__file__).resolve().parent.parent

        self.rules_file = (
            self.project_root /
            "config" /
            "rules.json"
        )

        self._ensure_rules_file()

    def _ensure_rules_file(self):
        """
        Create rules file if it doesn't exist.
        """

        if not self.rules_file.exists():

            default_rules = {
                "blocked_ips": [],
                "blocked_ports": [21, 23, 445]
            }

            with open(self.rules_file, "w") as file:
                json.dump(default_rules, file, indent=4)

    def load_rules(self):
        """
        Load firewall rules.
        """

        with open(self.rules_file, "r") as file:
            return json.load(file)

    def save_rules(self, rules):
        """
        Save firewall rules.
        """

        with open(self.rules_file, "w") as file:
            json.dump(rules, file, indent=4)

    def add_ip(self, ip_address):
        """
        Add blocked IP.
        """

        try:
            ipaddress.ip_address(ip_address)

        except ValueError:
            raise ValueError(
                f"Invalid IP address: {ip_address}"
            )

        rules = self.load_rules()

        if ip_address not in rules["blocked_ips"]:

            rules["blocked_ips"].append(ip_address)

            self.save_rules(rules)

            return True

        return False

    def remove_ip(self, ip_address):
        """
        Remove blocked IP.
        """

        rules = self.load_rules()

        if ip_address in rules["blocked_ips"]:

            rules["blocked_ips"].remove(ip_address)

            self.save_rules(rules)

            return True

        return False

    def add_port(self, port):
        """
        Add blocked port.
        """

        port = int(port)

        if port < 1 or port > 65535:
            raise ValueError(
                "Port must be between 1 and 65535"
            )

        rules = self.load_rules()

        if port not in rules["blocked_ports"]:

            rules["blocked_ports"].append(port)

            self.save_rules(rules)

            return True

        return False

    def remove_port(self, port):
        """
        Remove blocked port.
        """

        port = int(port)

        rules = self.load_rules()

        if port in rules["blocked_ports"]:

            rules["blocked_ports"].remove(port)

            self.save_rules(rules)

            return True

        return False

    def get_blocked_ips(self):
        """
        Return blocked IP list.
        """

        return self.load_rules()["blocked_ips"]

    def get_blocked_ports(self):
        """
        Return blocked port list.
        """

        return self.load_rules()["blocked_ports"]