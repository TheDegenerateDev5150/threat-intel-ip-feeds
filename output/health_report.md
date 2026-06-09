# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-09T18:21:20.905698+00:00
**Duration:** 45.6s
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
| Unique to single source | 60,419 |
| Found in multiple sources | 45,300 |
| Max source overlap | 9 |
| Avg sources per IP | 1.84 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,915 | 24,888 | 56.2% |
| SGB (Turkiye) | 9,767 | 233 | 97.7% |
| Stamparm IPsum | 7,617 | 28,989 | 20.8% |
| CINS Army | 6,529 | 8,471 | 43.5% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| AbuseIPDB | 790 | 9,210 | 7.9% |
| BinaryDefense | 715 | 3,027 | 19.1% |
| Tor Exit Nodes | 649 | 608 | 51.6% |
| GreenSnow | 430 | 4,349 | 9.0% |
| AlienVault OTX | 145 | 30 | 82.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 57 | 22,822 | 0.2% |
| Blocklist.de (strongips) | 28 | 309 | 8.3% |
| Emerging Threats | 14 | 505 | 2.7% |
| Blocklist.de (bots) | 9 | 3,127 | 0.3% |
| Blocklist.de (apache) | 1 | 8,912 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,013 | 0.0% |
| Blocklist.de (mail) | 0 | 13,321 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 733 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,201 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,320 |
| Blocklist.de (all) & Stamparm IPsum | 8,931 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,907 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,821 |
| Stamparm IPsum & AbuseIPDB | 8,206 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,504 |
| RTBH (Turkiye) & AbuseIPDB | 7,011 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,003 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 45 | 2026-06-09 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,803 | OK |
| Stamparm IPsum | 36,606 | OK |
| Blocklist.de (all) | 22,879 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,321 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,913 | OK |
| Blocklist.de (ssh) | 5,013 | OK |
| GreenSnow | 4,779 | OK |
| BinaryDefense | 3,742 | OK |
| Blocklist.de (bots) | 3,136 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,257 | OK |
| Blocklist.de (bruteforcelogin) | 733 | OK |
| Emerging Threats | 519 | OK |
| Blocklist.de (strongips) | 337 | OK |
| AlienVault OTX | 175 | OK |
| Spamhaus DROPv6 | 93 | OK |
