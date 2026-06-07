# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-07T04:59:12.469081+00:00
**Duration:** 36.19s
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
| Unique to single source | 56,224 |
| Found in multiple sources | 47,346 |
| Max source overlap | 9 |
| Avg sources per IP | 1.89 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 29,792 | 26,539 | 52.9% |
| SGB (Turkiye) | 9,765 | 235 | 97.7% |
| Stamparm IPsum | 7,304 | 30,364 | 19.4% |
| CINS Army | 5,410 | 9,590 | 36.1% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 674 | 9,326 | 6.7% |
| Tor Exit Nodes | 618 | 628 | 49.6% |
| BinaryDefense | 473 | 2,567 | 15.6% |
| GreenSnow | 246 | 5,242 | 4.5% |
| AlienVault OTX | 112 | 30 | 78.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 39 | 23,199 | 0.2% |
| Emerging Threats | 30 | 495 | 5.7% |
| Blocklist.de (strongips) | 25 | 303 | 7.6% |
| Blocklist.de (bots) | 1 | 4,411 | 0.0% |
| Blocklist.de (ssh) | 0 | 4,685 | 0.0% |
| Blocklist.de (mail) | 0 | 12,633 | 0.0% |
| Blocklist.de (apache) | 0 | 8,763 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 531 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,100 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,633 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,400 |
| Blocklist.de (all) & Stamparm IPsum | 8,862 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,763 |
| CINS Army & Stamparm IPsum | 8,645 |
| Stamparm IPsum & AbuseIPDB | 8,385 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,821 |
| CINS Army & RTBH (Turkiye) | 5,163 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 25 | 2026-06-07 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,331 | OK |
| Stamparm IPsum | 37,668 | OK |
| Blocklist.de (all) | 23,238 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,633 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,763 | OK |
| GreenSnow | 5,488 | OK |
| Blocklist.de (ssh) | 4,685 | OK |
| Blocklist.de (bots) | 4,412 | OK |
| BinaryDefense | 3,040 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,246 | OK |
| Blocklist.de (bruteforcelogin) | 531 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 142 | OK |
| Spamhaus DROPv6 | 93 | OK |
