# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-14T21:39:26.924784+00:00
**Duration:** 34.09s
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
| Unique to single source | 55,950 |
| Found in multiple sources | 46,071 |
| Max source overlap | 9 |
| Avg sources per IP | 1.91 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,602 | 27,437 | 50.1% |
| SGB (Turkiye) | 9,784 | 216 | 97.8% |
| Stamparm IPsum | 7,487 | 30,740 | 19.6% |
| CINS Army | 6,296 | 8,704 | 42.0% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,189 | 3,794 | 23.9% |
| AbuseIPDB | 701 | 9,299 | 7.0% |
| Tor Exit Nodes | 613 | 643 | 48.8% |
| GreenSnow | 261 | 5,114 | 4.9% |
| AlienVault OTX | 145 | 22 | 86.8% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Emerging Threats | 31 | 497 | 5.9% |
| Blocklist.de (all) | 26 | 21,943 | 0.1% |
| Blocklist.de (strongips) | 23 | 319 | 6.7% |
| Blocklist.de (bots) | 1 | 2,164 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,468 | 0.0% |
| Blocklist.de (mail) | 0 | 12,608 | 0.0% |
| Blocklist.de (apache) | 0 | 9,154 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 922 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,165 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,608 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,290 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,154 |
| Blocklist.de (all) & Stamparm IPsum | 9,102 |
| Stamparm IPsum & AbuseIPDB | 8,217 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,651 |
| RTBH (Turkiye) & AbuseIPDB | 7,064 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,468 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 84 | 2026-06-14 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,039 | OK |
| Stamparm IPsum | 38,227 | OK |
| Blocklist.de (all) | 21,969 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,608 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,154 | OK |
| Blocklist.de (ssh) | 5,468 | OK |
| GreenSnow | 5,375 | OK |
| BinaryDefense | 4,983 | OK |
| Blocklist.de (bots) | 2,165 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,256 | OK |
| Blocklist.de (bruteforcelogin) | 922 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 167 | OK |
| Spamhaus DROPv6 | 94 | OK |
