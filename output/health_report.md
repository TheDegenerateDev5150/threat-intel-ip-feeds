# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-09T12:15:40.051774+00:00
**Duration:** 38.83s
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
| Unique to single source | 59,514 |
| Found in multiple sources | 45,129 |
| Max source overlap | 9 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,460 | 24,855 | 55.9% |
| SGB (Turkiye) | 9,766 | 234 | 97.7% |
| Stamparm IPsum | 7,432 | 29,174 | 20.3% |
| CINS Army | 6,167 | 8,833 | 41.1% |
| Spamhaus DROP | 1,621 | 0 | 100.0% |
| AbuseIPDB | 1,055 | 8,945 | 10.5% |
| BinaryDefense | 720 | 3,022 | 19.2% |
| Tor Exit Nodes | 647 | 609 | 51.5% |
| GreenSnow | 322 | 4,237 | 7.1% |
| AlienVault OTX | 145 | 30 | 82.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 39 | 22,504 | 0.2% |
| Blocklist.de (strongips) | 28 | 308 | 8.3% |
| Emerging Threats | 14 | 505 | 2.7% |
| Blocklist.de (mail) | 5 | 12,927 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,046 | 0.0% |
| Blocklist.de (apache) | 0 | 8,892 | 0.0% |
| Blocklist.de (bots) | 0 | 3,147 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 714 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,096 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,916 |
| Blocklist.de (all) & Stamparm IPsum | 8,909 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,892 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,886 |
| Stamparm IPsum & AbuseIPDB | 8,134 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,936 |
| RTBH (Turkiye) & AbuseIPDB | 6,838 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,046 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 43 | 2026-06-09 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,315 | OK |
| Stamparm IPsum | 36,606 | OK |
| Blocklist.de (all) | 22,543 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,932 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,892 | OK |
| Blocklist.de (ssh) | 5,046 | OK |
| GreenSnow | 4,559 | OK |
| BinaryDefense | 3,742 | OK |
| Blocklist.de (bots) | 3,147 | OK |
| Spamhaus DROP | 1,621 | OK |
| Tor Exit Nodes | 1,256 | OK |
| Blocklist.de (bruteforcelogin) | 714 | OK |
| Emerging Threats | 519 | OK |
| Blocklist.de (strongips) | 336 | OK |
| AlienVault OTX | 175 | OK |
| Spamhaus DROPv6 | 93 | OK |
