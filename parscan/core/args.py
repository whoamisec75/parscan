import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host', help="Specify the host.")
parser.add_argument('--with-subs', help="Retrieve urls from subdomains of the host.", default=True)
parser.add_argument('--output', help="Specify output file", default='output.txt')
parser.add_argument('--sleep-time', help="Increase or Decrease sleep time after scanning each URL, default is 1", default=1, type=int)
parser.add_argument('-c','--concurrency', help='Specify concurrency, default is 50', default=50)
args = parser.parse_args()
host = args.host
with_subs = args.with_subs
output = args.output
sleep_time = args.sleep_time
concurrency = args.concurrency
