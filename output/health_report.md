# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-10T22:57:10.441752+00:00
**Duration:** 73.04s
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
| Unique to single source | 56,638 |
| Found in multiple sources | 47,639 |
| Max source overlap | 9 |
| Avg sources per IP | 1.92 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 26,889 | 28,900 | 48.2% |
| SGB (Turkiye) | 9,766 | 234 | 97.7% |
| Stamparm IPsum | 8,368 | 29,947 | 21.8% |
| CINS Army | 6,446 | 8,554 | 43.0% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| AbuseIPDB | 1,479 | 8,521 | 14.8% |
| BinaryDefense | 760 | 3,256 | 18.9% |
| Tor Exit Nodes | 625 | 635 | 49.6% |
| GreenSnow | 338 | 4,304 | 7.3% |
| AlienVault OTX | 152 | 27 | 84.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 26 | 24,741 | 0.1% |
| Blocklist.de (strongips) | 19 | 323 | 5.6% |
| Emerging Threats | 9 | 518 | 1.7% |
| Blocklist.de (mail) | 6 | 13,361 | 0.0% |
| Blocklist.de (ssh) | 1 | 7,710 | 0.0% |
| Blocklist.de (bots) | 1 | 2,151 | 0.0% |
| Blocklist.de (apache) | 0 | 9,099 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 938 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,541 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,356 |
| Blocklist.de (all) & RTBH (Turkiye) | 12,662 |
| Blocklist.de (all) & Stamparm IPsum | 9,325 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,096 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,708 |
| CINS Army & Stamparm IPsum | 7,458 |
| Stamparm IPsum & AbuseIPDB | 7,408 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 6,707 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 54 | 2026-06-10 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,789 | OK |
| Stamparm IPsum | 38,315 | OK |
| Blocklist.de (all) | 24,767 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,367 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,099 | OK |
| Blocklist.de (ssh) | 7,711 | OK |
| GreenSnow | 4,642 | OK |
| BinaryDefense | 4,016 | OK |
| Blocklist.de (bots) | 2,152 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 938 | OK |
| Emerging Threats | 527 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 179 | OK |
| Spamhaus DROPv6 | 93 | OK |
