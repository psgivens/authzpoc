

function Start-AuthzDocker {
    param(
        [Parameter(Mandatory=$true)]
        [ValidateSet(
            "authz-python"
            )] 
        [string]$Container,
        [Parameter(Mandatory=$false)]
        [switch]$Bash
    )

    if (-not $env:PSGIVENS_REPOS) {
        Write-Host "Please set your PSGIVENS_REPOS environment variable to the root of your git repos."
        RETURN
    }
  
    if ($Bash) {
        docker run `
            -it `
            --rm `
            -p 8888:8888 `
            --mount type=bind,source=$env:PSGIVENS_REPOS/authzpoc,target=/authzpoc `
            $Container /bin/bash
    } else {
        Write-Host "Non-bash execution is not currently supported."
    }
}

Function Build-AuthzImage {
    param(
        [Parameter(Mandatory=$true)]
        [ValidateSet(
            "authz-python"
            )] 
        [string]$Image
    )

    if (-not $env:PSGIVENS_REPOS) {
      Write-Host "Please set your PSGIVENS_REPOS environment variable to the root of your git repos."
      RETURN
    }
  
    $repo = "{0}/authzpoc" -f $env:PSGIVENS_REPOS
  
    switch ($Image) {
        "authz-python" { 
            docker build -t authz-python -f $repo/Dockerfile $repo
        }
        Default {
            Write-Host ("Image {0} not currently supported." -f $Image)
        }
    }
  }
  

Function Update-AuthzModule {
    $MyPSModulePath = "{0}/.local/share/powershell/Modules" -f (ls -d ~)
    mkdir -p $MyPSModulePath/authzpocenv
    Write-Host ("Copying {0}/authzpoc/scripts/authzpocenv.psm1 to {1}/authzpocenv/" -f $env:PSGIVENS_REPOS,  $MyPSModulePath)
    cp -f $env:PSGIVENS_REPOS/authzpoc/scripts/authzpocenv.psm1  $MyPSModulePath/authzpocenv/
    Write-Host "Force import-module authzpocenv"
    Import-Module authzpocenv -Force 
}

Export-ModuleMember -Function Update-AuthzModule
Export-ModuleMember -Function Start-AuthzDocker
Export-ModuleMember -Function Build-AuthzImage

