# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-15T18:02:21.859150+00:00
**Duration:** 103.77s
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
| Unique to single source | 59,376 |
| Found in multiple sources | 48,803 |
| Max source overlap | 9 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,556 | 26,374 | 53.7% |
| SGB (Turkiye) | 9,785 | 215 | 97.9% |
| Stamparm IPsum | 7,548 | 31,034 | 19.6% |
| CINS Army | 6,175 | 8,825 | 41.2% |
| Spamhaus DROP | 1,695 | 0 | 100.0% |
| BinaryDefense | 1,271 | 3,925 | 24.5% |
| AbuseIPDB | 927 | 9,073 | 9.3% |
| Tor Exit Nodes | 616 | 633 | 49.3% |
| GreenSnow | 448 | 4,917 | 8.4% |
| AlienVault OTX | 155 | 22 | 87.6% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Emerging Threats | 47 | 481 | 8.9% |
| Blocklist.de (all) | 35 | 24,939 | 0.1% |
| Blocklist.de (strongips) | 23 | 321 | 6.7% |
| Blocklist.de (bots) | 1 | 4,148 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,328 | 0.0% |
| Blocklist.de (mail) | 0 | 13,719 | 0.0% |
| Blocklist.de (apache) | 0 | 9,214 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 934 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,742 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,719 |
| Blocklist.de (all) & Stamparm IPsum | 9,763 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,214 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,213 |
| Stamparm IPsum & AbuseIPDB | 8,080 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,682 |
| RTBH (Turkiye) & AbuseIPDB | 6,944 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,328 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 88 | 2026-06-15 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,930 | OK |
| Stamparm IPsum | 38,582 | OK |
| Blocklist.de (all) | 24,974 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,719 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,214 | OK |
| GreenSnow | 5,365 | OK |
| Blocklist.de (ssh) | 5,328 | OK |
| BinaryDefense | 5,196 | OK |
| Blocklist.de (bots) | 4,149 | OK |
| Spamhaus DROP | 1,695 | OK |
| Tor Exit Nodes | 1,249 | OK |
| Blocklist.de (bruteforcelogin) | 934 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 344 | OK |
| AlienVault OTX | 177 | OK |
| Spamhaus DROPv6 | 94 | OK |
