# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-14T15:18:17.687730+00:00
**Duration:** 41.55s
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
| Unique to single source | 59,423 |
| Found in multiple sources | 45,112 |
| Max source overlap | 8 |
| Avg sources per IP | 1.87 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,671 | 25,720 | 55.2% |
| SGB (Turkiye) | 9,780 | 220 | 97.8% |
| Stamparm IPsum | 7,186 | 31,041 | 18.8% |
| CINS Army | 5,919 | 9,081 | 39.5% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,177 | 3,806 | 23.6% |
| AbuseIPDB | 700 | 9,300 | 7.0% |
| Tor Exit Nodes | 616 | 643 | 48.9% |
| GreenSnow | 358 | 4,906 | 6.8% |
| AlienVault OTX | 145 | 22 | 86.8% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Emerging Threats | 31 | 497 | 5.9% |
| Blocklist.de (all) | 29 | 21,117 | 0.1% |
| Blocklist.de (strongips) | 20 | 321 | 5.9% |
| Blocklist.de (ssh) | 0 | 5,601 | 0.0% |
| Blocklist.de (mail) | 0 | 12,536 | 0.0% |
| Blocklist.de (apache) | 0 | 9,110 | 0.0% |
| Blocklist.de (bots) | 0 | 1,327 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 898 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,652 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,536 |
| Blocklist.de (all) & Stamparm IPsum | 9,476 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,110 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,648 |
| Stamparm IPsum & AbuseIPDB | 8,217 |
| CINS Army & Stamparm IPsum | 8,026 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,954 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,601 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 81 | 2026-06-14 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,391 | OK |
| Stamparm IPsum | 38,227 | OK |
| Blocklist.de (all) | 21,146 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,536 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,110 | OK |
| Blocklist.de (ssh) | 5,601 | OK |
| GreenSnow | 5,264 | OK |
| BinaryDefense | 4,983 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,327 | OK |
| Tor Exit Nodes | 1,259 | OK |
| Blocklist.de (bruteforcelogin) | 898 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 341 | OK |
| AlienVault OTX | 167 | OK |
| Spamhaus DROPv6 | 94 | OK |
