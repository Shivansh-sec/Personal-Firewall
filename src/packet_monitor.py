"""
packet_monitor.py
-----------------

Monitors active network connections and
checks them against firewall rules.
"""

import psutil

from src.rule_manager import RuleManager
from src.logger import firewall_logger


class PacketMonitor:

    def __init__(self):

        self.rule_manager = RuleManager()

    def get_connections(self):

        connections = []

        for conn in psutil.net_connections(kind="inet"):

            try:

                local_ip = (
                    conn.laddr.ip
                    if conn.laddr else "N/A"
                )

                local_port = (
                    conn.laddr.port
                    if conn.laddr else "N/A"
                )

                remote_ip = (
                    conn.raddr.ip
                    if conn.raddr else "N/A"
                )

                remote_port = (
                    conn.raddr.port
                    if conn.raddr else "N/A"
                )

                status = conn.status

                connection = {
                    "local_ip": local_ip,
                    "local_port": local_port,
                    "remote_ip": remote_ip,
                    "remote_port": remote_port,
                    "status": status
                }

                connections.append(connection)

            except Exception:
                continue

        return connections

    def inspect_connections(self):

        blocked_ips = (
            self.rule_manager.get_blocked_ips()
        )

        blocked_ports = (
            self.rule_manager.get_blocked_ports()
        )

        findings = []

        for conn in self.get_connections():

            remote_ip = conn["remote_ip"]
            remote_port = conn["remote_port"]

            if remote_ip in blocked_ips:

                alert = (
                    f"BLOCKED IP DETECTED -> "
                    f"{remote_ip}"
                )

                firewall_logger.warning(alert)

                findings.append(alert)

            elif remote_port in blocked_ports:

                alert = (
                    f"BLOCKED PORT DETECTED -> "
                    f"{remote_port}"
                )

                firewall_logger.warning(alert)

                findings.append(alert)

        return findings