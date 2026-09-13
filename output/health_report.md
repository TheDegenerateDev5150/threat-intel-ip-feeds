# IP Blacklist Aggregator - Health Report

**Date:** 2026-09-13T01:01:03.585053+00:00
**Duration:** 95.55s
**Successful:** 18/19

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| GreenSnow | HttpError: HTTP 503: <!DOCTYPE html>
<html style="height:100%">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
<title> 503 Service Unavailable
</title | 4,333 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 72,276 |
| Found in multiple sources | 48,977 |
| Max source overlap | 9 |
| Avg sources per IP | 1.81 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 44,029 | 30,352 | 59.2% |
| SGB (Turkiye) | 9,540 | 460 | 95.4% |
| CINS Army | 7,307 | 7,693 | 48.7% |
| Stamparm IPsum | 6,330 | 26,656 | 19.2% |
| Spamhaus DROP | 1,722 | 0 | 100.0% |
| AbuseIPDB | 1,499 | 8,501 | 15.0% |
| BinaryDefense | 592 | 2,781 | 17.6% |
| Tor Exit Nodes | 568 | 760 | 42.8% |
| GreenSnow | 386 | 3,947 | 8.9% |
| AlienVault OTX | 181 | 50 | 78.4% |
| Spamhaus DROPv6 | 92 | 0 | 100.0% |
| Emerging Threats | 13 | 597 | 2.1% |
| Blocklist.de (all) | 8 | 27,910 | 0.0% |
| Blocklist.de (mail) | 3 | 12,513 | 0.0% |
| Blocklist.de (strongips) | 3 | 356 | 0.8% |
| Blocklist.de (ssh) | 2 | 11,348 | 0.0% |
| Blocklist.de (bots) | 1 | 2,394 | 0.0% |
| Blocklist.de (apache) | 0 | 9,548 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 944 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 19,585 |
| Blocklist.de (all) & RTBH (Turkiye) | 15,692 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,510 |
| Blocklist.de (all) & Blocklist.de (ssh) | 11,342 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 10,148 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,548 |
| Blocklist.de (all) & Stamparm IPsum | 8,786 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 6,860 |
| CINS Army & Stamparm IPsum | 6,635 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| GreenSnow | 1 | 2026-09-13 | HttpError: HTTP 503: <!DOCTYPE html>
<html style="height:100 |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 74,381 | OK |
| Stamparm IPsum | 32,986 | OK |
| Blocklist.de (all) | 27,918 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,516 | OK |
| Blocklist.de (ssh) | 11,350 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | OK |
| Blocklist.de (apache) | 9,548 | OK |
| GreenSnow | 4,333 | CACHED |
| BinaryDefense | 3,373 | OK |
| Blocklist.de (bots) | 2,395 | OK |
| Spamhaus DROP | 1,722 | OK |
| Tor Exit Nodes | 1,328 | OK |
| Blocklist.de (bruteforcelogin) | 944 | OK |
| Emerging Threats | 610 | OK |
| Blocklist.de (strongips) | 359 | OK |
| AlienVault OTX | 231 | OK |
| Spamhaus DROPv6 | 92 | OK |
