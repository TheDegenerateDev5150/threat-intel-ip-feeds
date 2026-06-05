# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-05T18:09:53.873393+00:00
**Duration:** 86.37s
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
| Unique to single source | 58,946 |
| Found in multiple sources | 44,005 |
| Max source overlap | 9 |
| Avg sources per IP | 1.84 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,926 | 26,408 | 53.9% |
| SGB (Turkiye) | 9,751 | 249 | 97.5% |
| CINS Army | 7,393 | 7,607 | 49.3% |
| Stamparm IPsum | 6,324 | 28,087 | 18.4% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 1,117 | 8,883 | 11.2% |
| Tor Exit Nodes | 687 | 566 | 54.8% |
| GreenSnow | 403 | 4,659 | 8.0% |
| BinaryDefense | 335 | 2,061 | 14.0% |
| Blocklist.de (all) | 131 | 21,321 | 0.6% |
| AlienVault OTX | 115 | 39 | 74.7% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 22 | 508 | 4.2% |
| Blocklist.de (strongips) | 7 | 320 | 2.1% |
| Blocklist.de (ssh) | 0 | 5,117 | 0.0% |
| Blocklist.de (mail) | 0 | 12,239 | 0.0% |
| Blocklist.de (apache) | 0 | 8,943 | 0.0% |
| Blocklist.de (bots) | 0 | 2,287 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 788 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,005 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,239 |
| Blocklist.de (all) & Stamparm IPsum | 8,961 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,943 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,819 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,267 |
| RTBH (Turkiye) & AbuseIPDB | 6,944 |
| CINS Army & Stamparm IPsum | 5,650 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,117 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 11 | 2026-06-05 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,334 | OK |
| Stamparm IPsum | 34,411 | OK |
| Blocklist.de (all) | 21,452 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,239 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,943 | OK |
| Blocklist.de (ssh) | 5,117 | OK |
| GreenSnow | 5,062 | OK |
| BinaryDefense | 2,396 | OK |
| Blocklist.de (bots) | 2,287 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,253 | OK |
| Blocklist.de (bruteforcelogin) | 788 | OK |
| Emerging Threats | 530 | OK |
| Blocklist.de (strongips) | 327 | OK |
| AlienVault OTX | 154 | OK |
| Spamhaus DROPv6 | 93 | OK |
