# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-06T20:35:26.771787+00:00
**Duration:** 35.89s
**Successful:** 17/19

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
| Unique to single source | 59,535 |
| Found in multiple sources | 47,210 |
| Max source overlap | 8 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,838 | 28,184 | 53.0% |
| SGB (Turkiye) | 9,754 | 246 | 97.5% |
| Stamparm IPsum | 7,346 | 30,610 | 19.4% |
| CINS Army | 6,401 | 8,599 | 42.7% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 1,029 | 8,971 | 10.3% |
| Tor Exit Nodes | 618 | 626 | 49.7% |
| BinaryDefense | 409 | 2,335 | 14.9% |
| GreenSnow | 236 | 4,428 | 5.1% |
| AlienVault OTX | 112 | 30 | 78.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 43 | 22,634 | 0.2% |
| Emerging Threats | 11 | 514 | 2.1% |
| Blocklist.de (bots) | 2 | 4,070 | 0.0% |
| Blocklist.de (bruteforcelogin) | 1 | 522 | 0.2% |
| Blocklist.de (ssh) | 0 | 4,660 | 0.0% |
| Blocklist.de (mail) | 0 | 12,494 | 0.0% |
| Blocklist.de (apache) | 0 | 8,721 | 0.0% |
| Blocklist.de (strongips) | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,510 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,494 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,052 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,721 |
| Blocklist.de (all) & Stamparm IPsum | 8,455 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,956 |
| CINS Army & Stamparm IPsum | 7,623 |
| RTBH (Turkiye) & AbuseIPDB | 6,696 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,659 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 22 | 2026-06-06 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 60,022 | OK |
| Stamparm IPsum | 37,956 | OK |
| Blocklist.de (all) | 22,677 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,494 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,721 | OK |
| GreenSnow | 4,664 | OK |
| Blocklist.de (ssh) | 4,660 | OK |
| Blocklist.de (bots) | 4,072 | OK |
| BinaryDefense | 2,744 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,244 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (bruteforcelogin) | 523 | OK |
| AlienVault OTX | 142 | OK |
| Spamhaus DROPv6 | 93 | OK |
| Blocklist.de (strongips) | 0 | EMPTY |
