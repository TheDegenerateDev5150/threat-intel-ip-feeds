# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-13T22:19:07.585430+00:00
**Duration:** 35.33s
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
| Unique to single source | 57,536 |
| Found in multiple sources | 45,321 |
| Max source overlap | 9 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,931 | 27,113 | 51.6% |
| SGB (Turkiye) | 9,770 | 230 | 97.7% |
| Stamparm IPsum | 7,538 | 31,185 | 19.5% |
| CINS Army | 6,210 | 8,790 | 41.4% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,129 | 3,635 | 23.7% |
| AbuseIPDB | 991 | 9,009 | 9.9% |
| Tor Exit Nodes | 619 | 642 | 49.1% |
| GreenSnow | 347 | 5,190 | 6.3% |
| AlienVault OTX | 146 | 22 | 86.9% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 35 | 21,389 | 0.2% |
| Emerging Threats | 17 | 511 | 3.2% |
| Blocklist.de (strongips) | 7 | 331 | 2.1% |
| Blocklist.de (mail) | 5 | 12,777 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,696 | 0.0% |
| Blocklist.de (apache) | 0 | 8,927 | 0.0% |
| Blocklist.de (bots) | 0 | 1,503 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 771 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,423 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,775 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,865 |
| Blocklist.de (all) & Stamparm IPsum | 9,584 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,927 |
| Stamparm IPsum & AbuseIPDB | 8,060 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,788 |
| RTBH (Turkiye) & AbuseIPDB | 6,897 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,696 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 76 | 2026-06-13 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,044 | OK |
| Stamparm IPsum | 38,723 | OK |
| Blocklist.de (all) | 21,424 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,782 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,927 | OK |
| Blocklist.de (ssh) | 5,696 | OK |
| GreenSnow | 5,537 | OK |
| BinaryDefense | 4,764 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,503 | OK |
| Tor Exit Nodes | 1,261 | OK |
| Blocklist.de (bruteforcelogin) | 771 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 338 | OK |
| AlienVault OTX | 168 | OK |
| Spamhaus DROPv6 | 94 | OK |
