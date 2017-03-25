# Tokens:
#   (Malul):  Mjk0ODg2OTI5NzM1MDkwMTg2.C7b7Fg.adre6bVKOBEYvJL0QZyUPz5VV2I
#   (Zafig):  MjkzMDk1NzY0MDEwMzM2MjY2.C7bqXA.QjOGFq-bP409lsLH6T7TNzS1LgQgit
#   (Fknfgt): Mjk0ODgzNjI3MTY1MDI0MjU4.C7bnWA.T466dvvu3Z0cssV7tuBgfffGRb0
#   (John):   Mjk0ODg3MDk2MjM2MjQ1MDAy.C7cAaQ.1P9z_JvnQ3AQz3GO5C42iRpXXUA

token_dict = { 'malul' : 'Mjk0ODg2OTI5NzM1MDkwMTg2.C7b7Fg.adre6bVKOBEYvJL0QZyUPz5VV2I',
               'zafig' : 'MjkzMDk1NzY0MDEwMzM2MjY2.C7bqXA.QjOGFq-bP409lsLH6T7TNzS1LgQgit',
               'fknfgt' : 'Mjk0ODgzNjI3MTY1MDI0MjU4.C7bnWA.T466dvvu3Z0cssV7tuBgfffGRb0',
               'yoni' : 'Mjk0ODg3MDk2MjM2MjQ1MDAy.C7cAaQ.1P9z_JvnQ3AQz3GO5C42iRpXXUA',
               'prod' : ''
               }
def get_discord_token(key):
    return token_dict[key]
