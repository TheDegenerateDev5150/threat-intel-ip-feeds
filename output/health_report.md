# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-14T01:37:07.955713+00:00
**Duration:** 39.74s
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
| Unique to single source | 56,359 |
| Found in multiple sources | 44,889 |
| Max source overlap | 9 |
| Avg sources per IP | 1.94 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,336 | 25,985 | 53.9% |
| SGB (Turkiye) | 9,771 | 229 | 97.7% |
| Stamparm IPsum | 7,033 | 31,194 | 18.4% |
| CINS Army | 4,266 | 10,734 | 28.4% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,187 | 3,796 | 23.8% |
| AbuseIPDB | 888 | 9,112 | 8.9% |
| Tor Exit Nodes | 621 | 638 | 49.3% |
| GreenSnow | 253 | 6,217 | 3.9% |
| AlienVault OTX | 146 | 22 | 86.9% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Emerging Threats | 31 | 497 | 5.9% |
| Blocklist.de (strongips) | 20 | 318 | 5.9% |
| Blocklist.de (all) | 16 | 21,420 | 0.1% |
| Blocklist.de (ssh) | 0 | 5,760 | 0.0% |
| Blocklist.de (mail) | 0 | 12,742 | 0.0% |
| Blocklist.de (apache) | 0 | 8,967 | 0.0% |
| Blocklist.de (bots) | 0 | 1,469 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 809 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,479 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,742 |
| Blocklist.de (all) & Stamparm IPsum | 10,113 |
| CINS Army & Stamparm IPsum | 9,779 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,619 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,967 |
| Stamparm IPsum & AbuseIPDB | 8,444 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,918 |
| CINS Army & RTBH (Turkiye) | 6,473 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 77 | 2026-06-14 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,321 | OK |
| Stamparm IPsum | 38,227 | OK |
| Blocklist.de (all) | 21,436 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,742 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,967 | OK |
| GreenSnow | 6,470 | OK |
| Blocklist.de (ssh) | 5,760 | OK |
| BinaryDefense | 4,983 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,469 | OK |
| Tor Exit Nodes | 1,259 | OK |
| Blocklist.de (bruteforcelogin) | 809 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 338 | OK |
| AlienVault OTX | 168 | OK |
| Spamhaus DROPv6 | 94 | OK |
