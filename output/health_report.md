# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-06T16:19:51.102428+00:00
**Duration:** 33.15s
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
| Unique to single source | 58,441 |
| Found in multiple sources | 46,798 |
| Max source overlap | 8 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,860 | 26,025 | 54.2% |
| SGB (Turkiye) | 9,761 | 239 | 97.6% |
| Stamparm IPsum | 7,436 | 30,520 | 19.6% |
| CINS Army | 6,321 | 8,679 | 42.1% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 730 | 9,270 | 7.3% |
| Tor Exit Nodes | 622 | 622 | 50.0% |
| BinaryDefense | 414 | 2,330 | 15.1% |
| GreenSnow | 342 | 4,304 | 7.4% |
| AlienVault OTX | 112 | 30 | 78.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 79 | 22,821 | 0.3% |
| Blocklist.de (strongips) | 18 | 311 | 5.5% |
| Emerging Threats | 11 | 514 | 2.1% |
| Blocklist.de (ssh) | 0 | 4,974 | 0.0% |
| Blocklist.de (mail) | 0 | 12,444 | 0.0% |
| Blocklist.de (apache) | 0 | 8,751 | 0.0% |
| Blocklist.de (bots) | 0 | 3,904 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 552 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,500 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,444 |
| Blocklist.de (all) & Stamparm IPsum | 8,810 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,751 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,707 |
| Stamparm IPsum & AbuseIPDB | 8,369 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,796 |
| RTBH (Turkiye) & AbuseIPDB | 6,925 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,974 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 20 | 2026-06-06 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,885 | OK |
| Stamparm IPsum | 37,956 | OK |
| Blocklist.de (all) | 22,900 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,444 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,751 | OK |
| Blocklist.de (ssh) | 4,974 | OK |
| GreenSnow | 4,646 | OK |
| Blocklist.de (bots) | 3,904 | OK |
| BinaryDefense | 2,744 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,244 | OK |
| Blocklist.de (bruteforcelogin) | 552 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 142 | OK |
| Spamhaus DROPv6 | 93 | OK |
