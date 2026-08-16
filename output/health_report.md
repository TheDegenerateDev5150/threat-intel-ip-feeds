# IP Blacklist Aggregator - Health Report

**Date:** 2026-08-16T13:00:56.143563+00:00
**Duration:** 59.45s
**Successful:** 18/19

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| GreenSnow | HttpError: HTTP 503: <!DOCTYPE html>
<html style="height:100%">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
<title> 503 Service Unavailable
</title | 2,500 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 65,999 |
| Found in multiple sources | 42,151 |
| Max source overlap | 9 |
| Avg sources per IP | 1.72 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 38,365 | 22,535 | 63.0% |
| SGB (Turkiye) | 9,552 | 448 | 95.5% |
| CINS Army | 7,074 | 7,926 | 47.2% |
| Stamparm IPsum | 6,533 | 24,077 | 21.3% |
| Spamhaus DROP | 1,686 | 0 | 100.0% |
| AbuseIPDB | 1,137 | 8,863 | 11.4% |
| Tor Exit Nodes | 849 | 648 | 56.7% |
| GreenSnow | 273 | 2,227 | 10.9% |
| AlienVault OTX | 255 | 49 | 83.9% |
| BinaryDefense | 107 | 757 | 12.4% |
| Spamhaus DROPv6 | 91 | 0 | 100.0% |
| Blocklist.de (strongips) | 29 | 321 | 8.3% |
| Emerging Threats | 27 | 524 | 4.9% |
| Blocklist.de (all) | 20 | 21,520 | 0.1% |
| Blocklist.de (ssh) | 1 | 4,963 | 0.0% |
| Blocklist.de (mail) | 0 | 12,344 | 0.0% |
| Blocklist.de (apache) | 0 | 8,924 | 0.0% |
| Blocklist.de (bots) | 0 | 3,153 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 657 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 16,914 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,334 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,924 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,113 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,317 |
| CINS Army & Stamparm IPsum | 7,066 |
| Blocklist.de (all) & Stamparm IPsum | 6,840 |
| RTBH (Turkiye) & AbuseIPDB | 6,352 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,958 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| GreenSnow | 1 | 2026-08-16 | HttpError: HTTP 503: <!DOCTYPE html>
<html style="height:100 |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 60,900 | OK |
| Stamparm IPsum | 30,610 | OK |
| Blocklist.de (all) | 21,540 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,344 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | OK |
| Blocklist.de (apache) | 8,924 | OK |
| Blocklist.de (ssh) | 4,964 | OK |
| Blocklist.de (bots) | 3,153 | OK |
| GreenSnow | 2,500 | CACHED |
| Spamhaus DROP | 1,686 | OK |
| Tor Exit Nodes | 1,497 | OK |
| BinaryDefense | 864 | OK |
| Blocklist.de (bruteforcelogin) | 657 | OK |
| Emerging Threats | 551 | OK |
| Blocklist.de (strongips) | 350 | OK |
| AlienVault OTX | 304 | OK |
| Spamhaus DROPv6 | 91 | OK |
