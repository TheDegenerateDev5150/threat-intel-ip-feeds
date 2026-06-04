# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-04T09:00:52.744755+00:00
**Duration:** 42.77s
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
| Unique to single source | 52,881 |
| Found in multiple sources | 42,201 |
| Max source overlap | 8 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,804 | 27,343 | 51.3% |
| SGB (Turkiye) | 9,736 | 264 | 97.4% |
| Stamparm IPsum | 9,286 | 25,999 | 26.3% |
| AbuseIPDB | 1,683 | 8,317 | 16.8% |
| Spamhaus DROP | 1,641 | 0 | 100.0% |
| Tor Exit Nodes | 652 | 604 | 51.9% |
| GreenSnow | 518 | 5,369 | 8.8% |
| BinaryDefense | 253 | 1,860 | 12.0% |
| AlienVault OTX | 110 | 47 | 70.1% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 85 | 24,410 | 0.3% |
| Emerging Threats | 10 | 515 | 1.9% |
| Blocklist.de (strongips) | 7 | 316 | 2.2% |
| Blocklist.de (mail) | 2 | 12,622 | 0.0% |
| Blocklist.de (bruteforcelogin) | 1 | 918 | 0.1% |
| Blocklist.de (ssh) | 0 | 7,566 | 0.0% |
| Blocklist.de (apache) | 0 | 9,120 | 0.0% |
| Blocklist.de (bots) | 0 | 2,412 | 0.0% |
| CINS Army | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,537 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,607 |
| Blocklist.de (all) & RTBH (Turkiye) | 12,189 |
| Blocklist.de (all) & Stamparm IPsum | 11,267 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,120 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,557 |
| Stamparm IPsum & AbuseIPDB | 7,061 |
| RTBH (Turkiye) & AbuseIPDB | 6,768 |
| Blocklist.de (ssh) & Stamparm IPsum | 6,642 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 1 | 2026-06-04 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,147 | OK |
| Stamparm IPsum | 35,285 | OK |
| Blocklist.de (all) | 24,495 | OK |
| Blocklist.de (mail) | 12,624 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,120 | OK |
| Blocklist.de (ssh) | 7,566 | OK |
| GreenSnow | 5,887 | OK |
| Blocklist.de (bots) | 2,412 | OK |
| BinaryDefense | 2,113 | OK |
| Spamhaus DROP | 1,641 | OK |
| Tor Exit Nodes | 1,256 | OK |
| Blocklist.de (bruteforcelogin) | 919 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 323 | OK |
| AlienVault OTX | 157 | OK |
| Spamhaus DROPv6 | 93 | OK |
| CINS Army | 0 | EMPTY |
