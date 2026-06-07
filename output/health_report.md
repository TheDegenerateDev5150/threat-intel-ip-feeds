# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-07T08:30:14.118188+00:00
**Duration:** 34.5s
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
| Unique to single source | 57,466 |
| Found in multiple sources | 47,718 |
| Max source overlap | 9 |
| Avg sources per IP | 1.87 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,176 | 26,399 | 53.3% |
| SGB (Turkiye) | 9,765 | 235 | 97.7% |
| Stamparm IPsum | 7,160 | 30,508 | 19.0% |
| CINS Army | 6,344 | 8,656 | 42.3% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 709 | 9,291 | 7.1% |
| Tor Exit Nodes | 619 | 628 | 49.6% |
| BinaryDefense | 474 | 2,566 | 15.6% |
| GreenSnow | 275 | 5,162 | 5.1% |
| AlienVault OTX | 112 | 30 | 78.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 42 | 23,430 | 0.2% |
| Emerging Threats | 30 | 495 | 5.7% |
| Blocklist.de (strongips) | 25 | 303 | 7.6% |
| Blocklist.de (ssh) | 0 | 4,779 | 0.0% |
| Blocklist.de (mail) | 0 | 12,662 | 0.0% |
| Blocklist.de (apache) | 0 | 8,785 | 0.0% |
| Blocklist.de (bots) | 0 | 4,565 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 554 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,151 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,662 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,189 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,785 |
| Blocklist.de (all) & Stamparm IPsum | 8,740 |
| Stamparm IPsum & AbuseIPDB | 8,385 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,830 |
| RTBH (Turkiye) & AbuseIPDB | 6,836 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,779 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 26 | 2026-06-07 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,575 | OK |
| Stamparm IPsum | 37,668 | OK |
| Blocklist.de (all) | 23,472 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,662 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,785 | OK |
| GreenSnow | 5,437 | OK |
| Blocklist.de (ssh) | 4,779 | OK |
| Blocklist.de (bots) | 4,565 | OK |
| BinaryDefense | 3,040 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,247 | OK |
| Blocklist.de (bruteforcelogin) | 554 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 142 | OK |
| Spamhaus DROPv6 | 93 | OK |
