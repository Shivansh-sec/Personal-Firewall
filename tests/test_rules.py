import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.rule_manager import RuleManager

rules = RuleManager()

rules.add_ip("192.168.1.100")
rules.add_port(8080)

print("Blocked IPs:")
print(rules.get_blocked_ips())

print("\nBlocked Ports:")
print(rules.get_blocked_ports())