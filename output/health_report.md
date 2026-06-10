# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-10T20:45:31.330123+00:00
**Duration:** 45.71s
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
| Unique to single source | 59,659 |
| Found in multiple sources | 48,254 |
| Max source overlap | 9 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,563 | 29,895 | 50.6% |
| SGB (Turkiye) | 9,763 | 237 | 97.6% |
| Stamparm IPsum | 7,922 | 30,393 | 20.7% |
| CINS Army | 6,288 | 8,712 | 41.9% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| AbuseIPDB | 1,464 | 8,536 | 14.6% |
| BinaryDefense | 751 | 3,265 | 18.7% |
| Tor Exit Nodes | 625 | 635 | 49.6% |
| GreenSnow | 304 | 4,363 | 6.5% |
| AlienVault OTX | 152 | 27 | 84.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 27 | 24,905 | 0.1% |
| Blocklist.de (strongips) | 18 | 323 | 5.3% |
| Emerging Threats | 16 | 509 | 3.0% |
| Blocklist.de (mail) | 9 | 13,427 | 0.1% |
| Blocklist.de (ssh) | 3 | 7,719 | 0.0% |
| Blocklist.de (bruteforcelogin) | 1 | 969 | 0.1% |
| Blocklist.de (apache) | 0 | 9,126 | 0.0% |
| Blocklist.de (bots) | 0 | 2,212 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,196 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,422 |
| Blocklist.de (all) & RTBH (Turkiye) | 13,032 |
| Blocklist.de (all) & Stamparm IPsum | 9,433 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,126 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,710 |
| CINS Army & Stamparm IPsum | 7,576 |
| Stamparm IPsum & AbuseIPDB | 7,408 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 6,761 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 53 | 2026-06-10 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 60,458 | OK |
| Stamparm IPsum | 38,315 | OK |
| Blocklist.de (all) | 24,932 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,436 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,126 | OK |
| Blocklist.de (ssh) | 7,722 | OK |
| GreenSnow | 4,667 | OK |
| BinaryDefense | 4,016 | OK |
| Blocklist.de (bots) | 2,212 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 970 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 341 | OK |
| AlienVault OTX | 179 | OK |
| Spamhaus DROPv6 | 93 | OK |
