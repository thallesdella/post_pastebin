from argparse import ArgumentParser, FileType
from pastebin import Pastebin

p = ArgumentParser(description='Publicador de arquivos no site Pastebin')

expire_date = ['N', '10M', '1H', '1D', '1W', '2W', '1M', '6M', '1Y']

p.add_argument('-d', type=str, help='Data(s) de expiração do(s) documento(s)', nargs='+', choices=expire_date, default=[])
p.add_argument('-s', type=str, help='Sintaxe do(s) arquivo(s) a ser(em) publicado(s)', nargs='+', default=[])
p.add_argument('-A', type=FileType('r'), help='Arquivo(s) a ser(em) publicado(s)', nargs='+', required=True)

args = p.parse_args()

#paste = Pastebin('api_dev_key', 'api_username', 'api_password')
paste = Pastebin('', '', '')

c = 0
for arquivo in args.A:
    expire = None
    if c < len(args.d):
        expire = args.d[c]

    sintaxe = None        
    if c < len(args.s):
        sintaxe = args.s[c]
        
    url = paste.new_paste(code=arquivo.read(), paste_name=arquivo.name, paste_format=sintaxe, paste_private=1, paste_expire_date=expire)

    if url is not None:        
        print('{} - {}'.format(arquivo.name, url))
    else:
        for error in paste.get_error:
            print(error)

    arquivo.close()
    c += 1
