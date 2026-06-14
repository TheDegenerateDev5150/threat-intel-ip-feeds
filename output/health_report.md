# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-14T17:48:03.173574+00:00
**Duration:** 35.45s
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
| Unique to single source | 59,562 |
| Found in multiple sources | 45,684 |
| Max source overlap | 9 |
| Avg sources per IP | 1.87 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,646 | 25,885 | 55.0% |
| SGB (Turkiye) | 9,780 | 220 | 97.8% |
| Stamparm IPsum | 7,205 | 31,022 | 18.8% |
| CINS Army | 6,029 | 8,971 | 40.2% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,181 | 3,802 | 23.7% |
| AbuseIPDB | 700 | 9,300 | 7.0% |
| Tor Exit Nodes | 614 | 643 | 48.8% |
| GreenSnow | 370 | 4,944 | 7.0% |
| AlienVault OTX | 145 | 22 | 86.8% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 34 | 21,584 | 0.2% |
| Emerging Threats | 31 | 497 | 5.9% |
| Blocklist.de (strongips) | 20 | 322 | 5.8% |
| Blocklist.de (mail) | 15 | 12,577 | 0.1% |
| Blocklist.de (apache) | 1 | 9,147 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,515 | 0.0% |
| Blocklist.de (bots) | 0 | 1,780 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 928 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,677 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,571 |
| Blocklist.de (all) & Stamparm IPsum | 9,338 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,146 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,702 |
| Stamparm IPsum & AbuseIPDB | 8,217 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,940 |
| RTBH (Turkiye) & AbuseIPDB | 6,965 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,515 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 82 | 2026-06-14 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,531 | OK |
| Stamparm IPsum | 38,227 | OK |
| Blocklist.de (all) | 21,618 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,592 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,148 | OK |
| Blocklist.de (ssh) | 5,515 | OK |
| GreenSnow | 5,314 | OK |
| BinaryDefense | 4,983 | OK |
| Blocklist.de (bots) | 1,780 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,257 | OK |
| Blocklist.de (bruteforcelogin) | 928 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 167 | OK |
| Spamhaus DROPv6 | 94 | OK |
