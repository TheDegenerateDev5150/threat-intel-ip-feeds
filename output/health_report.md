# IP Blacklist Aggregator - Health Report

**Date:** 2026-07-24T17:51:47.704119+00:00
**Duration:** 733.32s
**Successful:** 18/19

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| Emerging Threats | ConnectTimeout: HTTPSConnectionPool(host='rules.emergingthreats.net', port=443): Max retries exceeded with url: /blockrules/compromised-ips.txt (Caused by ConnectTimeoutError(<HTTPSConnection(host='ru | 583 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 62,199 |
| Found in multiple sources | 45,550 |
| Max source overlap | 9 |
| Avg sources per IP | 1.82 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 35,248 | 25,375 | 58.1% |
| SGB (Turkiye) | 9,615 | 385 | 96.2% |
| CINS Army | 7,208 | 7,792 | 48.1% |
| Stamparm IPsum | 5,171 | 26,710 | 16.2% |
| Spamhaus DROP | 1,669 | 0 | 100.0% |
| AbuseIPDB | 918 | 9,082 | 9.2% |
| Tor Exit Nodes | 808 | 573 | 58.5% |
| BinaryDefense | 807 | 3,095 | 20.7% |
| GreenSnow | 364 | 2,904 | 11.1% |
| AlienVault OTX | 227 | 45 | 83.5% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 29 | 24,021 | 0.1% |
| Blocklist.de (strongips) | 27 | 310 | 8.0% |
| Emerging Threats | 14 | 569 | 2.4% |
| Blocklist.de (bots) | 1 | 5,488 | 0.0% |
| Blocklist.de (ssh) | 0 | 4,588 | 0.0% |
| Blocklist.de (mail) | 0 | 12,496 | 0.0% |
| Blocklist.de (apache) | 0 | 9,269 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 1,038 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 20,343 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,496 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,269 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,173 |
| Blocklist.de (all) & Stamparm IPsum | 8,208 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,821 |
| RTBH (Turkiye) & AbuseIPDB | 7,130 |
| CINS Army & Stamparm IPsum | 6,412 |
| Blocklist.de (all) & Blocklist.de (bots) | 5,488 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| Emerging Threats | 1 | 2026-07-24 | ConnectTimeout: HTTPSConnectionPool(host='rules.emergingthre |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 60,623 | OK |
| Stamparm IPsum | 31,881 | OK |
| Blocklist.de (all) | 24,050 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,496 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | OK |
| Blocklist.de (apache) | 9,269 | OK |
| Blocklist.de (bots) | 5,489 | OK |
| Blocklist.de (ssh) | 4,588 | OK |
| BinaryDefense | 3,902 | OK |
| GreenSnow | 3,268 | OK |
| Spamhaus DROP | 1,669 | OK |
| Tor Exit Nodes | 1,381 | OK |
| Blocklist.de (bruteforcelogin) | 1,038 | OK |
| Emerging Threats | 583 | CACHED |
| Blocklist.de (strongips) | 337 | OK |
| AlienVault OTX | 272 | OK |
| Spamhaus DROPv6 | 93 | OK |
