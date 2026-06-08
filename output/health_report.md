# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-08T23:37:02.147842+00:00
**Duration:** 36.11s
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
| Unique to single source | 56,879 |
| Found in multiple sources | 46,352 |
| Max source overlap | 9 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,836 | 26,973 | 50.8% |
| SGB (Turkiye) | 9,764 | 236 | 97.6% |
| Stamparm IPsum | 8,355 | 29,520 | 22.1% |
| CINS Army | 6,433 | 8,567 | 42.9% |
| Spamhaus DROP | 1,621 | 0 | 100.0% |
| AbuseIPDB | 1,021 | 8,979 | 10.2% |
| Tor Exit Nodes | 659 | 599 | 52.4% |
| BinaryDefense | 540 | 2,817 | 16.1% |
| GreenSnow | 351 | 4,923 | 6.7% |
| AlienVault OTX | 130 | 30 | 81.2% |
| Spamhaus DROPv6 | 86 | 0 | 100.0% |
| Blocklist.de (all) | 34 | 22,746 | 0.1% |
| Blocklist.de (strongips) | 26 | 309 | 7.8% |
| Blocklist.de (bots) | 9 | 3,487 | 0.3% |
| Emerging Threats | 8 | 511 | 1.5% |
| Blocklist.de (ssh) | 4 | 5,000 | 0.1% |
| Blocklist.de (mail) | 2 | 12,808 | 0.0% |
| Blocklist.de (apache) | 0 | 8,905 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 693 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,892 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,805 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,145 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,904 |
| Blocklist.de (all) & Stamparm IPsum | 8,523 |
| Stamparm IPsum & AbuseIPDB | 8,212 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,632 |
| RTBH (Turkiye) & AbuseIPDB | 6,801 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,995 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 40 | 2026-06-08 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 54,809 | OK |
| Stamparm IPsum | 37,875 | OK |
| Blocklist.de (all) | 22,780 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,810 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,905 | OK |
| GreenSnow | 5,274 | OK |
| Blocklist.de (ssh) | 5,004 | OK |
| Blocklist.de (bots) | 3,496 | OK |
| BinaryDefense | 3,357 | OK |
| Spamhaus DROP | 1,621 | OK |
| Tor Exit Nodes | 1,258 | OK |
| Blocklist.de (bruteforcelogin) | 693 | OK |
| Emerging Threats | 519 | OK |
| Blocklist.de (strongips) | 335 | OK |
| AlienVault OTX | 160 | OK |
| Spamhaus DROPv6 | 86 | OK |
