# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-06T18:39:32.178331+00:00
**Duration:** 50.01s
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
| Unique to single source | 58,833 |
| Found in multiple sources | 46,823 |
| Max source overlap | 9 |
| Avg sources per IP | 1.84 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,067 | 25,984 | 54.5% |
| SGB (Turkiye) | 9,760 | 240 | 97.6% |
| Stamparm IPsum | 7,510 | 30,446 | 19.8% |
| CINS Army | 6,413 | 8,587 | 42.8% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 748 | 9,252 | 7.5% |
| Tor Exit Nodes | 621 | 623 | 49.9% |
| BinaryDefense | 409 | 2,335 | 14.9% |
| GreenSnow | 345 | 4,322 | 7.4% |
| AlienVault OTX | 112 | 30 | 78.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 83 | 22,806 | 0.4% |
| Blocklist.de (strongips) | 18 | 311 | 5.5% |
| Emerging Threats | 11 | 514 | 2.1% |
| Blocklist.de (mail) | 1 | 12,448 | 0.0% |
| Blocklist.de (ssh) | 0 | 4,930 | 0.0% |
| Blocklist.de (apache) | 0 | 8,718 | 0.0% |
| Blocklist.de (bots) | 0 | 3,970 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 521 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,529 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,431 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,718 |
| Blocklist.de (all) & Stamparm IPsum | 8,680 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,536 |
| Stamparm IPsum & AbuseIPDB | 8,369 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,700 |
| RTBH (Turkiye) & AbuseIPDB | 6,936 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,930 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 21 | 2026-06-06 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,051 | OK |
| Stamparm IPsum | 37,956 | OK |
| Blocklist.de (all) | 22,889 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,449 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,718 | OK |
| Blocklist.de (ssh) | 4,930 | OK |
| GreenSnow | 4,667 | OK |
| Blocklist.de (bots) | 3,970 | OK |
| BinaryDefense | 2,744 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,244 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (bruteforcelogin) | 521 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 142 | OK |
| Spamhaus DROPv6 | 93 | OK |
