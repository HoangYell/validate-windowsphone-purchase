import urllib
import urllib2
from fake_useragent import UserAgent
from lxml import etree

ua = UserAgent()
url = 'https://www.aleksey.com/cgi-bin/xmldsigverify'
receipt_data='<Receipt xmlns="http://schemas.microsoft.com/windows/2012/store/receipt" Version="1.0" CertificateId="A656B9B1B3AA509EEA30222E6D5E7DBDA9822DCD"><ProductReceipt PurchasePrice="$20.89" PurchaseDate="2012-11-30T21:32:07.096Z" Id="2f9c5c8f-3e1d-4fc7-a871-ac58f7e78053" AppId="3ec6cd9a-ca82-4d38-bfdf-ecafdb35a738" ProductId="Test" ProductType="Consumable" PublisherDeviceId="Test" MicrosoftProductId="59ef70aa-7099-4679-889e-f21919bfd2c6"/><Signature xmlns="http://www.w3.org/2000/09/xmldsig#"><SignedInfo><CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/><SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/><Reference URI=""><Transforms><Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/></Transforms><DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/><DigestValue>FyFb1HGm+yeOIjt18M6TPD4Qzeu469vwDbQs7w72mdA=</DigestValue></Reference></SignedInfo><SignatureValue>noct5CYBtRwBxVxkUeZIzeDyruLGVBqBMuFuBytpouPLACnQ5dbzdRvWX4XN67IUo0J2FW8DoYcMbf3sAS+PeKKV8SLnU+l8K1hWEbbbugHZezStTzwwkYcZuCTnAk7BYO0aiZWuXm9GiZGT9iyXsYtU1/u87L+llnVibU/m7gV8tD3vG0tVkjzV20C8666mHUsY/jxeq3ed7YY9CT0SDrh5PeL4ESaopBLcncHo/e6lcjyoKbO3e6YuIpsi8DVueeKNhpTlwa5yc0O3qzc5SGnT4Kbhj9NBEXf15/oTaLlg7lJhnQZ0mY+yR8vc4D0SkqD6e5Uc4u64hnu+g3Hphg==</SignatureValue><KeyInfo><X509Data><X509Certificate>MIIDFDCCAgCgAwIBAgIQrih3cQuSeL1CgpLFusfJsTAJBgUrDgMCHQUAMB8xHTAbBgNVBAMTFElhcFJlY2VpcHRQcm9kdWN0aW9uMB4XDTEyMDIxNzAxMTYyNFoXDTM5MTIzMTIzNTk1OVowHzEdMBsGA1UEAxMUSWFwUmVjZWlwdFByb2R1Y3Rpb24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDb0CeltVqOOIJiwNGgAr7Z0K4rAYsHCa1oSFPJXtokz134bi2neJ8bHIKAnT0kwa3xViUxwp3+OZd2t2PshDv0ucZ5dus6WCnuAw/MHVAodgLQMqYiKeM7VTIi3S1s3iV/66Y8KP7jH3CmE2XCXOQae+bQUuyGsTit0ScU7+MofODoNhvONs54n/K1WVnct2wWBpn8GGAS+l2mzOF0jXbMSjtz7wuK77GeydG+x9paLuHIyCso7tjOqv/lvol5IIX0VnC5G2vC6dWR6MkNL5FzLXnsSuQgoYEUZXPlXJhsmv6oyyenaP0PpYJZcCLLVi1L2hcVo8B2DIEg3I3t8ch/AgMBAAGjVDBSMFAGA1UdAQRJMEeAEHGLK3BRpCWDa2vU50kI73ehITAfMR0wGwYDVQQDExRJYXBSZWNlaXB0UHJvZHVjdGlvboIQrih3cQuSeL1CgpLFusfJsTAJBgUrDgMCHQUAA4IBAQC4jmOu0H3j7AwVBvpQzPMLBd0GTimBXmJw+nruE+0Hh/0ywGTFNE+KcQ21L4v+IuP8iMh3lpOcPb23ucuaoNSdWi375/KxrW831dbh+goqCZP7mWbxpnSnFnuV+R1VPsQjdS+0tg5gjDKNMSx/2fH8krLAkidJ7rvUNmtEWMeVNk0/ZM/ECinobMSSwbqUuc9Qql9T1epe+xv34a6eek+m4W0VXnLSuKhQS5jdILsyeJWHROZF5mrh3DQuS0Ll5FzKmJxHf0hyXAo03SSA+x3JphAU4oYbkE9nRTU1tR6iq1D9ZxfQmvzmIbMfyJ/y89PLs/ewHopSK7vQmGFjfjIl</X509Certificate></X509Data><KeyValue><RSAKeyValue><Modulus>29AnpbVajjiCYsDRoAK+2dCuKwGLBwmtaEhTyV7aJM9d+G4tp3ifGxyCgJ09JMGt8VYlMcKd/jmXdrdj7IQ79LnGeXbrOlgp7gMPzB1QKHYC0DKmIinjO1UyIt0tbN4lf+umPCj+4x9wphNlwlzkGnvm0FLshrE4rdEnFO/jKHzg6DYbzjbOeJ/ytVlZ3LdsFgaZ/BhgEvpdpszhdI12zEo7c+8Liu+xnsnRvsfaWi7hyMgrKO7Yzqr/5b6JeSCF9FZwuRtrwunVkejJDS+Rcy157ErkIKGBFGVz5VyYbJr+qMsnp2j9D6WCWXAiy1YtS9oXFaPAdgyBINyN7fHIfw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue></KeyValue></KeyInfo></Signature></Receipt>'
# receipt_data=None
# with open('wp1.xml') as data_file:
#     receipt_data = str(data_file.read())

#remove all space between >remove me<
parser = etree.XMLParser(remove_blank_text=True)
elem = etree.XML(receipt_data,parser=parser)
receipt_data=etree.tostring(elem)

print receipt_data
print"------------------------------------"
values = {'_xmldoc': receipt_data}
headers = {'User-Agent': ua.chrome}

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print "TheResult:--------\n"+the_page
