#create typer cli automation
import typer
app = typer.Typer()

@app.command()
def mysqlconfig(ipadress: str,port: int, username: str, password: str):
    print(f"Configuring MySQL with IP: {ipadress}, Port: {port}, Username: {username}, Password: {password}")

@app.command()
def accessapi(endpoint: str, method: str):
    print(f"Accessing API Endpoint: {endpoint} with Method: {method}")

@app.command()
def deployapp(appname: str, version: str):
    print(f"Deploying App: {appname} with Version: {version}")

if __name__ == "__main__":
    app()
    