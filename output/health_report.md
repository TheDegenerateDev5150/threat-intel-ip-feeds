# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-07T15:01:24.330659+00:00
**Duration:** 42.39s
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
| Unique to single source | 58,230 |
| Found in multiple sources | 47,646 |
| Max source overlap | 9 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,996 | 26,020 | 54.4% |
| SGB (Turkiye) | 9,763 | 237 | 97.6% |
| Stamparm IPsum | 7,451 | 30,217 | 19.8% |
| CINS Army | 6,053 | 8,947 | 40.4% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 673 | 9,327 | 6.7% |
| Tor Exit Nodes | 629 | 628 | 50.0% |
| BinaryDefense | 474 | 2,566 | 15.6% |
| GreenSnow | 256 | 4,010 | 6.0% |
| AlienVault OTX | 104 | 29 | 78.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 40 | 23,612 | 0.2% |
| Emerging Threats | 30 | 495 | 5.7% |
| Blocklist.de (strongips) | 24 | 305 | 7.3% |
| Blocklist.de (apache) | 2 | 8,789 | 0.0% |
| Blocklist.de (ssh) | 0 | 4,859 | 0.0% |
| Blocklist.de (mail) | 0 | 12,623 | 0.0% |
| Blocklist.de (bots) | 0 | 4,734 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 557 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,257 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,623 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,789 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,758 |
| Blocklist.de (all) & Stamparm IPsum | 8,443 |
| Stamparm IPsum & AbuseIPDB | 8,284 |
| CINS Army & Stamparm IPsum | 7,996 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,073 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,859 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 29 | 2026-06-07 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,016 | OK |
| Stamparm IPsum | 37,668 | OK |
| Blocklist.de (all) | 23,652 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,623 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,791 | OK |
| Blocklist.de (ssh) | 4,859 | OK |
| Blocklist.de (bots) | 4,734 | OK |
| GreenSnow | 4,266 | OK |
| BinaryDefense | 3,040 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,257 | OK |
| Blocklist.de (bruteforcelogin) | 557 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 133 | OK |
| Spamhaus DROPv6 | 93 | OK |
