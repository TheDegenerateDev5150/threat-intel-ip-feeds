# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-05T16:09:35.087435+00:00
**Duration:** 63.45s
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
| Unique to single source | 58,854 |
| Found in multiple sources | 43,864 |
| Max source overlap | 9 |
| Avg sources per IP | 1.84 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,769 | 26,368 | 53.9% |
| SGB (Turkiye) | 9,752 | 248 | 97.5% |
| CINS Army | 7,621 | 7,379 | 50.8% |
| Stamparm IPsum | 6,198 | 28,213 | 18.0% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 1,112 | 8,888 | 11.1% |
| Tor Exit Nodes | 666 | 561 | 54.3% |
| GreenSnow | 387 | 4,600 | 7.8% |
| BinaryDefense | 334 | 2,062 | 13.9% |
| Blocklist.de (all) | 133 | 21,196 | 0.6% |
| AlienVault OTX | 115 | 39 | 74.7% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 22 | 508 | 4.2% |
| Blocklist.de (strongips) | 7 | 320 | 2.1% |
| Blocklist.de (bruteforcelogin) | 3 | 812 | 0.4% |
| Blocklist.de (ssh) | 0 | 5,123 | 0.0% |
| Blocklist.de (mail) | 0 | 12,288 | 0.0% |
| Blocklist.de (apache) | 0 | 8,985 | 0.0% |
| Blocklist.de (bots) | 0 | 2,062 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,984 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,288 |
| Blocklist.de (all) & Stamparm IPsum | 9,054 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,985 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,925 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,267 |
| RTBH (Turkiye) & AbuseIPDB | 6,937 |
| CINS Army & Stamparm IPsum | 5,460 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,120 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 10 | 2026-06-05 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,137 | OK |
| Stamparm IPsum | 34,411 | OK |
| Blocklist.de (all) | 21,329 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,288 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,985 | OK |
| Blocklist.de (ssh) | 5,123 | OK |
| GreenSnow | 4,987 | OK |
| BinaryDefense | 2,396 | OK |
| Blocklist.de (bots) | 2,062 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,227 | OK |
| Blocklist.de (bruteforcelogin) | 815 | OK |
| Emerging Threats | 530 | OK |
| Blocklist.de (strongips) | 327 | OK |
| AlienVault OTX | 154 | OK |
| Spamhaus DROPv6 | 93 | OK |
