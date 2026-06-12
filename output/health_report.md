# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-12T19:22:02.859797+00:00
**Duration:** 54.24s
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
| Unique to single source | 59,920 |
| Found in multiple sources | 46,925 |
| Max source overlap | 8 |
| Avg sources per IP | 1.89 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,863 | 27,058 | 54.1% |
| SGB (Turkiye) | 9,776 | 224 | 97.8% |
| Stamparm IPsum | 7,248 | 30,276 | 19.3% |
| CINS Army | 6,056 | 8,944 | 40.4% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,004 | 3,503 | 22.3% |
| AbuseIPDB | 802 | 9,198 | 8.0% |
| Tor Exit Nodes | 659 | 605 | 52.1% |
| GreenSnow | 493 | 4,521 | 9.8% |
| AlienVault OTX | 155 | 23 | 87.1% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 46 | 24,191 | 0.2% |
| Emerging Threats | 13 | 513 | 2.5% |
| Blocklist.de (strongips) | 12 | 330 | 3.5% |
| Blocklist.de (bruteforcelogin) | 2 | 742 | 0.3% |
| Blocklist.de (ssh) | 0 | 8,071 | 0.0% |
| Blocklist.de (mail) | 0 | 12,994 | 0.0% |
| Blocklist.de (apache) | 0 | 8,922 | 0.0% |
| Blocklist.de (bots) | 0 | 1,753 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,410 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,994 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,820 |
| Blocklist.de (all) & Stamparm IPsum | 9,860 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,922 |
| Stamparm IPsum & AbuseIPDB | 8,281 |
| Blocklist.de (all) & Blocklist.de (ssh) | 8,071 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,875 |
| RTBH (Turkiye) & AbuseIPDB | 6,956 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 66 | 2026-06-12 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 58,921 | OK |
| Stamparm IPsum | 37,524 | OK |
| Blocklist.de (all) | 24,237 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,994 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,922 | OK |
| Blocklist.de (ssh) | 8,071 | OK |
| GreenSnow | 5,014 | OK |
| BinaryDefense | 4,507 | OK |
| Blocklist.de (bots) | 1,753 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,264 | OK |
| Blocklist.de (bruteforcelogin) | 744 | OK |
| Emerging Threats | 526 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 178 | OK |
| Spamhaus DROPv6 | 94 | OK |
