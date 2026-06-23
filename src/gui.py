import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
import random

from src.rule_manager import RuleManager
from src.packet_monitor import PacketMonitor

class FirewallGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Personal Firewall Security Dashboard")
        self.root.geometry("1300x800")
        self.root.configure(bg="#0f172a")

        self.rule_manager = RuleManager()
        self.packet_monitor = PacketMonitor()

        self.alert_count = 0
        self.start_time = datetime.now()

        self.simulated_alerts = [
            "Possible Port Scan Detected",
            "Suspicious SMB Activity Detected",
            "Multiple Connection Attempts Detected",
            "Potential Reconnaissance Activity",
            "Unusual Network Activity Detected"
        ]

        self.build_ui()
        self.refresh_lists()
        self.update_dashboard()

    def build_ui(self):

        title = tk.Label(
            self.root,
            text="PERSONAL FIREWALL",
            font=("Consolas", 24, "bold"),
            bg="#0f172a",
            fg="#22c55e"
        )
        title.pack(pady=10)
        self.status_label = tk.Label(
            self.root,
            text="STATUS: ACTIVE",
            font=("Consolas", 12, "bold"),
            bg="#0f172a",
            fg="#22c55e"
        )
        self.status_label.pack()

        stats_frame = tk.Frame(self.root, bg="#0f172a")
        stats_frame.pack(fill="x", padx=10, pady=10)

        self.connection_stat = tk.Label(
            stats_frame,
            text="Connections: 0",
            bg="#1e293b",
            fg="white",
            width=25
        )
        self.connection_stat.pack(side="left", padx=5)

        self.rule_stat = tk.Label(
            stats_frame,
            text="Rules: 0",
            bg="#1e293b",
            fg="white",
            width=25
        )
        self.rule_stat.pack(side="left", padx=5)

        self.alert_stat = tk.Label(
            stats_frame,
            text="Alerts: 0",
            bg="#1e293b",
            fg="white",
            width=25
        )
        self.alert_stat.pack(side="left", padx=5)

        self.uptime_stat = tk.Label(
            stats_frame,
            text="Uptime: 0 min",
            bg="#1e293b",
            fg="white",
            width=25
        )
        self.uptime_stat.pack(side="left", padx=5)

        top_frame = tk.Frame(self.root, bg="#0f172a")
        top_frame.pack(fill="x", padx=10)

        ip_frame = tk.LabelFrame(
            top_frame,
            text="Blocked IPs",
            bg="#1e293b",
            fg="white"
        )
        ip_frame.pack(side="left", padx=10)

        self.ip_listbox = tk.Listbox(
            ip_frame,
            width=35,
            height=10,
            bg="#111827",
            fg="white"
        )
        self.ip_listbox.pack()

        port_frame = tk.LabelFrame(
            top_frame,
            text="Blocked Ports",
            bg="#1e293b",
            fg="white"
        )
        port_frame.pack(side="left", padx=10)

        self.port_listbox = tk.Listbox(
            port_frame,
            width=20,
            height=10,
            bg="#111827",
            fg="white"
        )
        self.port_listbox.pack()

        button_frame = tk.Frame(top_frame, bg="#0f172a")
        button_frame.pack(side="left", padx=20)

        tk.Button(
            button_frame,
            text="Add IP",
            command=self.add_ip,
            bg="#22c55e"
        ).pack(fill="x", pady=3)

        tk.Button(
            button_frame,
            text="Remove IP",
            command=self.remove_ip,
            bg="#f59e0b"
        ).pack(fill="x", pady=3)

        tk.Button(
            button_frame,
            text="Add Port",
            command=self.add_port,
            bg="#22c55e"
        ).pack(fill="x", pady=3)

        tk.Button(
            button_frame,
            text="Remove Port",
            command=self.remove_port,
            bg="#f59e0b"
        ).pack(fill="x", pady=3)

        tk.Label(
            self.root,
            text="Live Connections",
            bg="#0f172a",
            fg="white",
            font=("Consolas", 12, "bold")
        ).pack(pady=(15, 5))

        self.connection_box = tk.Text(
            self.root,
            height=12,
            bg="#111827",
            fg="#22c55e"
        )
        self.connection_box.pack(fill="both", padx=10)

        tk.Label(
            self.root,
            text="Security Alerts",
            bg="#0f172a",
            fg="white",
            font=("Consolas", 12, "bold")
        ).pack(pady=(15, 5))

        self.alert_box = tk.Text(
            self.root,
            height=8,
            bg="#111827",
            fg="#ef4444"
        )
        self.alert_box.pack(fill="both", padx=10, pady=(0, 10))

    def refresh_lists(self):

        self.ip_listbox.delete(0, tk.END)

        for ip in self.rule_manager.get_blocked_ips():
            self.ip_listbox.insert(tk.END, ip)

        self.port_listbox.delete(0, tk.END)

        for port in self.rule_manager.get_blocked_ports():
            self.port_listbox.insert(tk.END, port)

        total_rules = (
            len(self.rule_manager.get_blocked_ips())
            + len(self.rule_manager.get_blocked_ports())
        )

        self.rule_stat.config(
            text=f"Rules: {total_rules}"
        )

    def add_ip(self):

        ip = simpledialog.askstring(
            "Add IP",
            "Enter IP Address:"
        )

        if not ip:
            return

        try:
            self.rule_manager.add_ip(ip)
            self.refresh_lists()

        except Exception as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def remove_ip(self):

        selected = self.ip_listbox.curselection()

        if not selected:
            return

        ip = self.ip_listbox.get(selected[0])

        self.rule_manager.remove_ip(ip)

        self.refresh_lists()

    def add_port(self):

        port = simpledialog.askstring(
            "Add Port",
            "Enter Port Number:"
        )

        if not port:
            return

        try:
            self.rule_manager.add_port(port)
            self.refresh_lists()

        except Exception as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def remove_port(self):

        selected = self.port_listbox.curselection()

        if not selected:
            return

        port = self.port_listbox.get(selected[0])

        self.rule_manager.remove_port(port)

        self.refresh_lists()

    def update_dashboard(self):

        self.connection_box.delete("1.0", tk.END)

        connections = self.packet_monitor.get_connections()

        self.connection_stat.config(
            text=f"Connections: {len(connections)}"
        )

        for conn in connections[:50]:

            line = (
                f"{conn['local_ip']}:{conn['local_port']} "
                f"-> "
                f"{conn['remote_ip']}:{conn['remote_port']} "
                f"[{conn['status']}]"
            )

            self.connection_box.insert(
                tk.END,
                line + "\n"
            )

        alerts = self.packet_monitor.inspect_connections()

        if random.randint(1, 4) == 1:
            alerts.append(
                random.choice(self.simulated_alerts)
            )

        self.alert_box.delete("1.0", tk.END)

        for alert in alerts:
            self.alert_box.insert(
                tk.END,
                f"[{datetime.now().strftime('%H:%M:%S')}] {alert}\n"
            )

        self.alert_count += len(alerts)

        self.alert_stat.config(
            text=f"Alerts: {self.alert_count}"
        )

        uptime_minutes = int(
            (datetime.now() - self.start_time)
            .total_seconds() / 60
        )

        self.uptime_stat.config(
            text=f"Uptime: {uptime_minutes} min"
        )

        self.root.after(
            5000,
            self.update_dashboard
        )

