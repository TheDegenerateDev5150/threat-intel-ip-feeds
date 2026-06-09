# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-09T15:29:24.825296+00:00
**Duration:** 36.84s
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
| Unique to single source | 60,018 |
| Found in multiple sources | 45,061 |
| Max source overlap | 9 |
| Avg sources per IP | 1.84 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,751 | 24,800 | 56.1% |
| SGB (Turkiye) | 9,768 | 232 | 97.7% |
| Stamparm IPsum | 7,598 | 29,008 | 20.8% |
| CINS Army | 6,391 | 8,609 | 42.6% |
| Spamhaus DROP | 1,643 | 0 | 100.0% |
| AbuseIPDB | 818 | 9,182 | 8.2% |
| BinaryDefense | 712 | 3,030 | 19.0% |
| Tor Exit Nodes | 649 | 608 | 51.6% |
| GreenSnow | 360 | 4,288 | 7.7% |
| AlienVault OTX | 145 | 30 | 82.9% |
| Spamhaus DROPv6 | 86 | 0 | 100.0% |
| Blocklist.de (all) | 44 | 22,503 | 0.2% |
| Blocklist.de (strongips) | 28 | 309 | 8.3% |
| Emerging Threats | 14 | 505 | 2.7% |
| Blocklist.de (bots) | 11 | 3,070 | 0.4% |
| Blocklist.de (ssh) | 0 | 5,105 | 0.0% |
| Blocklist.de (mail) | 0 | 12,964 | 0.0% |
| Blocklist.de (apache) | 0 | 8,890 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 714 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,142 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,964 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,886 |
| Blocklist.de (all) & Stamparm IPsum | 8,786 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,757 |
| Stamparm IPsum & AbuseIPDB | 8,206 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,724 |
| RTBH (Turkiye) & AbuseIPDB | 6,975 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,105 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 44 | 2026-06-09 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,551 | OK |
| Stamparm IPsum | 36,606 | OK |
| Blocklist.de (all) | 22,547 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,964 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,890 | OK |
| Blocklist.de (ssh) | 5,105 | OK |
| GreenSnow | 4,648 | OK |
| BinaryDefense | 3,742 | OK |
| Blocklist.de (bots) | 3,081 | OK |
| Spamhaus DROP | 1,643 | OK |
| Tor Exit Nodes | 1,257 | OK |
| Blocklist.de (bruteforcelogin) | 714 | OK |
| Emerging Threats | 519 | OK |
| Blocklist.de (strongips) | 337 | OK |
| AlienVault OTX | 175 | OK |
| Spamhaus DROPv6 | 86 | OK |
