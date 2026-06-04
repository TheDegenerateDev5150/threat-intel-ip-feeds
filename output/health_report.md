# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-04T16:29:13.828934+00:00
**Duration:** 32.08s
**Successful:** 17/19

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
| Unique to single source | 54,351 |
| Found in multiple sources | 41,980 |
| Max source overlap | 8 |
| Avg sources per IP | 1.87 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,179 | 26,791 | 53.0% |
| SGB (Turkiye) | 9,744 | 256 | 97.4% |
| Stamparm IPsum | 9,332 | 25,953 | 26.4% |
| AbuseIPDB | 1,664 | 8,336 | 16.6% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| Tor Exit Nodes | 608 | 556 | 52.2% |
| GreenSnow | 598 | 4,550 | 11.6% |
| BinaryDefense | 252 | 1,861 | 11.9% |
| AlienVault OTX | 117 | 39 | 75.0% |
| Blocklist.de (all) | 100 | 24,214 | 0.4% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 10 | 515 | 1.9% |
| Blocklist.de (strongips) | 7 | 317 | 2.2% |
| Blocklist.de (mail) | 4 | 12,604 | 0.0% |
| Blocklist.de (bruteforcelogin) | 1 | 961 | 0.1% |
| Blocklist.de (ssh) | 0 | 7,558 | 0.0% |
| Blocklist.de (apache) | 0 | 9,191 | 0.0% |
| Blocklist.de (bots) | 0 | 2,202 | 0.0% |
| CINS Army | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,645 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,594 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,581 |
| Blocklist.de (all) & Stamparm IPsum | 10,942 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,191 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,552 |
| Stamparm IPsum & AbuseIPDB | 7,061 |
| RTBH (Turkiye) & AbuseIPDB | 6,790 |
| Blocklist.de (ssh) & Stamparm IPsum | 6,519 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 3 | 2026-06-04 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,970 | OK |
| Stamparm IPsum | 35,285 | OK |
| Blocklist.de (all) | 24,314 | OK |
| Blocklist.de (mail) | 12,608 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,191 | OK |
| Blocklist.de (ssh) | 7,558 | OK |
| GreenSnow | 5,148 | OK |
| Blocklist.de (bots) | 2,202 | OK |
| BinaryDefense | 2,113 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,164 | OK |
| Blocklist.de (bruteforcelogin) | 962 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 324 | OK |
| AlienVault OTX | 156 | OK |
| Spamhaus DROPv6 | 93 | OK |
| CINS Army | 0 | EMPTY |
