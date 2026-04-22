#create click cli automation
import click
@click.group()
def cli():
    pass


@click.command()
@click.option('--ipadress', prompt='MySQL IP Address', help='The IP address of the MySQL server.')
@click.option('--port', prompt='MySQL Port', help='The port number of the MySQL server.', type=int)
@click.option('--username', prompt='MySQL Username', help='The username for the MySQL server.')
@click.option('--password', prompt='MySQL Password', help='The password for the MySQL server.', hide_input=True)
def mysqlconfig(ipadress, port, username, password):
    click.echo(f"Configuring MySQL with IP: {ipadress}, Port: {port}, Username: {username}, Password: {password}")

@click.command()
@click.option('--endpoint', prompt='API Endpoint', help='The endpoint of the API.')
@click.option('--method', prompt='HTTP Method', help='The HTTP method for the API request.')
def accessapi(endpoint, method):
    click.echo(f"Accessing API Endpoint: {endpoint} with Method: {method}")

cli.add_command(mysqlconfig)
cli.add_command(accessapi)
if __name__ == '__main__':
    cli()