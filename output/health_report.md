# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-11T11:48:52.458393+00:00
**Duration:** 67.12s
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
| Unique to single source | 58,764 |
| Found in multiple sources | 47,434 |
| Max source overlap | 9 |
| Avg sources per IP | 1.91 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 29,622 | 27,370 | 52.0% |
| SGB (Turkiye) | 9,769 | 231 | 97.7% |
| Stamparm IPsum | 8,089 | 32,038 | 20.2% |
| CINS Army | 6,027 | 8,973 | 40.2% |
| Spamhaus DROP | 1,702 | 0 | 100.0% |
| AbuseIPDB | 1,329 | 8,671 | 13.3% |
| BinaryDefense | 864 | 3,404 | 20.2% |
| Tor Exit Nodes | 617 | 643 | 49.0% |
| GreenSnow | 396 | 4,023 | 9.0% |
| AlienVault OTX | 151 | 25 | 85.8% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 49 | 24,605 | 0.2% |
| Blocklist.de (strongips) | 18 | 324 | 5.3% |
| Emerging Threats | 17 | 510 | 3.2% |
| Blocklist.de (ssh) | 9 | 7,785 | 0.1% |
| Blocklist.de (bots) | 7 | 1,801 | 0.4% |
| Blocklist.de (mail) | 2 | 13,501 | 0.0% |
| Blocklist.de (bruteforcelogin) | 2 | 961 | 0.2% |
| Blocklist.de (apache) | 0 | 9,135 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,267 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,486 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,467 |
| Blocklist.de (all) & Stamparm IPsum | 11,242 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,135 |
| CINS Army & Stamparm IPsum | 8,050 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,900 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,779 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 6,518 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 57 | 2026-06-11 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,992 | OK |
| Stamparm IPsum | 40,127 | OK |
| Blocklist.de (all) | 24,654 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,503 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,135 | OK |
| Blocklist.de (ssh) | 7,794 | OK |
| GreenSnow | 4,419 | OK |
| BinaryDefense | 4,268 | OK |
| Blocklist.de (bots) | 1,808 | OK |
| Spamhaus DROP | 1,702 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 963 | OK |
| Emerging Threats | 527 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 176 | OK |
| Spamhaus DROPv6 | 94 | OK |
