

Function Initialize-ZapDastEnv {

  # Create the volume for the database
  Write-Host "creating volume dast-pgsql-volume"
  docker volume create dast-pgsql-volume

  # Create the network
  Write-Host "Creating network dast-net"
  docker network create --driver bridge dast-net

  Write-Host "Pulling chorss/docker-pgadmin4"
  docker image pull chorss/docker-pgadmin4
}

Function Reset-DastDbVolume {
  docker volume rm dast-pgsql-volume
  docker volume create dast-pgsql-volume
}

Function Build-DastImages {
  if (-not $env:ZAPDAST_REPOS) {
    Write-Host "Please set your ZAPDAST_REPOS environment variable to the root of your git repos."
    RETURN
  }

  $repo = "{0}/zapdast" -f $env:ZAPDAST_REPOS

  # Build the pgsql database
  docker build -t dast-pgsql -f $repo/pgsql/Dockerfile $repo/pgsql
}

Function Start-DastEnv {
  if (-not $env:ZAPDAST_REPOS) {
    Write-Host "Please set your ZAPDAST_REPOS environment variable to the root of your git repos."
    RETURN
  }

  $repo = "{0}/zapdast" -f $env:ZAPDAST_REPOS

  Write-Host ("Starting database as dast-pgsql")
  # run the database container
  # https://hub.docker.com/_/postgres/
  docker run `
    --name dast-pgsql `
    --network dast-net `
    --rm `
    -p 5432:5432 `
    -e POSTGRES_PASSWORD=Password1 `
    -e POSTGRES_USER=samplesam `
    -e POSTGRES_DB=defaultdb `
    -e PGDATA=/var/lib/postgresql/data/pgdata `
    --mount type=bind,source=$repo/dast/sql,target=/dast/sql `
    --mount source=dast-pgsql-volume,target=/var/lib/postgresql/data/pgdata `
    -d `
    dast-pgsql

    Write-Host ("Starting pgadmin as dast-pgadmin")
    # Use pgadmin to explore the database
    docker run `
      -p 5050:5050 `
      --rm `
      --name dast-pgadmin `
      --network dast-net `
      -e "PGADMIN_DEFAULT_EMAIL=user@domain.com" `
      -e "PGADMIN_DEFAULT_PASSWORD=Password1" `
      -d `
      chorss/docker-pgadmin4

}

Function Connect-DastDocker {
    param(
        [Parameter(Mandatory=$false)]
        [ValidateSet(
            "dast-pgsql", 
            "dast-pgadmin"
            )] 
        [string]$Container
    )
    docker exec -it $Container /bin/sh
}


Function Stop-DastEnv {
  Write-Host "Stopping dast-pgsql"
  docker container stop dast-pgsql

  Write-Host "Stopping dast-pgadmin"
  docker container stop dast-pgadmin
}


Function Update-DastModule {
  $MyPSModulePath = "{0}/.local/share/powershell/Modules" -f (ls -d ~)
  mkdir -p $MyPSModulePath/ZapDastEnv
  Write-Host ("Copying {0}/zapdast/scripts/ZapDastEnv.psm1 to {1}/ZapDastEnv/" -f $env:ZAPDAST_REPOS,  $MyPSModulePath)
  cp -f $env:ZAPDAST_REPOS/zapdast/scripts/ZapDastEnv.psm1  $MyPSModulePath/ZapDastEnv/
  Write-Host "Force import-module ZapDastEnv"
  Import-Module ZapDastEnv -Force 
}

Export-ModuleMember -Function Initialize-ZapDastEnv
Export-ModuleMember -Function Build-DastImages
Export-ModuleMember -Function Start-DastEnv
Export-ModuleMember -Function Connect-DastDocker
Export-ModuleMember -Function Stop-DastEnv
Export-ModuleMember -Function Update-DastModule
Export-ModuleMember -Function Reset-DastDbVolume