# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-10T14:29:22.867357+00:00
**Duration:** 144.81s
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
| Unique to single source | 57,116 |
| Found in multiple sources | 47,830 |
| Max source overlap | 8 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 29,021 | 25,437 | 53.3% |
| SGB (Turkiye) | 9,776 | 224 | 97.8% |
| Stamparm IPsum | 7,888 | 30,427 | 20.6% |
| CINS Army | 6,014 | 8,986 | 40.1% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| BinaryDefense | 753 | 3,263 | 18.8% |
| AbuseIPDB | 660 | 9,340 | 6.6% |
| Tor Exit Nodes | 625 | 635 | 49.6% |
| GreenSnow | 412 | 4,151 | 9.0% |
| AlienVault OTX | 152 | 27 | 84.9% |
| Spamhaus DROPv6 | 86 | 0 | 100.0% |
| Blocklist.de (all) | 31 | 25,037 | 0.1% |
| Blocklist.de (strongips) | 22 | 314 | 6.5% |
| Emerging Threats | 16 | 509 | 3.0% |
| Blocklist.de (ssh) | 0 | 7,710 | 0.0% |
| Blocklist.de (mail) | 0 | 13,495 | 0.0% |
| Blocklist.de (apache) | 0 | 9,066 | 0.0% |
| Blocklist.de (bots) | 0 | 2,410 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 903 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,971 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,495 |
| Blocklist.de (all) & Stamparm IPsum | 9,738 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,507 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,066 |
| Stamparm IPsum & AbuseIPDB | 8,541 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,941 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,710 |
| RTBH (Turkiye) & AbuseIPDB | 7,112 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 51 | 2026-06-10 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 54,458 | OK |
| Stamparm IPsum | 38,315 | OK |
| Blocklist.de (all) | 25,068 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,495 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,066 | OK |
| Blocklist.de (ssh) | 7,710 | OK |
| GreenSnow | 4,563 | OK |
| BinaryDefense | 4,016 | OK |
| Blocklist.de (bots) | 2,410 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 903 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 336 | OK |
| AlienVault OTX | 179 | OK |
| Spamhaus DROPv6 | 86 | OK |
