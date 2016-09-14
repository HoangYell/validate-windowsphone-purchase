import urllib
import urllib2
from fake_useragent import UserAgent

ua = UserAgent()
url = 'https://www.aleksey.com/cgi-bin/xmldsigverify'
receipt_data='<?xml version="1.0"?><Receipt Version="1.0" CertificateId="A656B9B1B3AA509EEA30222E6D5E7DBDA9822DCD" xmlns="http://schemas.microsoft.com/windows/2012/store/receipt"><ProductReceipt PurchasePrice="$20.89" PurchaseDate="2012-11-30T21:32:07.096Z" Id="2f9c5c8f-3e1d-4fc7-a871-ac58f7e78053" AppId="3ec6cd9a-ca82-4d38-bfdf-ecafdb35a738" ProductId="Test" ProductType="Consumable" PublisherDeviceId="Test" MicrosoftProductId="59ef70aa-7099-4679-889e-f21919bfd2c6" /><Signature xmlns="http://www.w3.org/2000/09/xmldsig#"><SignedInfo><CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" /><SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" /><Reference URI=""><Transforms><Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" /></Transforms><DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" /><DigestValue>FyFb1HGm+yeOIjt18M6TPD4Qzeu469vwDbQs7w72mdA=</DigestValue></Reference></SignedInfo><SignatureValue>noct5CYBtRwBxVxkUeZIzeDyruLGVBqBMuFuBytpouPLACnQ5dbzdRvWX4XN67IUo0J2FW8DoYcMbf3sAS+PeKKV8SLnU+l8K1hWEbbbugHZezStTzwwkYcZuCTnAk7BYO0aiZWuXm9GiZGT9iyXsYtU1/u87L+llnVibU/m7gV8tD3vG0tVkjzV20C8666mHUsY/jxeq3ed7YY9CT0SDrh5PeL4ESaopBLcncHo/e6lcjyoKbO3e6YuIpsi8DVueeKNhpTlwa5yc0O3qzc5SGnT4Kbhj9NBEXf15/oTaLlg7lJhnQZ0mY+yR8vc4D0SkqD6e5Uc4u64hnu+g3Hphg==</SignatureValue></Signature></Receipt>'
# receipt_data=None
# with open('ReceiptSHA256.xml') as data_file:
#     receipt_data = str(data_file.read())


values = {'_xmldoc': receipt_data}
headers = {'User-Agent': ua.chrome}

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print "TheResult:--------\n"+the_page