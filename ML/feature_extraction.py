from urllib.parse import urlparse
import re
import ipaddress

SUSPICIOUS_WORDS=[
    "login","signin","verify","verification","account","secure","security",
    "update","confirm","confirmation","password","credential","banking",
    "payment","wallet","authenticate","authentication","unlock","suspend",
    "restricted","recover","reset"
]
BRAND_NAMES=[
    "paypal","google","microsoft","apple","amazon","facebook","instagram",
    "netflix","linkedin","twitter","whatsapp","bankofamerica","sbi","hdfc",
    "icici","axisbank"
]

def extract_url_features(url):
    url=url.strip()
    if not url:
        raise ValueError("URL cannot be empty")
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://",url):
        url="http://"+url
    parsed=urlparse(url)
    domain=parsed.netloc
    if "@" in domain:
        domain=domain.split("@")[-1]
    if ":" in domain:
        domain=domain.split(":")[0]
    path=parsed.path
    full_url=url
    url_lower=full_url.lower()
    url_length=len(full_url)
    domain_length=len(domain)
    try:
        ipaddress.ip_address(domain)
        is_domain_ip=1
    except ValueError:
        is_domain_ip=0
    domain_parts=domain.split(".")
    if len(domain_parts)>=2:
        tld_length=len(domain_parts[-1])
    else:
        tld_length=0
    no_of_subdomain=0 if is_domain_ip else max(len(domain_parts)-2,0)
    obfuscated_chars=len(re.findall(r"%[0-9a-fA-F]{2}",full_url))
    obfuscated_chars+=len(re.findall(r"\\x[0-9a-fA-F]{2}",full_url))
    has_obfuscation=1 if obfuscated_chars>0 else 0
    obfuscation_ratio=obfuscated_chars/url_length if url_length>0 else 0
    no_of_letters=sum(1 for char in full_url if char.isalpha())
    letter_ratio=no_of_letters/url_length if url_length>0 else 0
    no_of_digits=sum(1 for char in full_url if char.isdigit())
    digit_ratio=no_of_digits/url_length if url_length>0 else 0
    no_of_equals=full_url.count("=")
    no_of_qmark=full_url.count("?")
    no_of_ampersand=full_url.count("&")
    no_of_other_special_chars=sum(1 for char in full_url if not char.isalnum() and char not in set(":/?=&.-_~"))
    special_chars=sum(1 for char in full_url if not char.isalnum())
    special_char_ratio=special_chars/url_length if url_length>0 else 0
    is_https=1 if parsed.scheme.lower()=="https" else 0
    no_of_suspicious_words=sum(1 for word in SUSPICIOUS_WORDS if word in url_lower)
    has_suspicious_word=1 if no_of_suspicious_words>0 else 0
    has_brand_name=1 if any(brand in url_lower for brand in BRAND_NAMES) else 0
    no_of_hyphens=full_url.count("-")
    no_of_dots=full_url.count(".")
    path_length=len(path)
    has_login_keyword=1 if any(word in url_lower for word in ["login","signin"]) else 0
    has_verify_keyword=1 if any(word in url_lower for word in ["verify","verification","confirm","confirmation"]) else 0
    has_account_keyword=1 if any(word in url_lower for word in ["account","credential","password"]) else 0
    return {
        "URLLength":url_length,
        "DomainLength":domain_length,
        "IsDomainIP":is_domain_ip,
        "TLDLength":tld_length,
        "NoOfSubDomain":no_of_subdomain,
        "HasObfuscation":has_obfuscation,
        "NoOfObfuscatedChar":obfuscated_chars,
        "ObfuscationRatio":obfuscation_ratio,
        "NoOfLettersInURL":no_of_letters,
        "LetterRatioInURL":letter_ratio,
        "NoOfDegitsInURL":no_of_digits,
        "DegitRatioInURL":digit_ratio,
        "NoOfEqualsInURL":no_of_equals,
        "NoOfQMarkInURL":no_of_qmark,
        "NoOfAmpersandInURL":no_of_ampersand,
        "NoOfOtherSpecialCharsInURL":no_of_other_special_chars,
        "SpacialCharRatioInURL":special_char_ratio,
        "IsHTTPS":is_https,
        "HasSuspiciousWord":has_suspicious_word,
        "NoOfSuspiciousWords":no_of_suspicious_words,
        "HasBrandName":has_brand_name,
        "NoOfHyphens":no_of_hyphens,
        "NoOfDots":no_of_dots,
        "PathLength":path_length,
        "HasLoginKeyword":has_login_keyword,
        "HasVerifyKeyword":has_verify_keyword,
        "HasAccountKeyword":has_account_keyword
    }

if __name__=="__main__":
    url=input("Enter URL: ").strip()
    try:
        features=extract_url_features(url)
        print("\nExtracted Features:")
        for name,value in features.items():
            print(f"{name}: {value}")
    except Exception as error:
        print(f"\nError: {error}")