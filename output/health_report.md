# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-10T06:42:31.822237+00:00
**Duration:** 85.6s
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
| Unique to single source | 56,070 |
| Found in multiple sources | 47,054 |
| Max source overlap | 9 |
| Avg sources per IP | 1.92 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,999 | 25,730 | 52.1% |
| SGB (Turkiye) | 9,777 | 223 | 97.8% |
| Stamparm IPsum | 7,943 | 30,372 | 20.7% |
| CINS Army | 5,626 | 9,374 | 37.5% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| BinaryDefense | 759 | 3,257 | 18.9% |
| Tor Exit Nodes | 629 | 631 | 49.9% |
| AbuseIPDB | 625 | 9,375 | 6.2% |
| Blocklist.de (all) | 434 | 24,354 | 1.8% |
| GreenSnow | 335 | 5,254 | 6.0% |
| AlienVault OTX | 145 | 30 | 82.9% |
| Spamhaus DROPv6 | 86 | 0 | 100.0% |
| Blocklist.de (strongips) | 36 | 300 | 10.7% |
| Emerging Threats | 16 | 509 | 3.0% |
| Blocklist.de (ssh) | 0 | 6,958 | 0.0% |
| Blocklist.de (mail) | 0 | 13,422 | 0.0% |
| Blocklist.de (apache) | 0 | 8,979 | 0.0% |
| Blocklist.de (bots) | 0 | 2,579 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 806 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,886 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,419 |
| Blocklist.de (all) & Stamparm IPsum | 10,018 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,904 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,979 |
| Stamparm IPsum & AbuseIPDB | 8,541 |
| CINS Army & Stamparm IPsum | 8,257 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,099 |
| Blocklist.de (all) & Blocklist.de (ssh) | 6,956 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 49 | 2026-06-10 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 53,729 | OK |
| Stamparm IPsum | 38,315 | OK |
| Blocklist.de (all) | 24,788 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,422 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,979 | OK |
| Blocklist.de (ssh) | 6,958 | OK |
| GreenSnow | 5,589 | OK |
| BinaryDefense | 4,016 | OK |
| Blocklist.de (bots) | 2,579 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 806 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 336 | OK |
| AlienVault OTX | 175 | OK |
| Spamhaus DROPv6 | 86 | OK |
