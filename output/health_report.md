# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-08T07:03:52.960020+00:00
**Duration:** 37.92s
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
| Unique to single source | 57,136 |
| Found in multiple sources | 46,505 |
| Max source overlap | 8 |
| Avg sources per IP | 1.87 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 29,599 | 25,465 | 53.8% |
| SGB (Turkiye) | 9,765 | 235 | 97.7% |
| Stamparm IPsum | 7,513 | 30,362 | 19.8% |
| CINS Army | 5,871 | 9,129 | 39.1% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 1,015 | 8,985 | 10.2% |
| Tor Exit Nodes | 653 | 607 | 51.8% |
| BinaryDefense | 546 | 2,811 | 16.3% |
| GreenSnow | 239 | 4,845 | 4.7% |
| AlienVault OTX | 105 | 27 | 79.5% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 41 | 484 | 7.8% |
| Blocklist.de (all) | 33 | 22,741 | 0.1% |
| Blocklist.de (strongips) | 21 | 312 | 6.3% |
| Blocklist.de (ssh) | 0 | 4,914 | 0.0% |
| Blocklist.de (mail) | 0 | 12,498 | 0.0% |
| Blocklist.de (apache) | 0 | 8,760 | 0.0% |
| Blocklist.de (bots) | 0 | 3,943 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 597 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,774 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,498 |
| Blocklist.de (all) & Stamparm IPsum | 8,871 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,760 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,756 |
| CINS Army & Stamparm IPsum | 8,264 |
| Stamparm IPsum & AbuseIPDB | 8,212 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,673 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,914 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 35 | 2026-06-08 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,064 | OK |
| Stamparm IPsum | 37,875 | OK |
| Blocklist.de (all) | 22,774 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,498 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,760 | OK |
| GreenSnow | 5,084 | OK |
| Blocklist.de (ssh) | 4,914 | OK |
| Blocklist.de (bots) | 3,943 | OK |
| BinaryDefense | 3,357 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 597 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 333 | OK |
| AlienVault OTX | 132 | OK |
| Spamhaus DROPv6 | 93 | OK |
