import argparse, os
from src import hash, crypto

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Instructions for use.')
    parser.add_argument('action', action="store", help="Available options: encrypt, decrypt, hash.")
    parser.add_argument('data', action="store", help="Data for the selected action or path to file with data.")
    parser.add_argument('-g', '--gen-key', action="store", help="Available options: number of bytes in the key. The more bytes, the more reliable and slower. Cannot be used with -k (--key).")
    parser.add_argument('-k', '--key', action="store", help='Available options: key, path to .dke file.')
    parser.add_argument('-ok', '--out-key', action="store", default=False, help="Available options: path to save the key. If the parameter is not used, then the key will be printed to the console. Cannot be used with -k (--key)")
    parser.add_argument('-od', '--out-data', action='store', default=False, help="Available options: path to save the result. If the parameter is not used, then the result will be printed to the console.")
    args = parser.parse_args()

    if args.action != 'encrypt' and args.action != 'decrypt' and args.action != 'hash':
        print('Wrong action.')
        exit(0)

    if args.action == 'hash':
        print(f"Hash: {hash.gethash(args.data.encode())}")
        exit(0)

    key = None
    printKey = args.out_key

    if args.gen_key != None:
        try:
            numofbytes = int(args.gen_key)
            key = crypto.genkey(numofbytes)
            if not printKey:
                print(f'Key: {key}')
            else:
                f = open(printKey + '.dke', 'w')
                f.write(key)
                f.close()
                print(f'Key saved to {args.out_key}.')
        except Exception as e:
            if e.args[0] == 2:
                print('Wrong path to save a key.')
                exit(0)
            else:
                print('Invalid number of bytes.')
                exit(0)
    elif args.key != None:
        try:
            f = open(args.key, 'r')
            key = f.read(os.stat(args.key).st_size)
            f.close()
        except:
            key = args.key
    else:
        print('Missing key.')
        exit(0)


    if args.action == 'encrypt':
        try:
            f = open(args.data, 'r')
            args.data = f.read(os.stat(args.data).st_size)
        except:
            pass
        result = hash.gethash(key.encode()) + crypto.encrypt(args.data, key)
        if not args.out_data:
            print(f'Result: {result}')
            exit(0)

        else:
            f = open(args.out_data, 'w')
            f.write(result)
            f.close()
            print(f'Result saved to {args.out_data}.')
            exit(0)
    else:
        try:
            f = open(args.data, 'r')
            args.data = f.read(os.stat(args.data).st_size)
        except:
            pass

        if not args.data.startswith('dh'):
            print('The data is not encrypted or corrupted.')
            exit(0)

        keyhash = hash.gethash(key.encode())
        if keyhash != args.data[0:34]:
            print('Wrong key.')
            exit(0)


        result = crypto.decrypt(args.data[34:len(args.data)], key)
        if not args.out_data:
            print(f'Result: {result}')
            exit(0)

        else:
            f = open(args.out_data, 'w')
            f.write(result)
            f.close()
            print(f'Result saved to {args.out_data}.')
            exit(0)
