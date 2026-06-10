# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-10T18:09:52.378311+00:00
**Duration:** 286.18s
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
| Unique to single source | 57,902 |
| Found in multiple sources | 47,934 |
| Max source overlap | 8 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 29,501 | 25,385 | 53.7% |
| SGB (Turkiye) | 9,776 | 224 | 97.8% |
| Stamparm IPsum | 7,935 | 30,380 | 20.7% |
| CINS Army | 6,233 | 8,767 | 41.6% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| BinaryDefense | 752 | 3,264 | 18.7% |
| AbuseIPDB | 674 | 9,326 | 6.7% |
| Tor Exit Nodes | 626 | 634 | 49.7% |
| GreenSnow | 437 | 4,209 | 9.4% |
| AlienVault OTX | 152 | 27 | 84.9% |
| Spamhaus DROPv6 | 86 | 0 | 100.0% |
| Blocklist.de (all) | 35 | 24,908 | 0.1% |
| Blocklist.de (strongips) | 18 | 323 | 5.3% |
| Emerging Threats | 16 | 509 | 3.0% |
| Blocklist.de (mail) | 1 | 13,438 | 0.0% |
| Blocklist.de (ssh) | 0 | 7,698 | 0.0% |
| Blocklist.de (apache) | 0 | 9,118 | 0.0% |
| Blocklist.de (bots) | 0 | 2,286 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 955 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,014 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,438 |
| Blocklist.de (all) & Stamparm IPsum | 9,512 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,142 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,118 |
| Stamparm IPsum & AbuseIPDB | 8,541 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,698 |
| CINS Army & Stamparm IPsum | 7,684 |
| RTBH (Turkiye) & AbuseIPDB | 7,119 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 52 | 2026-06-10 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 54,886 | OK |
| Stamparm IPsum | 38,315 | OK |
| Blocklist.de (all) | 24,943 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,439 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,118 | OK |
| Blocklist.de (ssh) | 7,698 | OK |
| GreenSnow | 4,646 | OK |
| BinaryDefense | 4,016 | OK |
| Blocklist.de (bots) | 2,286 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 955 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 341 | OK |
| AlienVault OTX | 179 | OK |
| Spamhaus DROPv6 | 86 | OK |
