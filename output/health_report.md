# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-11T23:56:11.053016+00:00
**Duration:** 104.18s
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
| Unique to single source | 57,774 |
| Found in multiple sources | 47,672 |
| Max source overlap | 8 |
| Avg sources per IP | 1.92 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,648 | 29,191 | 48.6% |
| SGB (Turkiye) | 9,768 | 232 | 97.7% |
| Stamparm IPsum | 8,488 | 31,639 | 21.2% |
| CINS Army | 6,698 | 8,302 | 44.7% |
| Spamhaus DROP | 1,698 | 0 | 100.0% |
| AbuseIPDB | 1,329 | 8,671 | 13.3% |
| BinaryDefense | 874 | 3,394 | 20.5% |
| Tor Exit Nodes | 623 | 639 | 49.4% |
| GreenSnow | 334 | 5,073 | 6.2% |
| AlienVault OTX | 163 | 25 | 86.7% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 29 | 23,978 | 0.1% |
| Blocklist.de (strongips) | 19 | 321 | 5.6% |
| Emerging Threats | 9 | 517 | 1.7% |
| Blocklist.de (ssh) | 0 | 7,661 | 0.0% |
| Blocklist.de (mail) | 0 | 12,985 | 0.0% |
| Blocklist.de (apache) | 0 | 9,139 | 0.0% |
| Blocklist.de (bots) | 0 | 1,770 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 957 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 24,043 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,985 |
| Blocklist.de (all) & RTBH (Turkiye) | 12,175 |
| Blocklist.de (all) & Stamparm IPsum | 10,278 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,139 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,900 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,661 |
| CINS Army & Stamparm IPsum | 7,383 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 6,729 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 61 | 2026-06-11 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,839 | OK |
| Stamparm IPsum | 40,127 | OK |
| Blocklist.de (all) | 24,007 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,985 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,139 | OK |
| Blocklist.de (ssh) | 7,661 | OK |
| GreenSnow | 5,407 | OK |
| BinaryDefense | 4,268 | OK |
| Blocklist.de (bots) | 1,770 | OK |
| Spamhaus DROP | 1,698 | OK |
| Tor Exit Nodes | 1,262 | OK |
| Blocklist.de (bruteforcelogin) | 957 | OK |
| Emerging Threats | 526 | OK |
| Blocklist.de (strongips) | 340 | OK |
| AlienVault OTX | 188 | OK |
| Spamhaus DROPv6 | 94 | OK |
