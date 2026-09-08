from urllib.parse import urlparse
SUSPICIOUS_WORDS={"login","signin","verify","verification","account","secure","security","update","confirm","confirmation","password","credential","wallet","payment","invoice","bank","authorize","authentication","recover"}
BRAND_NAMES={"paypal","google","microsoft","apple","amazon","facebook","instagram","netflix","linkedin","github","bankofamerica","visa","mastercard"}
def get_domain(url):
    try:
        parsed=urlparse(url if "://" in url else "http://"+url)
        return parsed.hostname.lower() if parsed.hostname else ""
    except Exception:
        return ""
def is_brand_impersonation(url,features):
    domain=get_domain(url)
    if not domain or features.get("HasBrandName",0)==0:
        return False
    domain_parts=domain.split(".")
    main_domain=domain_parts[-2] if len(domain_parts)>=2 else domain
    for brand in BRAND_NAMES:
        if brand in domain and main_domain!=brand:
            return True
    suspicious_features=(
        features.get("HasLoginKeyword",0)==1 or
        features.get("HasVerifyKeyword",0)==1 or
        features.get("HasAccountKeyword",0)==1 or
        features.get("HasSuspiciousWord",0)==1
    )
    if suspicious_features and main_domain not in BRAND_NAMES:
        for brand in BRAND_NAMES:
            if brand in domain:
                return True
    return False
def analyze_risk(url,features):
    reasons=[]
    score=0
    if features.get("IsDomainIP",0)==1:
        score+=25
        reasons.append("URL uses an IP address instead of a domain name")
    if features.get("IsHTTPS",0)==0:
        score+=15
        reasons.append("URL does not use HTTPS")
    if features.get("DomainLength",0)>=30:
        score+=15
        reasons.append("Domain name is unusually long")
    elif features.get("DomainLength",0)>=25:
        score+=10
        reasons.append("Domain name is relatively long")
    if features.get("NoOfSubDomain",0)>=3:
        score+=10
        reasons.append("URL contains multiple subdomains")
    if features.get("NoOfHyphens",0)>=2:
        score+=10
        reasons.append("Domain contains multiple hyphens")
    if features.get("NoOfDegitsInURL",0)>=5:
        score+=10
        reasons.append("URL contains an unusually high number of digits")
    if features.get("HasObfuscation",0)==1:
        score+=20
        reasons.append("URL contains obfuscated characters")
    if features.get("HasLoginKeyword",0)==1:
        score+=10
        reasons.append("URL contains a login-related keyword")
    if features.get("HasVerifyKeyword",0)==1:
        score+=10
        reasons.append("URL contains a verification-related keyword")
    if features.get("HasAccountKeyword",0)==1:
        score+=8
        reasons.append("URL contains an account-related keyword")
    if features.get("HasSuspiciousWord",0)==1:
        score+=10
        reasons.append("URL contains suspicious security-related words")
    if is_brand_impersonation(url,features):
        score+=15
        reasons.append("URL may be impersonating a recognized brand")
    if features.get("PathLength",0)>=50:
        score+=10
        reasons.append("URL path is unusually long")
    score=min(score,100)
    if score>=60:
        risk_level="High"
    elif score>=30:
        risk_level="Medium"
    else:
        risk_level="Low"
    return score,risk_level,reasons
if __name__=="__main__":
    from feature_extraction import extract_url_features
    url=input("Enter URL: ").strip()
    if not url:
        print("Please enter a URL.")
    else:
        features=extract_url_features(url)
        score,level,reasons=analyze_risk(url,features)
        print("\nRisk Score:",f"{score}%")
        print("Risk Level:",level)
        print("Reasons:")
        if reasons:
            for reason in reasons:
                print("-",reason)
        else:
            print("- No major suspicious URL characteristics detected")