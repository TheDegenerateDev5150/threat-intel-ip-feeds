# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-13T04:51:50.495438+00:00
**Duration:** 53.54s
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
| Unique to single source | 55,654 |
| Found in multiple sources | 47,149 |
| Max source overlap | 9 |
| Avg sources per IP | 1.97 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 29,437 | 27,360 | 51.8% |
| SGB (Turkiye) | 9,778 | 222 | 97.8% |
| Stamparm IPsum | 7,157 | 31,566 | 18.5% |
| CINS Army | 4,576 | 10,424 | 30.5% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,129 | 3,635 | 23.7% |
| AbuseIPDB | 716 | 9,284 | 7.2% |
| Tor Exit Nodes | 618 | 645 | 48.9% |
| GreenSnow | 254 | 5,788 | 4.2% |
| AlienVault OTX | 155 | 23 | 87.1% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 19 | 24,264 | 0.1% |
| Emerging Threats | 17 | 511 | 3.2% |
| Blocklist.de (strongips) | 7 | 330 | 2.1% |
| Blocklist.de (ssh) | 0 | 8,329 | 0.0% |
| Blocklist.de (mail) | 0 | 12,920 | 0.0% |
| Blocklist.de (apache) | 0 | 8,916 | 0.0% |
| Blocklist.de (bots) | 0 | 1,640 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 780 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,228 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,920 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,764 |
| Blocklist.de (all) & Stamparm IPsum | 11,032 |
| CINS Army & Stamparm IPsum | 9,448 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,916 |
| Stamparm IPsum & AbuseIPDB | 8,419 |
| Blocklist.de (all) & Blocklist.de (ssh) | 8,329 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,101 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 69 | 2026-06-13 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,797 | OK |
| Stamparm IPsum | 38,723 | OK |
| Blocklist.de (all) | 24,283 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,920 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,916 | OK |
| Blocklist.de (ssh) | 8,329 | OK |
| GreenSnow | 6,042 | OK |
| BinaryDefense | 4,764 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,640 | OK |
| Tor Exit Nodes | 1,263 | OK |
| Blocklist.de (bruteforcelogin) | 780 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 337 | OK |
| AlienVault OTX | 178 | OK |
| Spamhaus DROPv6 | 94 | OK |
