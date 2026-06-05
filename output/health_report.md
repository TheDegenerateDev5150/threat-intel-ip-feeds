# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-05T04:47:34.616171+00:00
**Duration:** 41.76s
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
| Unique to single source | 51,758 |
| Found in multiple sources | 41,509 |
| Max source overlap | 8 |
| Avg sources per IP | 1.92 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,982 | 26,998 | 51.8% |
| SGB (Turkiye) | 9,755 | 245 | 97.5% |
| Stamparm IPsum | 8,073 | 26,338 | 23.5% |
| AbuseIPDB | 1,679 | 8,321 | 16.8% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| Tor Exit Nodes | 607 | 560 | 52.0% |
| BinaryDefense | 345 | 2,051 | 14.4% |
| GreenSnow | 324 | 5,634 | 5.4% |
| AlienVault OTX | 118 | 39 | 75.2% |
| Blocklist.de (all) | 109 | 23,950 | 0.5% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 22 | 508 | 4.2% |
| Blocklist.de (strongips) | 9 | 320 | 2.7% |
| Blocklist.de (ssh) | 0 | 7,606 | 0.0% |
| Blocklist.de (mail) | 0 | 12,378 | 0.0% |
| Blocklist.de (apache) | 0 | 9,112 | 0.0% |
| Blocklist.de (bots) | 0 | 2,090 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 904 | 0.0% |
| CINS Army | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,837 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,378 |
| Blocklist.de (all) & RTBH (Turkiye) | 12,280 |
| Blocklist.de (all) & Stamparm IPsum | 11,015 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,112 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,606 |
| Stamparm IPsum & AbuseIPDB | 7,267 |
| RTBH (Turkiye) & AbuseIPDB | 6,902 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 6,548 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 7 | 2026-06-05 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,980 | OK |
| Stamparm IPsum | 34,411 | OK |
| Blocklist.de (all) | 24,059 | OK |
| Blocklist.de (mail) | 12,378 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,112 | OK |
| Blocklist.de (ssh) | 7,606 | OK |
| GreenSnow | 5,958 | OK |
| BinaryDefense | 2,396 | OK |
| Blocklist.de (bots) | 2,090 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,167 | OK |
| Blocklist.de (bruteforcelogin) | 904 | OK |
| Emerging Threats | 530 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 157 | OK |
| Spamhaus DROPv6 | 93 | OK |
| CINS Army | 0 | EMPTY |
