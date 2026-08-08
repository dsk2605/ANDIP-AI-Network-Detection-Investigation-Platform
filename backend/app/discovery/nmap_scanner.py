import shutil
import subprocess
from typing import Any, Dict, List

from app.discovery.base_scanner import BaseScanner


class NmapScanner(BaseScanner):
    """Runs Nmap scans and returns raw XML output."""

    def __init__(self):
        self.nmap_path = shutil.which("nmap")

        if not self.nmap_path:
            raise RuntimeError(
                "Nmap executable not found. Please ensure Nmap is installed and added to PATH."
            )

    def scan(self, target: str) -> List[Dict[str, Any]]:
        command = [
            self.nmap_path,
            "-sS",
            "-sV",
            "-O",
            "-T4",
            "-oX",
            "-",
            target,
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
            )

            return [
                {
                    "scanner": "nmap",
                    "target": target,
                    "xml": result.stdout,
                }
            ]

        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"Nmap scan failed:\n{e.stderr}"
            ) from e