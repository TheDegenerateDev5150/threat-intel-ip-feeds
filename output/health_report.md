# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-07T22:18:11.703382+00:00
**Duration:** 36.93s
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
| Unique to single source | 55,484 |
| Found in multiple sources | 47,150 |
| Max source overlap | 9 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 26,913 | 27,448 | 49.5% |
| SGB (Turkiye) | 9,765 | 235 | 97.7% |
| Stamparm IPsum | 7,891 | 29,777 | 20.9% |
| CINS Army | 6,551 | 8,449 | 43.7% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 1,118 | 8,882 | 11.2% |
| Tor Exit Nodes | 637 | 623 | 50.6% |
| BinaryDefense | 470 | 2,570 | 15.5% |
| GreenSnow | 220 | 4,118 | 5.1% |
| AlienVault OTX | 105 | 27 | 79.5% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 31 | 494 | 5.9% |
| Blocklist.de (all) | 24 | 23,300 | 0.1% |
| Blocklist.de (strongips) | 24 | 308 | 7.2% |
| Blocklist.de (ssh) | 0 | 4,914 | 0.0% |
| Blocklist.de (mail) | 0 | 12,726 | 0.0% |
| Blocklist.de (apache) | 0 | 8,758 | 0.0% |
| Blocklist.de (bots) | 0 | 4,276 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 564 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,385 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,726 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,314 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,758 |
| Blocklist.de (all) & Stamparm IPsum | 8,242 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,841 |
| CINS Army & Stamparm IPsum | 7,492 |
| RTBH (Turkiye) & AbuseIPDB | 6,626 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,914 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 33 | 2026-06-07 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 54,361 | OK |
| Stamparm IPsum | 37,668 | OK |
| Blocklist.de (all) | 23,324 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,726 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,758 | OK |
| Blocklist.de (ssh) | 4,914 | OK |
| GreenSnow | 4,338 | OK |
| Blocklist.de (bots) | 4,276 | OK |
| BinaryDefense | 3,040 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 564 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 332 | OK |
| AlienVault OTX | 132 | OK |
| Spamhaus DROPv6 | 93 | OK |
