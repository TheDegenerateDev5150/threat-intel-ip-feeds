# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-06T10:22:14.830354+00:00
**Duration:** 68.42s
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
| Unique to single source | 58,073 |
| Found in multiple sources | 46,316 |
| Max source overlap | 9 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,547 | 25,926 | 54.1% |
| SGB (Turkiye) | 9,761 | 239 | 97.6% |
| Stamparm IPsum | 7,359 | 30,597 | 19.4% |
| CINS Army | 6,404 | 8,596 | 42.7% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 753 | 9,247 | 7.5% |
| Tor Exit Nodes | 623 | 621 | 50.1% |
| BinaryDefense | 414 | 2,330 | 15.1% |
| GreenSnow | 261 | 3,225 | 7.5% |
| AlienVault OTX | 113 | 30 | 79.0% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 73 | 22,795 | 0.3% |
| Blocklist.de (strongips) | 19 | 310 | 5.8% |
| Emerging Threats | 11 | 514 | 2.1% |
| Blocklist.de (ssh) | 0 | 4,992 | 0.0% |
| Blocklist.de (mail) | 0 | 12,516 | 0.0% |
| Blocklist.de (apache) | 0 | 8,888 | 0.0% |
| Blocklist.de (bots) | 0 | 3,632 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 665 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,429 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,516 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,145 |
| Blocklist.de (all) & Stamparm IPsum | 9,086 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,888 |
| Stamparm IPsum & AbuseIPDB | 8,369 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,808 |
| RTBH (Turkiye) & AbuseIPDB | 6,889 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,992 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 17 | 2026-06-06 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,473 | OK |
| Stamparm IPsum | 37,956 | OK |
| Blocklist.de (all) | 22,868 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,516 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,888 | OK |
| Blocklist.de (ssh) | 4,992 | OK |
| Blocklist.de (bots) | 3,632 | OK |
| GreenSnow | 3,486 | OK |
| BinaryDefense | 2,744 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,244 | OK |
| Blocklist.de (bruteforcelogin) | 665 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 143 | OK |
| Spamhaus DROPv6 | 93 | OK |
