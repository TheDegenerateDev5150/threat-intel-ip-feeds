# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-05T08:52:41.553490+00:00
**Duration:** 37.33s
**Successful:** 17/19

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
| Unique to single source | 53,451 |
| Found in multiple sources | 40,463 |
| Max source overlap | 8 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,665 | 25,771 | 54.3% |
| SGB (Turkiye) | 9,755 | 245 | 97.5% |
| Stamparm IPsum | 8,032 | 26,379 | 23.3% |
| AbuseIPDB | 1,671 | 8,329 | 16.7% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| Tor Exit Nodes | 607 | 559 | 52.1% |
| GreenSnow | 375 | 5,582 | 6.3% |
| BinaryDefense | 345 | 2,051 | 14.4% |
| AlienVault OTX | 121 | 39 | 75.6% |
| Blocklist.de (all) | 114 | 21,196 | 0.5% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 22 | 508 | 4.2% |
| Blocklist.de (strongips) | 9 | 320 | 2.7% |
| Blocklist.de (ssh) | 0 | 5,129 | 0.0% |
| Blocklist.de (mail) | 0 | 12,276 | 0.0% |
| Blocklist.de (apache) | 0 | 9,027 | 0.0% |
| Blocklist.de (bots) | 0 | 2,000 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 839 | 0.0% |
| CINS Army | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,898 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,276 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,360 |
| Blocklist.de (all) & Stamparm IPsum | 9,347 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,027 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,267 |
| RTBH (Turkiye) & AbuseIPDB | 6,914 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,129 |
| GreenSnow & RTBH (Turkiye) | 4,915 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 8 | 2026-06-05 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,436 | OK |
| Stamparm IPsum | 34,411 | OK |
| Blocklist.de (all) | 21,310 | OK |
| Blocklist.de (mail) | 12,276 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,027 | OK |
| GreenSnow | 5,957 | OK |
| Blocklist.de (ssh) | 5,129 | OK |
| BinaryDefense | 2,396 | OK |
| Blocklist.de (bots) | 2,000 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,166 | OK |
| Blocklist.de (bruteforcelogin) | 839 | OK |
| Emerging Threats | 530 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 160 | OK |
| Spamhaus DROPv6 | 93 | OK |
| CINS Army | 0 | EMPTY |
