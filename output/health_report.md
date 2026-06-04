# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-04T23:37:29.693878+00:00
**Duration:** 40.5s
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
| Unique to single source | 51,233 |
| Found in multiple sources | 42,426 |
| Max source overlap | 8 |
| Avg sources per IP | 1.92 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 26,927 | 28,567 | 48.5% |
| SGB (Turkiye) | 9,745 | 255 | 97.5% |
| Stamparm IPsum | 9,509 | 25,776 | 26.9% |
| AbuseIPDB | 1,663 | 8,337 | 16.6% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| Tor Exit Nodes | 609 | 557 | 52.2% |
| GreenSnow | 525 | 5,390 | 8.9% |
| BinaryDefense | 253 | 1,860 | 12.0% |
| Blocklist.de (all) | 134 | 24,247 | 0.5% |
| AlienVault OTX | 118 | 39 | 75.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (strongips) | 8 | 320 | 2.4% |
| Emerging Threats | 7 | 523 | 1.3% |
| Blocklist.de (ssh) | 0 | 7,693 | 0.0% |
| Blocklist.de (mail) | 0 | 12,475 | 0.0% |
| Blocklist.de (apache) | 0 | 9,172 | 0.0% |
| Blocklist.de (bots) | 0 | 2,195 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 949 | 0.0% |
| CINS Army | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,272 |
| Blocklist.de (all) & RTBH (Turkiye) | 12,985 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,475 |
| Blocklist.de (all) & Stamparm IPsum | 10,649 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,172 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,693 |
| Stamparm IPsum & AbuseIPDB | 7,061 |
| RTBH (Turkiye) & AbuseIPDB | 6,896 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 6,726 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 6 | 2026-06-04 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,494 | OK |
| Stamparm IPsum | 35,285 | OK |
| Blocklist.de (all) | 24,381 | OK |
| Blocklist.de (mail) | 12,475 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,172 | OK |
| Blocklist.de (ssh) | 7,693 | OK |
| GreenSnow | 5,915 | OK |
| Blocklist.de (bots) | 2,195 | OK |
| BinaryDefense | 2,113 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,166 | OK |
| Blocklist.de (bruteforcelogin) | 949 | OK |
| Emerging Threats | 530 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 157 | OK |
| Spamhaus DROPv6 | 93 | OK |
| CINS Army | 0 | EMPTY |
