import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.packet_monitor import PacketMonitor

monitor = PacketMonitor()

connections = monitor.get_connections()

print("\nACTIVE CONNECTIONS\n")

for connection in connections[:10]:

    print(connection)

print("\nFIREWALL ALERTS\n")

alerts = monitor.inspect_connections()

for alert in alerts:
    print(alert)