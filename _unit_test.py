import base64
import json

import tester

# --- vless h2 ---
o = tester.link_outbound(
    'vless://uuid@h2.example.com:443?security=tls&type=h2&host=h2.example.com&path=%2Fh2&sni=h2.example.com#t')
assert o['streamSettings']['network'] == 'http', o['streamSettings']
assert o['streamSettings']['httpSettings'] == {'path': '/h2', 'host': ['h2.example.com']}, \
    o['streamSettings']['httpSettings']
print('vless h2 OK')

# --- vmess h2 ---
vm = base64.b64encode(json.dumps({'add': 'vh2.com', 'port': '443', 'id': 'x',
                                  'net': 'h2', 'path': '/vm', 'host': 'vh2.com',
                                  'tls': 'tls', 'ps': 't'}).encode()).decode()
o2 = tester.link_outbound('vmess://' + vm)
assert o2['streamSettings']['network'] == 'http', o2['streamSettings']
assert o2['streamSettings']['httpSettings']['path'] == '/vm'
print('vmess h2 OK')

# --- trojan h2 ---
o3 = tester.link_outbound('trojan://pw@th2.com:443?security=tls&sni=th2.com&type=h2&host=th2.com&path=%2Ft#t')
assert o3['streamSettings']['network'] == 'http', o3['streamSettings']
assert 'host' in o3['streamSettings']['httpSettings']
print('trojan h2 OK')

# --- ss fully removed ---
assert 'ss://' not in tester.SCHEMES
assert tester.link_outbound('ss://YWVzLTI1Ni1nY206cGFzcw==@1.2.3.4:443#x') is None
links = tester.content_to_links('ss://abc@1.2.3.4:443#x\nvless://u@2.3.4.5:443?security=tls#y')
assert links == ['vless://u@2.3.4.5:443?security=tls#y'], links
print('ss removed OK')

# --- ws/grpc/tls still fine ---
o4 = tester.link_outbound('vless://u@w.com:443?security=tls&type=ws&host=w.com&path=%2Fws#z')
assert o4['streamSettings']['wsSettings']['path'] == '/ws'
o5 = tester.link_outbound('vless://u@g.com:443?security=reality&type=grpc&serviceName=svc&pbk=PK&sid=1&fp=chrome&sni=g.com#z')
assert o5['streamSettings']['grpcSettings']['serviceName'] == 'svc'
print('ws/grpc OK')

# --- fingerprint gate ---
assert tester.link_has_fp('vless://u@a.com:443?security=reality&pbk=X&sni=a.com#r') is True
assert tester.link_has_fp('vless://u@a.com:443?security=tls&fp=chrome&sni=a.com#t') is True
assert tester.link_has_fp('vless://u@a.com:443?security=tls&sni=a.com#t') is False
assert tester.link_has_fp('vless://u@a.com:443?type=tcp#plain') is False
assert tester.link_has_fp('trojan://pw@a.com:443?security=tls&fp=firefox&sni=a.com#t') is True
assert tester.link_has_fp('trojan://pw@a.com:443?security=tls&sni=a.com#t') is False
vm_fp = base64.b64encode(json.dumps({'add': 'a.com', 'port': '443', 'id': 'x',
                                     'net': 'tcp', 'tls': 'tls', 'fp': 'chrome',
                                     'ps': 't'}).encode()).decode()
vm_nofp = base64.b64encode(json.dumps({'add': 'a.com', 'port': '443', 'id': 'x',
                                       'net': 'tcp', 'tls': 'tls',
                                       'ps': 't'}).encode()).decode()
assert tester.link_has_fp('vmess://' + vm_fp) is True
assert tester.link_has_fp('vmess://' + vm_nofp) is False
# faithful TLS outbound: no fp in link -> no fingerprint injected
o6 = tester.link_outbound('vless://u@t.com:443?security=tls&sni=t.com#z')
assert 'fingerprint' not in o6['streamSettings']['tlsSettings']
o7 = tester.link_outbound('vless://u@t.com:443?security=tls&fp=safari&sni=t.com#z')
assert o7['streamSettings']['tlsSettings']['fingerprint'] == 'safari'
o8 = tester.link_outbound('vless://u@r.com:443?security=reality&pbk=K&sni=r.com#z')
assert o8['streamSettings']['realitySettings']['fingerprint'] == 'chrome'
print('fp gate OK')

# --- fp_priority + deduplicate_by_fp_priority ---
# chrome wins over firefox / safari / unknown
chrome_link  = 'vless://uuid@srv.com:443?security=tls&fp=chrome&sni=srv.com#c'
firefox_link = 'vless://uuid@srv.com:443?security=tls&fp=firefox&sni=srv.com#f'
safari_link  = 'vless://uuid@srv.com:443?security=tls&fp=safari&sni=srv.com#s'
unknown_link = 'vless://uuid@srv.com:443?security=tls&fp=randomized&sni=srv.com#r'
nofp_link    = 'vless://uuid@srv.com:443?security=tls&sni=srv.com#n'

assert tester.fp_priority(chrome_link)  == (0, 1),  tester.fp_priority(chrome_link)
assert tester.fp_priority(firefox_link) == (1, 1),  tester.fp_priority(firefox_link)
assert tester.fp_priority(safari_link)  == (2, 1),  tester.fp_priority(safari_link)
assert tester.fp_priority(unknown_link) > (2, 1),   tester.fp_priority(unknown_link)
assert tester.fp_priority(nofp_link)    > (2, 1),   tester.fp_priority(nofp_link)

# Reality fp priority: chrome (0, 0) beats firefox (1, 0) and safari (2, 0)
reality_link = 'vless://uuid@srv.com:443?security=reality&pbk=PK&sni=srv.com&fp=chrome#re'
reality_ff   = 'vless://uuid@srv.com:443?security=reality&pbk=PK&sni=srv.com&fp=firefox#rf'
reality_sf   = 'vless://uuid@srv.com:443?security=reality&pbk=PK&sni=srv.com&fp=safari#rs'
assert tester.fp_priority(reality_link) == (0, 0), tester.fp_priority(reality_link)
assert tester.fp_priority(reality_ff)   == (1, 0), tester.fp_priority(reality_ff)
assert tester.fp_priority(reality_sf)   == (2, 0), tester.fp_priority(reality_sf)
assert tester.fp_priority(reality_link) < tester.fp_priority(reality_ff)
assert tester.fp_priority(reality_ff) < tester.fp_priority(reality_sf)

# base_signature strips fp= and normalizes params
assert tester.base_signature(chrome_link) == tester.base_signature(firefox_link)
assert tester.base_signature(chrome_link) == tester.base_signature(safari_link)
assert tester.base_signature(chrome_link) == tester.base_signature(nofp_link)

# Different server → different base_signature
other_link = 'vless://uuid@other.com:443?security=tls&fp=firefox&sni=other.com#o'
assert tester.base_signature(chrome_link) != tester.base_signature(other_link)

# security=reality vs security=tls → different configs (correctly separate)
plain_tls = 'vless://uuid@srv.com:443?security=tls&fp=chrome&sni=srv.com#c'
assert tester.base_signature(plain_tls) != tester.base_signature(reality_link)

# Reality IP vs Domain equivalence test (same uuid + port + pbk = same server)
r_user_ip = 'vless://ad3f4a0a-a89f-498e-9869-a93c8fa185b1@91.107.179.0:10105?flow=xtls-rprx-vision&type=tcp&headerType=none&security=reality&fp=firefox&sni=play.google.com&pbk=PFC3JN1er1JE2vAemwRhNjewz8I4NUWP4XHf2Dza4Es&sid=12e321badd07906e#name1'
r_user_domain = 'vless://ad3f4a0a-a89f-498e-9869-a93c8fa185b1@germany1.xorsand.eu:10105?flow=xtls-rprx-vision&type=tcp&headerType=none&security=reality&fp=chrome&sni=play.google.com&pbk=PFC3JN1er1JE2vAemwRhNjewz8I4NUWP4XHf2Dza4Es&sid=12e321badd07906e#name2'
assert tester.base_signature(r_user_ip) == tester.base_signature(r_user_domain)

def _item(link): return {'raw': link, 'name': 'test'}

# chrome wins regardless of insertion order
result = tester.deduplicate_by_fp_priority([_item(firefox_link), _item(chrome_link)])
assert len(result) == 1
assert result[0]['raw'] == chrome_link, result[0]['raw']

result2 = tester.deduplicate_by_fp_priority([_item(safari_link), _item(firefox_link)])
assert len(result2) == 1
assert result2[0]['raw'] == firefox_link, result2[0]['raw']

# In reality group: chrome beats firefox even if firefox is inserted first
result3 = tester.deduplicate_by_fp_priority([_item(reality_ff), _item(reality_link)])
assert len(result3) == 1
assert result3[0]['raw'] == reality_link, result3[0]['raw']

# Testing exact user case: IP with firefox vs Domain with chrome -> Domain with chrome wins!
result_user = tester.deduplicate_by_fp_priority([_item(r_user_ip), _item(r_user_domain)])
assert len(result_user) == 1
assert result_user[0]['raw'] == r_user_domain, result_user[0]['raw']

# Reverse order test: Domain with chrome first, IP with firefox second -> Domain with chrome wins!
result_user_rev = tester.deduplicate_by_fp_priority([_item(r_user_domain), _item(r_user_ip)])
assert len(result_user_rev) == 1
assert result_user_rev[0]['raw'] == r_user_domain, result_user_rev[0]['raw']

# different servers → both kept
result4 = tester.deduplicate_by_fp_priority([_item(chrome_link), _item(other_link)])
assert len(result4) == 2

# insertion order of winners is preserved
mixed = [_item(other_link), _item(safari_link), _item(firefox_link)]
result5 = tester.deduplicate_by_fp_priority(mixed)
assert len(result5) == 2
assert result5[0]['raw'] == other_link    # other_link comes first (different sig)
assert result5[1]['raw'] == firefox_link  # firefox beats safari

print('fp_priority / deduplicate_by_fp_priority OK')

# --- dedup_signature: vmess fp-aware pass-1 ---
import base64 as _b64, json as _json

def _vmess(fp=None, add='s.com', port='443', uid='uid'):
    o = {'add': add, 'port': port, 'id': uid, 'tls': 'tls', 'ps': 'n'}
    if fp: o['fp'] = fp
    return 'vmess://' + _b64.b64encode(_json.dumps(o).encode()).decode()

# Same server+port+id, different fp -> pass-1 keeps BOTH (fp in signature)
sig_cr = tester.dedup_signature(_vmess('chrome'))
sig_ff = tester.dedup_signature(_vmess('firefox'))
assert sig_cr != sig_ff, f'vmess chrome/firefox should differ in pass-1: {sig_cr}'

# Same server+port+id, same fp -> pass-1 deduplicates (identical)
sig_cr2 = tester.dedup_signature(_vmess('chrome'))
assert sig_cr == sig_cr2

# No-fp vmess treated consistently (empty fp= in key)
sig_nofp = tester.dedup_signature(_vmess())
assert sig_nofp != sig_cr  # nofp differs from chrome
assert sig_nofp == tester.dedup_signature(_vmess())  # two nofp same server -> same sig

# pass-2 (base_signature) groups chrome+firefox+nofp all together for vmess
assert tester.base_signature(_vmess('chrome'))  == tester.base_signature(_vmess('firefox'))
assert tester.base_signature(_vmess('chrome'))  == tester.base_signature(_vmess())

# End-to-end: firefox-first vmess -> chrome should still win after both passes
items_vmess = [
    {'raw': _vmess('firefox'), 'name': 'ff'},
    {'raw': _vmess('chrome'),  'name': 'cr'},
]
# Simulate pass-1
seen1, after_p1 = {}, []
for it in items_vmess:
    sig = tester.dedup_signature(it['raw'])
    if sig not in seen1:
        seen1[sig] = True
        after_p1.append(it)
assert len(after_p1) == 2, 'pass-1 should keep both vmess (different fp sigs)'
# pass-2
after_p2 = tester.deduplicate_by_fp_priority(after_p1)
assert len(after_p2) == 1
winner_fp = _json.loads(tester.b64_decode(after_p2[0]['raw'][8:]))['fp']
assert winner_fp == 'chrome', f'chrome should win, got {winner_fp}'
print('vmess fp-aware dedup_signature OK')

# --- Gemini validation & Google GeoIP extraction ---
import re

for bad_c in ("RU", "IR", "CN", "KP", "CU", "SY", "BY"):
    assert bad_c in tester.UNSUPPORTED_GEMINI_COUNTRIES, f"{bad_c} missing from UNSUPPORTED_GEMINI_COUNTRIES"

# Test vXmutd regex extraction
sample_html_us = 'window.WIZ_global_data={"cfb2h":"boq","vXmutd":"%.@.\\"US\\",\\"ZZ\\",\\"Kg8nRoABeiVDD0wKMg9W6w\\\\u003d\\\\"}'
m_us = re.search(r'["\']vXmutd["\']\s*:\s*["\']%\.@\.\\?["\']([A-Z]{2})\\?["\']', sample_html_us)
assert m_us and m_us.group(1).upper() == "US", m_us

sample_html_ru = '{"vXmutd":"%.@.\\"RU\\",\\"ZZ\\""}'
m_ru = re.search(r'["\']vXmutd["\']\s*:\s*["\']%\.@\.\\?["\']([A-Z]{2})\\?["\']', sample_html_ru)
assert m_ru and m_ru.group(1).upper() == "RU", m_ru
assert m_ru.group(1).upper() in tester.UNSUPPORTED_GEMINI_COUNTRIES

# Test blocked URLs
test_blocked = lambda url: any(b in url for b in ("/sorry/", "sorry.google.com", "support.google.com"))
assert test_blocked("https://accounts.google.com/InteractiveLogin") is False
assert test_blocked("https://www.google.com/sorry/index?continue=https://gemini.google.com") is True
assert test_blocked("https://gemini.google.com/app") is False
assert test_blocked("https://consent.google.com/?continue=https://gemini.google.com") is False

# Test valid landing domains
test_valid_domain = lambda url: any(dom in url for dom in ("gemini.google.com", "accounts.google.com", "consent.google.com"))
assert test_valid_domain("https://gemini.google.com/app") is True
assert test_valid_domain("https://consent.google.com/?continue=xyz") is True
assert test_valid_domain("https://accounts.google.com/v3/signin") is True
assert test_valid_domain("https://unrelated.com/page") is False

print('Gemini validation & Google GeoIP extraction OK')

print('ALL UNIT TESTS PASSED')
