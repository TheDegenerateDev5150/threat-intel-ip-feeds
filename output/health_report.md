# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-07T00:17:10.200670+00:00
**Duration:** 32.12s
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
| Unique to single source | 56,376 |
| Found in multiple sources | 47,480 |
| Max source overlap | 9 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,174 | 27,794 | 50.3% |
| SGB (Turkiye) | 9,761 | 239 | 97.6% |
| Stamparm IPsum | 7,733 | 30,223 | 20.4% |
| CINS Army | 6,603 | 8,397 | 44.0% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 767 | 9,233 | 7.7% |
| Tor Exit Nodes | 621 | 625 | 49.8% |
| BinaryDefense | 503 | 2,537 | 16.5% |
| GreenSnow | 285 | 5,199 | 5.2% |
| AlienVault OTX | 112 | 30 | 78.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 47 | 22,830 | 0.2% |
| Blocklist.de (strongips) | 24 | 305 | 7.3% |
| Emerging Threats | 11 | 514 | 2.1% |
| Blocklist.de (ssh) | 0 | 4,701 | 0.0% |
| Blocklist.de (mail) | 0 | 12,546 | 0.0% |
| Blocklist.de (apache) | 0 | 8,706 | 0.0% |
| Blocklist.de (bots) | 0 | 4,187 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 524 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,043 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,546 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,728 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,706 |
| Blocklist.de (all) & Stamparm IPsum | 8,337 |
| Stamparm IPsum & AbuseIPDB | 8,019 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,363 |
| RTBH (Turkiye) & AbuseIPDB | 6,797 |
| GreenSnow & RTBH (Turkiye) | 4,832 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 24 | 2026-06-07 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,968 | OK |
| Stamparm IPsum | 37,956 | OK |
| Blocklist.de (all) | 22,877 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,546 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,706 | OK |
| GreenSnow | 5,484 | OK |
| Blocklist.de (ssh) | 4,701 | OK |
| Blocklist.de (bots) | 4,187 | OK |
| BinaryDefense | 3,040 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,246 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (bruteforcelogin) | 524 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 142 | OK |
| Spamhaus DROPv6 | 93 | OK |
