
#!/bin/python3.7:x
import configparser, os
import click

@click.command()
@click.option('--profile', required=True, help='AWS profile')
def profile(profile):
  config = configparser.ConfigParser()
  config.sections()
  config.read(['credentials', os.path.expanduser('~/.aws/credentials')])
  GetProfile=config[profile]

  print("export AWS_ACCESS_KEY_ID={}".format(GetProfile["aws_access_key_id"]))
  print("export AWS_SECRET_ACCESS_KEY={}".format(GetProfile["aws_secret_access_key"]))
  print("export AWS_SESSION_TOKEN={}".format(GetProfile["aws_session_token"]))

if __name__ == '__main__':
    profile()
