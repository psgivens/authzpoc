# authzpoc



## Environment
Set a local environment variable POMODORO_REPOS to the folder containing your Pomodoro Repos 

    $env:PSGIVENS_REPOS= "{0}/Repos/psgivens" -f (ls -d ~)

Link the powershell modules to the psmodule path

  $MyPSModulePath = "{0}/.local/share/powershell/Modules" -f (ls -d ~)
  mkdir -p $MyPSModulePath/authzpocenv
  cp -f $env:ZAPDAST_REPOS/authzpoc/scripts/authzpocenv.psm1  $MyPSModulePath/authzpocenv/
  Import-Module authzpocenv -Force 

Once the ZapDastEnv.psm1 is installed you can use the cmdlets to start and stop the environment. 

    Get-Command -Module ZapDastEnv


        docker run `
            -it `
            --rm `
            --mount type=bind,source=$env:PSGIVENS_REPOS/authzpoc,target=/authzpoc `
            python:3 /bin/sh    