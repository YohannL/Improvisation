import argparse
import os

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--admin', action='store_true', help='launch webapp in admin mode')
    parser.add_argument('--monitor', action='store_true', help='launch webapp in monitor mode')
    
    return parser.parse_args()

def main(opt):
    assert not (opt.admin and opt.monitor)
    if opt.admin:
        os.environ["FLASK_APP"] = "WebApp/admin/main.py"
        port = 6000
    elif opt.monitor:
        os.environ["FLASK_APP"] = "WebApp/monitor/main.py"
        port = 5002
    else:
        os.environ["FLASK_APP"] = "WebApp/public/main.py"
        port = 5001

    os.system(f"flask run --host 0.0.0.0 --port {port}")


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)