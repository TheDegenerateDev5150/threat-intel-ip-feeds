# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-14T06:57:11.795053+00:00
**Duration:** 52.35s
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
| Unique to single source | 57,934 |
| Found in multiple sources | 45,039 |
| Max source overlap | 9 |
| Avg sources per IP | 1.91 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,976 | 25,774 | 54.6% |
| SGB (Turkiye) | 9,770 | 230 | 97.7% |
| Stamparm IPsum | 7,037 | 31,190 | 18.4% |
| CINS Army | 5,123 | 9,877 | 34.2% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,189 | 3,794 | 23.9% |
| AbuseIPDB | 887 | 9,113 | 8.9% |
| Tor Exit Nodes | 622 | 638 | 49.4% |
| GreenSnow | 319 | 6,178 | 4.9% |
| AlienVault OTX | 146 | 22 | 86.9% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Emerging Threats | 31 | 497 | 5.9% |
| Blocklist.de (all) | 23 | 21,388 | 0.1% |
| Blocklist.de (strongips) | 20 | 318 | 5.9% |
| Blocklist.de (ssh) | 0 | 5,644 | 0.0% |
| Blocklist.de (mail) | 0 | 12,720 | 0.0% |
| Blocklist.de (apache) | 0 | 9,020 | 0.0% |
| Blocklist.de (bots) | 0 | 1,446 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 830 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,547 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,720 |
| Blocklist.de (all) & Stamparm IPsum | 9,872 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,144 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,020 |
| CINS Army & Stamparm IPsum | 8,966 |
| Stamparm IPsum & AbuseIPDB | 8,444 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,941 |
| CINS Army & RTBH (Turkiye) | 5,807 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 78 | 2026-06-14 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,750 | OK |
| Stamparm IPsum | 38,227 | OK |
| Blocklist.de (all) | 21,411 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,720 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,020 | OK |
| GreenSnow | 6,497 | OK |
| Blocklist.de (ssh) | 5,644 | OK |
| BinaryDefense | 4,983 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,446 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 830 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 338 | OK |
| AlienVault OTX | 168 | OK |
| Spamhaus DROPv6 | 94 | OK |
