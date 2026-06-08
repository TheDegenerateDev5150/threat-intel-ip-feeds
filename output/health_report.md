# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-08T16:20:27.854369+00:00
**Duration:** 111.59s
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
| Unique to single source | 58,909 |
| Found in multiple sources | 46,271 |
| Max source overlap | 8 |
| Avg sources per IP | 1.84 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,265 | 25,565 | 54.2% |
| SGB (Turkiye) | 9,761 | 239 | 97.6% |
| Stamparm IPsum | 8,044 | 29,831 | 21.2% |
| CINS Army | 6,280 | 8,720 | 41.9% |
| Spamhaus DROP | 1,621 | 0 | 100.0% |
| AbuseIPDB | 1,007 | 8,993 | 10.1% |
| Tor Exit Nodes | 653 | 606 | 51.9% |
| BinaryDefense | 545 | 2,812 | 16.2% |
| GreenSnow | 369 | 4,182 | 8.1% |
| AlienVault OTX | 130 | 30 | 81.2% |
| Spamhaus DROPv6 | 86 | 0 | 100.0% |
| Blocklist.de (all) | 70 | 22,492 | 0.3% |
| Emerging Threats | 41 | 484 | 7.8% |
| Blocklist.de (strongips) | 20 | 315 | 6.0% |
| Blocklist.de (bots) | 14 | 3,589 | 0.4% |
| Blocklist.de (mail) | 2 | 12,524 | 0.0% |
| Blocklist.de (apache) | 1 | 8,826 | 0.0% |
| Blocklist.de (ssh) | 0 | 4,954 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 638 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,904 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,507 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,826 |
| Blocklist.de (all) & Stamparm IPsum | 8,506 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,311 |
| Stamparm IPsum & AbuseIPDB | 8,212 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,772 |
| RTBH (Turkiye) & AbuseIPDB | 6,714 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,954 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 37 | 2026-06-08 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,830 | OK |
| Stamparm IPsum | 37,875 | OK |
| Blocklist.de (all) | 22,562 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,526 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,827 | OK |
| Blocklist.de (ssh) | 4,954 | OK |
| GreenSnow | 4,551 | OK |
| Blocklist.de (bots) | 3,603 | OK |
| BinaryDefense | 3,357 | OK |
| Spamhaus DROP | 1,621 | OK |
| Tor Exit Nodes | 1,259 | OK |
| Blocklist.de (bruteforcelogin) | 638 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 335 | OK |
| AlienVault OTX | 160 | OK |
| Spamhaus DROPv6 | 86 | OK |
