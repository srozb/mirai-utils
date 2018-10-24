# mirai-utils
reveal xored strings in mirai binary

## usage:
* `crack_mirai.py <mirai binary>` - will try to guess the XOR key and decrypt the binary
* `decode_mirai.py <mirai binary>` - will try to do it with the default key which is `0xdeadbeef`
  
The effective lenght of key is 1 byte anyway.

## take a look at:

https://github.com/srozb/spyrai - harmless mirai botnet client.
