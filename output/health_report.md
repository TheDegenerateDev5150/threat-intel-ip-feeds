# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-06T04:20:11.113214+00:00
**Duration:** 28.16s
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
| Unique to single source | 56,424 |
| Found in multiple sources | 46,079 |
| Max source overlap | 9 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 29,575 | 26,353 | 52.9% |
| SGB (Turkiye) | 9,756 | 244 | 97.6% |
| Stamparm IPsum | 7,292 | 30,664 | 19.2% |
| CINS Army | 5,906 | 9,094 | 39.4% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| Tor Exit Nodes | 624 | 623 | 50.0% |
| AbuseIPDB | 617 | 9,383 | 6.2% |
| BinaryDefense | 414 | 2,330 | 15.1% |
| GreenSnow | 297 | 5,462 | 5.2% |
| AlienVault OTX | 113 | 33 | 77.4% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 65 | 22,484 | 0.3% |
| Blocklist.de (strongips) | 19 | 309 | 5.8% |
| Emerging Threats | 11 | 514 | 2.1% |
| Blocklist.de (ssh) | 0 | 5,057 | 0.0% |
| Blocklist.de (mail) | 0 | 12,480 | 0.0% |
| Blocklist.de (apache) | 0 | 8,954 | 0.0% |
| Blocklist.de (bots) | 0 | 3,211 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 712 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,329 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,480 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,604 |
| Blocklist.de (all) & Stamparm IPsum | 9,395 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,954 |
| Stamparm IPsum & AbuseIPDB | 8,664 |
| CINS Army & Stamparm IPsum | 8,324 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,086 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,057 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 15 | 2026-06-06 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,928 | OK |
| Stamparm IPsum | 37,956 | OK |
| Blocklist.de (all) | 22,549 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,480 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,954 | OK |
| GreenSnow | 5,759 | OK |
| Blocklist.de (ssh) | 5,057 | OK |
| Blocklist.de (bots) | 3,211 | OK |
| BinaryDefense | 2,744 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,247 | OK |
| Blocklist.de (bruteforcelogin) | 712 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 146 | OK |
| Spamhaus DROPv6 | 93 | OK |
