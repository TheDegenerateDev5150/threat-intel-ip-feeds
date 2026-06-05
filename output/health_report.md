# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-05T20:13:24.326605+00:00
**Duration:** 41.03s
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
| Unique to single source | 58,902 |
| Found in multiple sources | 44,285 |
| Max source overlap | 9 |
| Avg sources per IP | 1.84 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,159 | 26,364 | 54.2% |
| SGB (Turkiye) | 9,758 | 242 | 97.6% |
| CINS Army | 7,250 | 7,750 | 48.3% |
| Stamparm IPsum | 6,469 | 27,942 | 18.8% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 839 | 9,161 | 8.4% |
| Tor Exit Nodes | 681 | 567 | 54.6% |
| GreenSnow | 411 | 4,663 | 8.1% |
| BinaryDefense | 332 | 2,064 | 13.9% |
| Blocklist.de (all) | 126 | 21,582 | 0.6% |
| AlienVault OTX | 113 | 33 | 77.4% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 22 | 508 | 4.2% |
| Blocklist.de (strongips) | 7 | 321 | 2.1% |
| Blocklist.de (ssh) | 0 | 5,127 | 0.0% |
| Blocklist.de (mail) | 0 | 12,275 | 0.0% |
| Blocklist.de (apache) | 0 | 8,965 | 0.0% |
| Blocklist.de (bots) | 0 | 2,497 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 767 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,033 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,275 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,965 |
| Blocklist.de (all) & Stamparm IPsum | 8,841 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,764 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,386 |
| RTBH (Turkiye) & AbuseIPDB | 6,998 |
| CINS Army & Stamparm IPsum | 5,706 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,127 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 12 | 2026-06-05 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,523 | OK |
| Stamparm IPsum | 34,411 | OK |
| Blocklist.de (all) | 21,708 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,275 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,965 | OK |
| Blocklist.de (ssh) | 5,127 | OK |
| GreenSnow | 5,074 | OK |
| Blocklist.de (bots) | 2,497 | OK |
| BinaryDefense | 2,396 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,248 | OK |
| Blocklist.de (bruteforcelogin) | 767 | OK |
| Emerging Threats | 530 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 146 | OK |
| Spamhaus DROPv6 | 93 | OK |
