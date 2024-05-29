import enum

import warnings
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers.algorithms import *
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

class Mode(enum.Enum):
    ECB = 'ecb'
    CBC = 'cbc'
    CTR = 'ctr'
    OFB = 'ofb'
    CFB = 'cfb'
    NONE = 'none'

class Encryption():
    methods = {"aes-128-ecb": {'algorithm': algorithms.AES128, 'key_size': algorithms.AES128.key_size, 'block_size': algorithms.AES128.block_size, 'mode': Mode.ECB},
    "aes-192-ecb": {'algorithm': algorithms.AES, 'key_size': 192, 'block_size': algorithms.AES.block_size, 'mode': Mode.ECB},
    "aes-256-ecb": {'algorithm': algorithms.AES256, 'key_size': algorithms.AES256.key_size, 'block_size': algorithms.AES256.block_size, 'mode': Mode.ECB},
    "camellia-128-ecb": {'algorithm': algorithms.Camellia, 'key_size': 128, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.ECB},
    "camellia-192-ecb": {'algorithm': algorithms.Camellia, 'key_size': 192, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.ECB},
    "camellia-256-ecb": {'algorithm': algorithms.Camellia, 'key_size': 256, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.ECB},
    "seed-ecb": {'algorithm': algorithms.SEED, 'key_size': 128, 'block_size': algorithms.SEED.block_size, 'mode': Mode.ECB},
    "sm4-ecb": {'algorithm': algorithms.SM4, 'key_size': 128, 'block_size': algorithms.SM4.block_size, 'mode': Mode.ECB},
    "cast5-ecb": {'algorithm': algorithms.CAST5, 'block_size': algorithms.CAST5.block_size, 'mode': Mode.ECB},
    "bf-ecb": {'algorithm': algorithms.Blowfish, 'block_size': algorithms.Blowfish.block_size, 'mode': Mode.ECB},
    "idea-ecb": {'algorithm': algorithms.IDEA, 'key_size': 128, 'block_size': algorithms.IDEA.block_size, 'mode': Mode.ECB},
    "des3-64-ecb": {'algorithm': algorithms.TripleDES, 'key_size': 64, 'block_size': algorithms.TripleDES.block_size, 'mode': Mode.ECB},

    "aes-128-cbc": {'algorithm': algorithms.AES128, 'key_size': algorithms.AES128.key_size, 'block_size': algorithms.AES128.block_size, 'mode': Mode.CBC},
    "aes-192-cbc": {'algorithm': algorithms.AES, 'key_size': 192, 'block_size': algorithms.AES.block_size, 'mode': Mode.CBC},
    "aes-256-cbc": {'algorithm': algorithms.AES256, 'key_size': algorithms.AES256.key_size, 'block_size': algorithms.AES256.block_size, 'mode': Mode.CBC},
    "camellia-128-cbc": {'algorithm': algorithms.Camellia, 'key_size': 128, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CBC},
    "camellia-192-cbc": {'algorithm': algorithms.Camellia, 'key_size': 192, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CBC},
    "camellia-256-cbc": {'algorithm': algorithms.Camellia, 'key_size': 256, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CBC},
    "seed-cbc": {'algorithm': algorithms.SEED, 'key_size': 128, 'block_size': algorithms.SEED.block_size, 'mode': Mode.CBC},
    "sm4-cbc": {'algorithm': algorithms.SM4, 'key_size': 128, 'block_size': algorithms.SM4.block_size, 'mode': Mode.CBC},
    "cast5-cbc": {'algorithm': algorithms.CAST5, 'block_size': algorithms.CAST5.block_size, 'mode': Mode.CBC},
    "bf-cbc": {'algorithm': algorithms.Blowfish, 'block_size': algorithms.Blowfish.block_size, 'mode': Mode.CBC},
    "idea-cbc": {'algorithm': algorithms.IDEA, 'key_size': 128, 'block_size': algorithms.IDEA.block_size, 'mode': Mode.CBC},
    "des3-64-cbc": {'algorithm': algorithms.TripleDES, 'key_size': 64, 'block_size': algorithms.TripleDES.block_size, 'mode': Mode.CBC},

    "aes-128-ctr": {'algorithm': algorithms.AES128, 'key_size': algorithms.AES128.key_size, 'block_size': algorithms.AES128.block_size, 'mode': Mode.CTR},
    "aes-192-ctr": {'algorithm': algorithms.AES, 'key_size': 192, 'block_size': algorithms.AES.block_size, 'mode': Mode.CTR},
    "aes-256-ctr": {'algorithm': algorithms.AES256, 'key_size': algorithms.AES256.key_size, 'block_size': algorithms.AES256.block_size, 'mode': Mode.CTR},
    "camellia-128-ctr": {'algorithm': algorithms.Camellia, 'key_size': 128, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CTR},
    "camellia-192-ctr": {'algorithm': algorithms.Camellia, 'key_size': 192, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CTR},
    "camellia-256-ctr": {'algorithm': algorithms.Camellia, 'key_size': 256, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CTR},
    "sm4-ctr": {'algorithm': algorithms.SM4, 'key_size': 128, 'block_size': algorithms.SM4.block_size, 'mode': Mode.CTR},

    "aes-128-ofb": {'algorithm': algorithms.AES128, 'key_size': algorithms.AES128.key_size, 'block_size': algorithms.AES128.block_size, 'mode': Mode.OFB},
    "aes-192-ofb": {'algorithm': algorithms.AES, 'key_size': 192, 'block_size': algorithms.AES.block_size, 'mode': Mode.OFB},
    "aes-256-ofb": {'algorithm': algorithms.AES256, 'key_size': algorithms.AES256.key_size, 'block_size': algorithms.AES256.block_size, 'mode': Mode.OFB},
    "camellia-128-ofb": {'algorithm': algorithms.Camellia, 'key_size': 128, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.OFB},
    "camellia-192-ofb": {'algorithm': algorithms.Camellia, 'key_size': 192, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.OFB},
    "camellia-256-ofb": {'algorithm': algorithms.Camellia, 'key_size': 256, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.OFB},
    "seed-ofb": {'algorithm': algorithms.SEED, 'key_size': 128, 'block_size': algorithms.SEED.block_size, 'mode': Mode.OFB},
    "sm4-ofb": {'algorithm': algorithms.SM4, 'key_size': 128, 'block_size': algorithms.SM4.block_size, 'mode': Mode.OFB},
    "cast5-ofb": {'algorithm': algorithms.CAST5, 'block_size': algorithms.CAST5.block_size, 'mode': Mode.OFB},
    "bf-ofb": {'algorithm': algorithms.Blowfish, 'block_size': algorithms.Blowfish.block_size, 'mode': Mode.OFB},
    "idea-ofb": {'algorithm': algorithms.IDEA, 'key_size': 128, 'block_size': algorithms.IDEA.block_size, 'mode': Mode.OFB},
    "des3-64-ofb": {'algorithm': algorithms.TripleDES, 'key_size': 64, 'block_size': algorithms.TripleDES.block_size, 'mode': Mode.OFB},

    "aes-128-cfb": {'algorithm': algorithms.AES128, 'key_size': algorithms.AES128.key_size, 'block_size': algorithms.AES128.block_size, 'mode': Mode.CFB},
    "aes-192-cfb": {'algorithm': algorithms.AES, 'key_size': 192, 'block_size': algorithms.AES.block_size, 'mode': Mode.CFB},
    "aes-256-cfb": {'algorithm': algorithms.AES256, 'key_size': algorithms.AES256.key_size, 'block_size': algorithms.AES256.block_size, 'mode': Mode.CFB},
    "camellia-128-cfb": {'algorithm': algorithms.Camellia, 'key_size': 128, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CFB},
    "camellia-192-cfb": {'algorithm': algorithms.Camellia, 'key_size': 192, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CFB},
    "camellia-256-cfb": {'algorithm': algorithms.Camellia, 'key_size': 256, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CFB},
    "seed-cfb": {'algorithm': algorithms.SEED, 'key_size': 128, 'block_size': algorithms.SEED.block_size, 'mode': Mode.CFB},
    "sm4-cfb": {'algorithm': algorithms.SM4, 'key_size': 128, 'block_size': algorithms.SM4.block_size, 'mode': Mode.CFB},
    "cast5-cfb": {'algorithm': algorithms.CAST5, 'block_size': algorithms.CAST5.block_size, 'mode': Mode.CFB},
    "bf-cfb": {'algorithm': algorithms.Blowfish, 'block_size': algorithms.Blowfish.block_size, 'mode': Mode.CFB},
    "idea-cfb": {'algorithm': algorithms.IDEA, 'key_size': 128, 'block_size': algorithms.IDEA.block_size, 'mode': Mode.CFB},
    "des3-64-cfb": {'algorithm': algorithms.TripleDES, 'key_size': 64, 'block_size': algorithms.TripleDES.block_size, 'mode': Mode.CFB},

    "rc4-128": {'algorithm': algorithms.ARC4, 'key_size': 128, 'mode': Mode.NONE},
    }

class Defaults():
    ALGORITHM = "aes-128-ecb"
    KEY = "00000000000000000000000000000000"
    IV = "00000000000000000000000000000000"
    NONCE = "00000000000000000000000000000000"

encryption = Encryption()
defaults = Defaults()