import argparse
import os
import configparser

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--admin', action='store_true', help='launch webapp in admin mode')
    parser.add_argument('--monitor', action='store_true', help='launch webapp in monitor mode')
    
    return parser.parse_args()

def main(opt):
    assert not (opt.admin and opt.monitor)
    config = configparser.ConfigParser()
    config.read('config.ini')
    if opt.admin:
        os.environ["FLASK_APP"] = config['admin']['flask_app']
        port = config['admin']['port']        
    elif opt.monitor:
        os.environ["FLASK_APP"] = config['monitor']['flask_app']
        port = config['monitor']['port'] 
    else:
        os.environ["FLASK_APP"] = config['public']['flask_app']
        port = config['public']['port'] 

    host=config['api']['apiHost']
    os.system(f"flask run --host {host} --port {port}")


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)