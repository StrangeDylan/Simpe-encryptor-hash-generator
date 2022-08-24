A simple implementation of encryption and hash generation. If you do not pay attention to the millions of possible vulnerabilities, then you can even use it for serious purposes.
---
**Doesn't require any additional libraries.**

	Instructions for use.

	positional arguments:
	  action                Available options: encrypt, decrypt, hash.
	  data                  Data for the selected action or path to file with data.

	optional arguments:
	  -h, --help                                    show this help message and exit
	  
	  -g GEN_KEY, --gen-key GEN_KEY 		Available options: number of bytes in the key. The more bytes, the more
							reliable and slower. Cannot be used with -k (--key).
							
	  -k KEY, --key KEY                             Available options: key, path to .dke file.
	  
	  -ok OUT_KEY, --out-key OUT_KEY 		Available options: path to save the key. If the parameter is not used,
							then the key will be printed to the console. Cannot be used with -k
							(--key)
							
	  -od OUT_DATA, --out-data OUT_DATA		Available options: path to save the result. If the parameter is not used,
							then the result will be printed to the console.
