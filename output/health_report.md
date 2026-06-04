# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-04T19:31:12.827695+00:00
**Duration:** 108.15s
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
| Unique to single source | 54,758 |
| Found in multiple sources | 41,936 |
| Max source overlap | 8 |
| Avg sources per IP | 1.86 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,525 | 26,673 | 53.4% |
| SGB (Turkiye) | 9,743 | 257 | 97.4% |
| Stamparm IPsum | 9,382 | 25,903 | 26.6% |
| AbuseIPDB | 1,655 | 8,345 | 16.6% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| GreenSnow | 633 | 4,593 | 12.1% |
| Tor Exit Nodes | 607 | 557 | 52.1% |
| BinaryDefense | 251 | 1,862 | 11.9% |
| AlienVault OTX | 118 | 39 | 75.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 92 | 24,071 | 0.4% |
| Emerging Threats | 10 | 515 | 1.9% |
| Blocklist.de (strongips) | 7 | 317 | 2.2% |
| Blocklist.de (ssh) | 0 | 7,525 | 0.0% |
| Blocklist.de (mail) | 0 | 12,535 | 0.0% |
| Blocklist.de (apache) | 0 | 9,175 | 0.0% |
| Blocklist.de (bots) | 0 | 2,162 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 957 | 0.0% |
| CINS Army | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,666 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,535 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,382 |
| Blocklist.de (all) & Stamparm IPsum | 10,767 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,175 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,515 |
| Stamparm IPsum & AbuseIPDB | 7,061 |
| RTBH (Turkiye) & AbuseIPDB | 6,795 |
| Blocklist.de (ssh) & Stamparm IPsum | 6,432 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 4 | 2026-06-04 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,198 | OK |
| Stamparm IPsum | 35,285 | OK |
| Blocklist.de (all) | 24,163 | OK |
| Blocklist.de (mail) | 12,535 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,175 | OK |
| Blocklist.de (ssh) | 7,525 | OK |
| GreenSnow | 5,226 | OK |
| Blocklist.de (bots) | 2,162 | OK |
| BinaryDefense | 2,113 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,164 | OK |
| Blocklist.de (bruteforcelogin) | 957 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 324 | OK |
| AlienVault OTX | 157 | OK |
| Spamhaus DROPv6 | 93 | OK |
| CINS Army | 0 | EMPTY |
