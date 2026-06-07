# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-07T12:52:29.385307+00:00
**Duration:** 33.78s
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
| Unique to single source | 58,062 |
| Found in multiple sources | 47,692 |
| Max source overlap | 8 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,802 | 26,095 | 54.1% |
| SGB (Turkiye) | 9,764 | 236 | 97.6% |
| Stamparm IPsum | 7,310 | 30,358 | 19.4% |
| CINS Army | 6,217 | 8,783 | 41.4% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 668 | 9,332 | 6.7% |
| Tor Exit Nodes | 628 | 627 | 50.0% |
| BinaryDefense | 471 | 2,569 | 15.5% |
| GreenSnow | 241 | 3,950 | 5.8% |
| AlienVault OTX | 104 | 29 | 78.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 41 | 23,582 | 0.2% |
| Emerging Threats | 30 | 495 | 5.7% |
| Blocklist.de (strongips) | 25 | 304 | 7.6% |
| Blocklist.de (bots) | 11 | 4,731 | 0.2% |
| Blocklist.de (mail) | 9 | 12,647 | 0.1% |
| Blocklist.de (apache) | 6 | 8,775 | 0.1% |
| Blocklist.de (ssh) | 0 | 4,812 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 548 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,224 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,632 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,934 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,774 |
| Blocklist.de (all) & Stamparm IPsum | 8,546 |
| Stamparm IPsum & AbuseIPDB | 8,385 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,854 |
| RTBH (Turkiye) & AbuseIPDB | 6,849 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,812 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 28 | 2026-06-07 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,897 | OK |
| Stamparm IPsum | 37,668 | OK |
| Blocklist.de (all) | 23,623 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,656 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,781 | OK |
| Blocklist.de (ssh) | 4,812 | OK |
| Blocklist.de (bots) | 4,742 | OK |
| GreenSnow | 4,191 | OK |
| BinaryDefense | 3,040 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,255 | OK |
| Blocklist.de (bruteforcelogin) | 548 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 133 | OK |
| Spamhaus DROPv6 | 93 | OK |
