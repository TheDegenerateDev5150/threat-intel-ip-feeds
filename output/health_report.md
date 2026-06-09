# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-09T08:41:39.678497+00:00
**Duration:** 36.91s
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
| Unique to single source | 58,758 |
| Found in multiple sources | 45,441 |
| Max source overlap | 9 |
| Avg sources per IP | 1.86 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,007 | 24,904 | 55.5% |
| SGB (Turkiye) | 9,767 | 233 | 97.7% |
| Stamparm IPsum | 7,096 | 29,510 | 19.4% |
| CINS Army | 6,198 | 8,802 | 41.3% |
| Spamhaus DROP | 1,621 | 0 | 100.0% |
| AbuseIPDB | 1,088 | 8,912 | 10.9% |
| BinaryDefense | 720 | 3,022 | 19.2% |
| Tor Exit Nodes | 647 | 609 | 51.5% |
| GreenSnow | 307 | 5,073 | 5.7% |
| AlienVault OTX | 130 | 30 | 81.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 39 | 22,514 | 0.2% |
| Blocklist.de (strongips) | 28 | 307 | 8.4% |
| Emerging Threats | 14 | 505 | 2.7% |
| Blocklist.de (mail) | 2 | 12,789 | 0.0% |
| Blocklist.de (apache) | 1 | 8,869 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,087 | 0.0% |
| Blocklist.de (bots) | 0 | 3,258 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 689 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 20,980 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,785 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,012 |
| Blocklist.de (all) & Stamparm IPsum | 9,002 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,868 |
| Stamparm IPsum & AbuseIPDB | 8,134 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,957 |
| RTBH (Turkiye) & AbuseIPDB | 6,820 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,087 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 42 | 2026-06-09 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,911 | OK |
| Stamparm IPsum | 36,606 | OK |
| Blocklist.de (all) | 22,553 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,791 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,870 | OK |
| GreenSnow | 5,380 | OK |
| Blocklist.de (ssh) | 5,087 | OK |
| BinaryDefense | 3,742 | OK |
| Blocklist.de (bots) | 3,258 | OK |
| Spamhaus DROP | 1,621 | OK |
| Tor Exit Nodes | 1,256 | OK |
| Blocklist.de (bruteforcelogin) | 689 | OK |
| Emerging Threats | 519 | OK |
| Blocklist.de (strongips) | 335 | OK |
| AlienVault OTX | 160 | OK |
| Spamhaus DROPv6 | 93 | OK |
