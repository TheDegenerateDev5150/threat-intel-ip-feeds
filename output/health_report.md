# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-19T19:09:55.945031+00:00
**Duration:** 191.68s
**Successful:** 18/19

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| CINS Army | ConnectTimeout: HTTPSConnectionPool(host='cinsscore.com', port=443): Max retries exceeded with url: /list/ci-badguys.txt (Caused by ConnectTimeoutError(<HTTPSConnection(host='cinsscore.com', port=443) | 15,000 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 60,986 |
| Found in multiple sources | 45,264 |
| Max source overlap | 9 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 33,112 | 25,656 | 56.3% |
| SGB (Turkiye) | 9,667 | 333 | 96.7% |
| Stamparm IPsum | 6,389 | 30,059 | 17.5% |
| CINS Army | 5,735 | 9,265 | 38.2% |
| BinaryDefense | 1,747 | 4,370 | 28.6% |
| Spamhaus DROP | 1,705 | 0 | 100.0% |
| AbuseIPDB | 1,022 | 8,978 | 10.2% |
| Tor Exit Nodes | 609 | 629 | 49.2% |
| GreenSnow | 457 | 4,436 | 9.3% |
| AlienVault OTX | 316 | 49 | 86.6% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 66 | 21,139 | 0.3% |
| Blocklist.de (strongips) | 53 | 295 | 15.2% |
| Emerging Threats | 14 | 590 | 2.3% |
| Blocklist.de (ssh) | 0 | 4,893 | 0.0% |
| Blocklist.de (mail) | 0 | 12,310 | 0.0% |
| Blocklist.de (apache) | 0 | 9,059 | 0.0% |
| Blocklist.de (bots) | 0 | 2,415 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 910 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,913 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,310 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,059 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,580 |
| Blocklist.de (all) & Stamparm IPsum | 8,500 |
| Stamparm IPsum & AbuseIPDB | 8,203 |
| CINS Army & Stamparm IPsum | 8,130 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,832 |
| CINS Army & RTBH (Turkiye) | 5,209 |

## 3 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| DShield | 2026-05-18 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| CINS Army | 1 | 2026-06-19 | ConnectTimeout: HTTPSConnectionPool(host='cinsscore.com', po |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 58,768 | OK |
| Stamparm IPsum | 36,448 | OK |
| Blocklist.de (all) | 21,205 | OK |
| CINS Army | 15,000 | CACHED |
| Blocklist.de (mail) | 12,310 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | OK |
| Blocklist.de (apache) | 9,059 | OK |
| BinaryDefense | 6,117 | OK |
| Blocklist.de (ssh) | 4,893 | OK |
| GreenSnow | 4,893 | OK |
| Blocklist.de (bots) | 2,415 | OK |
| Spamhaus DROP | 1,705 | OK |
| Tor Exit Nodes | 1,238 | OK |
| Blocklist.de (bruteforcelogin) | 910 | OK |
| Emerging Threats | 604 | OK |
| AlienVault OTX | 365 | OK |
| Blocklist.de (strongips) | 348 | OK |
| Spamhaus DROPv6 | 94 | OK |
