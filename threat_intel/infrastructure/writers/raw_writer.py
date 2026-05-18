"""Raw text output — one IP/CIDR per line, no headers. Firewall-ready."""

from __future__ import annotations

import os
import re
from collections import defaultdict

from threat_intel.domain.entities import CollectionResult, IPVersion
from threat_intel.domain.ports import OutputWriter


def _source_slug(name: str) -> str:
    """Convert a source name into a safe lowercase filename slug."""
    return re.sub(r"[^a-z0-9]+", "", name.lower())


class RawIPv4Writer(OutputWriter):
    """Writes hourlyIPv4.txt — bare IPs + CIDRs, one per line."""

    @property
    def format_name(self) -> str:
        return "Raw IPv4"

    def write(self, result: CollectionResult, output_dir: str) -> str:
        path = os.path.join(output_dir, "hourlyIPv4.txt")
        os.makedirs(output_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            for ip in result.ipv4_ips:
                f.write(f"{ip}\n")
            for cidr in result.ipv4_cidrs:
                f.write(f"{cidr}\n")
        return path


class PerSourceIPv4Writer(OutputWriter):
    """Writes one bare IPv4 file per source — e.g. sgbturkiyehourly.txt.

    Each file contains the same firewall-ready format as hourlyIPv4.txt
    (one IP/CIDR per line, no headers) but limited to entries reported
    by that single source. Whitelist filtering is preserved — entries
    come from the deduplicated indicators, not raw source results.
    """

    @property
    def format_name(self) -> str:
        return "Per-source IPv4"

    def write(self, result: CollectionResult, output_dir: str) -> str:
        os.makedirs(output_dir, exist_ok=True)

        per_source_ips: dict[str, list[str]] = defaultdict(list)
        per_source_cidrs: dict[str, list[str]] = defaultdict(list)
        for indicator in result.indicators:
            if indicator.ip.version != IPVersion.V4:
                continue
            target = per_source_cidrs if indicator.ip.is_cidr else per_source_ips
            for src in indicator.sources:
                target[src].append(indicator.ip.raw)

        all_sources = {sr.source_name for sr in result.source_results}
        written = []
        for source_name in all_sources:
            slug = _source_slug(source_name)
            if not slug:
                continue
            path = os.path.join(output_dir, f"{slug}hourly.txt")
            ips = sorted(set(per_source_ips.get(source_name, [])))
            cidrs = sorted(set(per_source_cidrs.get(source_name, [])))
            with open(path, "w", encoding="utf-8") as f:
                for ip in ips:
                    f.write(f"{ip}\n")
                for cidr in cidrs:
                    f.write(f"{cidr}\n")
            written.append(path)

        return ", ".join(written) if written else output_dir


class AnnotatedIPv4Writer(OutputWriter):
    """Writes ipv4_blacklist.txt — IPs with metadata header."""

    @property
    def format_name(self) -> str:
        return "Annotated IPv4"

    def write(self, result: CollectionResult, output_dir: str) -> str:
        path = os.path.join(output_dir, "ipv4_blacklist.txt")
        os.makedirs(output_dir, exist_ok=True)
        ips = result.ipv4_ips
        cidrs = result.ipv4_cidrs
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# IPv4 Blacklist\n")
            f.write(f"# Updated: {result.timestamp.isoformat()}\n")
            f.write(f"# IPs: {len(ips)} | CIDRs: {len(cidrs)}\n")
            f.write(f"# Duration: {result.elapsed_seconds}s\n")
            f.write(f"# Sources: {result.successful_sources}/{result.total_sources} OK\n")
            if result.whitelist_filtered_count > 0:
                f.write(f"# Whitelist filtered: {result.whitelist_filtered_count}\n")
            f.write("#\n")
            for ip in ips:
                f.write(f"{ip}\n")
            if cidrs:
                f.write("#\n# === CIDR ===\n")
                for cidr in cidrs:
                    f.write(f"{cidr}\n")
        return path


class AnnotatedIPv6Writer(OutputWriter):
    """Writes ipv6_blacklist.txt — IPv6 addresses with metadata header."""

    @property
    def format_name(self) -> str:
        return "Annotated IPv6"

    def write(self, result: CollectionResult, output_dir: str) -> str:
        path = os.path.join(output_dir, "ipv6_blacklist.txt")
        os.makedirs(output_dir, exist_ok=True)
        ips = result.ipv6_ips
        cidrs = result.ipv6_cidrs
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# IPv6 Blacklist\n")
            f.write(f"# Updated: {result.timestamp.isoformat()}\n")
            f.write(f"# IPs: {len(ips)} | CIDRs: {len(cidrs)}\n")
            f.write(f"# Duration: {result.elapsed_seconds}s\n")
            f.write(f"# Sources: {result.successful_sources}/{result.total_sources} OK\n")
            f.write("#\n")
            for ip in ips:
                f.write(f"{ip}\n")
            if cidrs:
                f.write("#\n# === CIDR ===\n")
                for cidr in cidrs:
                    f.write(f"{cidr}\n")
        return path
