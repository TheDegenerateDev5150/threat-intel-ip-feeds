# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-11T16:20:52.309244+00:00
**Duration:** 52.6s
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
| Unique to single source | 59,791 |
| Found in multiple sources | 47,376 |
| Max source overlap | 9 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,110 | 27,361 | 52.4% |
| SGB (Turkiye) | 9,768 | 232 | 97.7% |
| Stamparm IPsum | 8,281 | 31,846 | 20.6% |
| CINS Army | 6,317 | 8,683 | 42.1% |
| Spamhaus DROP | 1,698 | 0 | 100.0% |
| AbuseIPDB | 1,324 | 8,676 | 13.2% |
| BinaryDefense | 867 | 3,401 | 20.3% |
| Tor Exit Nodes | 617 | 643 | 49.0% |
| GreenSnow | 450 | 4,162 | 9.8% |
| AlienVault OTX | 163 | 25 | 86.7% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 63 | 24,517 | 0.3% |
| Blocklist.de (strongips) | 18 | 323 | 5.3% |
| Emerging Threats | 17 | 510 | 3.2% |
| Blocklist.de (bots) | 4 | 1,716 | 0.2% |
| Blocklist.de (ssh) | 0 | 7,724 | 0.0% |
| Blocklist.de (mail) | 0 | 13,550 | 0.0% |
| Blocklist.de (apache) | 0 | 9,128 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 948 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,348 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,548 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,191 |
| Blocklist.de (all) & Stamparm IPsum | 11,047 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,127 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,900 |
| CINS Army & Stamparm IPsum | 7,766 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,722 |
| RTBH (Turkiye) & AbuseIPDB | 6,494 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 58 | 2026-06-11 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,471 | OK |
| Stamparm IPsum | 40,127 | OK |
| Blocklist.de (all) | 24,580 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,550 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,128 | OK |
| Blocklist.de (ssh) | 7,724 | OK |
| GreenSnow | 4,612 | OK |
| BinaryDefense | 4,268 | OK |
| Blocklist.de (bots) | 1,720 | OK |
| Spamhaus DROP | 1,698 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 948 | OK |
| Emerging Threats | 527 | OK |
| Blocklist.de (strongips) | 341 | OK |
| AlienVault OTX | 188 | OK |
| Spamhaus DROPv6 | 94 | OK |
