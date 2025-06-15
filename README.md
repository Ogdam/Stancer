### Docker dev container VScode
installer l'extension dev container
appuyer sur F1
chercher et lancer : ````Dev containers: Rebuild and Reopen in Container````

### Docker sur terminal
vérifier que vous avez docker d'installer

##### créer l'image
````bash
docker build -t stancer-dev-env -f .devcontainer/Dockerfile .
````
  
#### lancer sous linux

````bash
docker run --rm -it -v "$(pwd)":/workspaces/stancer-client-dev -w /workspaces/stancer-client-dev stancer-dev-env uv sync
````
````bash
docker run --rm -it -v "$(pwd)":/workspaces/stancer-client-dev -w /workspaces/stancer-client-dev stancer-dev-env /bin/sh
````
  
#### lancer sous windows avec powershell
````powershell
docker run --rm -it -v "${pwd}:/workspaces/stancer-client-dev" -w /workspaces/stancer-client-dev stancer-dev-env uv sync
````
````powershell
docker run --rm -it -v "${pwd}:/workspaces/stancer-client-dev" -w /workspaces/stancer-client-dev stancer-dev-env /bin/sh
````

### lancer le script
````bash
uv run main.py
````

### Ajouter les dependence de dev 
````bash
uv sync --extra dev
````