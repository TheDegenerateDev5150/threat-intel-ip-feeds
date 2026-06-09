# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-09T04:35:36.082780+00:00
**Duration:** 41.03s
**Successful:** 18/19

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| SGB (Turkiye) | HttpError: HTTP 429: <html>
<head><title>429 Too Many Requests</title></head>
<body>
<center><h1>429 Too Many Requests</h1></center>
<hr><center>nginx</center>
</body>
</html>
 | 10,000 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 57,468 |
| Found in multiple sources | 45,233 |
| Max source overlap | 9 |
| Avg sources per IP | 1.89 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,345 | 25,098 | 54.7% |
| SGB (Turkiye) | 9,766 | 234 | 97.7% |
| Stamparm IPsum | 7,204 | 29,402 | 19.7% |
| CINS Army | 5,499 | 9,501 | 36.7% |
| Spamhaus DROP | 1,621 | 0 | 100.0% |
| AbuseIPDB | 1,079 | 8,921 | 10.8% |
| BinaryDefense | 719 | 3,023 | 19.2% |
| Tor Exit Nodes | 651 | 606 | 51.8% |
| GreenSnow | 242 | 5,114 | 4.5% |
| AlienVault OTX | 130 | 30 | 81.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 30 | 22,660 | 0.1% |
| Blocklist.de (strongips) | 28 | 307 | 8.4% |
| Blocklist.de (mail) | 27 | 12,772 | 0.2% |
| Blocklist.de (bots) | 18 | 3,351 | 0.5% |
| Emerging Threats | 14 | 505 | 2.7% |
| Blocklist.de (apache) | 2 | 8,855 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,099 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 687 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 20,915 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,759 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,518 |
| Blocklist.de (all) & Stamparm IPsum | 9,211 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,852 |
| CINS Army & Stamparm IPsum | 8,638 |
| Stamparm IPsum & AbuseIPDB | 8,134 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,811 |
| CINS Army & RTBH (Turkiye) | 5,305 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 41 | 2026-06-09 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,443 | OK |
| Stamparm IPsum | 36,606 | OK |
| Blocklist.de (all) | 22,690 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,799 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,857 | OK |
| GreenSnow | 5,356 | OK |
| Blocklist.de (ssh) | 5,099 | OK |
| BinaryDefense | 3,742 | OK |
| Blocklist.de (bots) | 3,369 | OK |
| Spamhaus DROP | 1,621 | OK |
| Tor Exit Nodes | 1,257 | OK |
| Blocklist.de (bruteforcelogin) | 687 | OK |
| Emerging Threats | 519 | OK |
| Blocklist.de (strongips) | 335 | OK |
| AlienVault OTX | 160 | OK |
| Spamhaus DROPv6 | 93 | OK |
