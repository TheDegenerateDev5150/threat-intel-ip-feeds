# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-11T01:40:09.955887+00:00
**Duration:** 56.88s
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
| Unique to single source | 55,232 |
| Found in multiple sources | 47,916 |
| Max source overlap | 9 |
| Avg sources per IP | 1.97 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,087 | 27,905 | 50.2% |
| SGB (Turkiye) | 9,767 | 233 | 97.7% |
| Stamparm IPsum | 7,673 | 32,454 | 19.1% |
| CINS Army | 4,612 | 10,388 | 30.7% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| AbuseIPDB | 1,326 | 8,674 | 13.3% |
| BinaryDefense | 867 | 3,401 | 20.3% |
| Tor Exit Nodes | 617 | 643 | 49.0% |
| GreenSnow | 283 | 5,104 | 5.3% |
| AlienVault OTX | 152 | 27 | 84.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 57 | 24,793 | 0.2% |
| Blocklist.de (strongips) | 19 | 323 | 5.6% |
| Emerging Threats | 17 | 510 | 3.2% |
| Blocklist.de (bots) | 2 | 2,196 | 0.1% |
| Blocklist.de (ssh) | 0 | 7,631 | 0.0% |
| Blocklist.de (mail) | 0 | 13,418 | 0.0% |
| Blocklist.de (apache) | 0 | 9,148 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 973 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,110 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,401 |
| Blocklist.de (all) & RTBH (Turkiye) | 12,335 |
| Blocklist.de (all) & Stamparm IPsum | 11,454 |
| CINS Army & Stamparm IPsum | 9,519 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,148 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,900 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,617 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 6,597 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 55 | 2026-06-11 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,992 | OK |
| Stamparm IPsum | 40,127 | OK |
| Blocklist.de (all) | 24,850 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,418 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,148 | OK |
| Blocklist.de (ssh) | 7,631 | OK |
| GreenSnow | 5,387 | OK |
| BinaryDefense | 4,268 | OK |
| Blocklist.de (bots) | 2,198 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 973 | OK |
| Emerging Threats | 527 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 179 | OK |
| Spamhaus DROPv6 | 93 | OK |
