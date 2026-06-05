# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-05T12:19:47.719052+00:00
**Duration:** 35.47s
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
| Unique to single source | 54,085 |
| Found in multiple sources | 40,342 |
| Max source overlap | 8 |
| Avg sources per IP | 1.83 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,262 | 25,542 | 55.0% |
| SGB (Turkiye) | 9,755 | 245 | 97.5% |
| Stamparm IPsum | 8,090 | 26,321 | 23.5% |
| AbuseIPDB | 1,665 | 8,335 | 16.7% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| Tor Exit Nodes | 602 | 558 | 51.9% |
| GreenSnow | 360 | 4,572 | 7.3% |
| BinaryDefense | 345 | 2,051 | 14.4% |
| Blocklist.de (all) | 122 | 21,154 | 0.6% |
| AlienVault OTX | 118 | 39 | 75.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 22 | 508 | 4.2% |
| Blocklist.de (strongips) | 8 | 320 | 2.4% |
| Blocklist.de (bruteforcelogin) | 1 | 829 | 0.1% |
| Blocklist.de (ssh) | 0 | 5,127 | 0.0% |
| Blocklist.de (mail) | 0 | 12,242 | 0.0% |
| Blocklist.de (apache) | 0 | 9,003 | 0.0% |
| Blocklist.de (bots) | 0 | 2,023 | 0.0% |
| CINS Army | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,936 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,242 |
| Blocklist.de (all) & Stamparm IPsum | 9,192 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,142 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,003 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,267 |
| RTBH (Turkiye) & AbuseIPDB | 6,925 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,127 |
| Blocklist.de (ssh) & Stamparm IPsum | 4,785 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 9 | 2026-06-05 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,804 | OK |
| Stamparm IPsum | 34,411 | OK |
| Blocklist.de (all) | 21,276 | OK |
| Blocklist.de (mail) | 12,242 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,003 | OK |
| Blocklist.de (ssh) | 5,127 | OK |
| GreenSnow | 4,932 | OK |
| BinaryDefense | 2,396 | OK |
| Blocklist.de (bots) | 2,023 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,160 | OK |
| Blocklist.de (bruteforcelogin) | 830 | OK |
| Emerging Threats | 530 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 157 | OK |
| Spamhaus DROPv6 | 93 | OK |
| CINS Army | 0 | EMPTY |
