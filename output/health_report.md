# IP Blacklist Aggregator - Health Report

**Date:** 2026-05-13T09:21:22.198443+00:00
**Duration:** 193.82s
**Successful:** 19/20

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| SGB (Turkiye) | ConnectTimeout: HTTPSConnectionPool(host='siberguvenlik.gov.tr', port=443): Max retries exceeded with url: /api/address/index?type=ip&page=1&per-page=10000 (Caused by ConnectTimeoutError(<HTTPSConnect | No cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 129,305 |
| Found in multiple sources | 47,951 |
| Max source overlap | 9 |
| Avg sources per IP | 1.57 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| DShield | 92,879 | 15,605 | 85.6% |
| RTBH (Turkiye) | 22,523 | 17,231 | 56.7% |
| Stamparm IPsum | 5,912 | 31,185 | 15.9% |
| CINS Army | 3,542 | 11,458 | 23.6% |
| Spamhaus DROP | 1,611 | 0 | 100.0% |
| GreenSnow | 930 | 4,206 | 18.1% |
| BinaryDefense | 802 | 1,585 | 33.6% |
| AbuseIPDB | 639 | 9,361 | 6.4% |
| AlienVault OTX | 208 | 2 | 99.0% |
| Blocklist.de (all) | 111 | 23,878 | 0.5% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (strongips) | 51 | 277 | 15.5% |
| Emerging Threats | 3 | 419 | 0.7% |
| Blocklist.de (ssh) | 0 | 5,033 | 0.0% |
| Blocklist.de (mail) | 0 | 14,057 | 0.0% |
| Blocklist.de (apache) | 0 | 9,460 | 0.0% |
| Blocklist.de (bots) | 0 | 2,885 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 1,258 | 0.0% |
| Tor Exit Nodes | 0 | 1,353 | 0.0% |
| SGB (Turkiye) | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 15,490 |
| DShield & Stamparm IPsum | 14,093 |
| Blocklist.de (all) & Blocklist.de (mail) | 14,057 |
| CINS Army & Stamparm IPsum | 10,400 |
| Blocklist.de (all) & Stamparm IPsum | 9,837 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,460 |
| Stamparm IPsum & AbuseIPDB | 8,321 |
| DShield & RTBH (Turkiye) | 8,010 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & RTBH (Turkiye) | 5,727 |

## 1 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| SGB (Turkiye) | Never | 7 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 7 | 2026-05-13 | ConnectTimeout: HTTPSConnectionPool(host='siberguvenlik.gov. |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| DShield | 108,484 | OK |
| RTBH (Turkiye) | 39,754 | OK |
| Stamparm IPsum | 37,097 | OK |
| Blocklist.de (all) | 23,989 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 14,057 | OK |
| AbuseIPDB | 10,000 | OK |
| Blocklist.de (apache) | 9,460 | OK |
| GreenSnow | 5,136 | OK |
| Blocklist.de (ssh) | 5,033 | OK |
| Blocklist.de (bots) | 2,885 | OK |
| BinaryDefense | 2,387 | OK |
| Spamhaus DROP | 1,611 | OK |
| Tor Exit Nodes | 1,353 | OK |
| Blocklist.de (bruteforcelogin) | 1,258 | OK |
| Emerging Threats | 422 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 210 | OK |
| Spamhaus DROPv6 | 94 | OK |
| SGB (Turkiye) | 0 | FAILED |
