# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-09T21:12:53.973252+00:00
**Duration:** 33.82s
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
| Unique to single source | 55,250 |
| Found in multiple sources | 44,966 |
| Max source overlap | 9 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 26,424 | 26,496 | 49.9% |
| SGB (Turkiye) | 9,796 | 204 | 98.0% |
| Stamparm IPsum | 7,844 | 28,762 | 21.4% |
| CINS Army | 6,625 | 8,375 | 44.2% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| AbuseIPDB | 809 | 9,191 | 8.1% |
| BinaryDefense | 719 | 3,023 | 19.2% |
| Tor Exit Nodes | 649 | 607 | 51.7% |
| GreenSnow | 374 | 4,483 | 7.7% |
| AlienVault OTX | 145 | 30 | 82.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (strongips) | 62 | 274 | 18.5% |
| Blocklist.de (all) | 42 | 22,674 | 0.2% |
| Emerging Threats | 8 | 517 | 1.5% |
| Blocklist.de (ssh) | 0 | 5,019 | 0.0% |
| Blocklist.de (mail) | 0 | 13,280 | 0.0% |
| Blocklist.de (apache) | 0 | 8,911 | 0.0% |
| Blocklist.de (bots) | 0 | 3,021 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 742 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,560 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,280 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,679 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,907 |
| Blocklist.de (all) & Stamparm IPsum | 8,862 |
| Stamparm IPsum & AbuseIPDB | 8,206 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,463 |
| RTBH (Turkiye) & AbuseIPDB | 7,058 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,004 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 46 | 2026-06-09 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 52,920 | OK |
| Stamparm IPsum | 36,606 | OK |
| Blocklist.de (all) | 22,716 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,280 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,911 | OK |
| Blocklist.de (ssh) | 5,019 | OK |
| GreenSnow | 4,857 | OK |
| BinaryDefense | 3,742 | OK |
| Blocklist.de (bots) | 3,021 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,256 | OK |
| Blocklist.de (bruteforcelogin) | 742 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 336 | OK |
| AlienVault OTX | 175 | OK |
| Spamhaus DROPv6 | 93 | OK |
