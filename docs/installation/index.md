# Installation

This page will guide you through the installation process this project.

## Install Dependency Management Tool

=== "uv"

    More information about [uv](https://docs.astral.sh/uv/)

    === "MacOS / Linux"

        ```bash
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```

    === "Windows"

        ```bash
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
        ```

=== "Rye"

    More information about [rye](https://rye.astral.sh/)

    === "MacOS / Linux"

        ```bash
        curl -sSf https://rye.astral.sh/get | bash
        ```

    === "Windows"

        ```powershell
        wget https://github.com/astral-sh/rye/releases/latest/download/rye-x86_64-windows.exe
        .\rye-x86_64-windows.exe
        ```

=== "Conda"

    More information about [miniconda](https://docs.anaconda.com/miniconda/install/)

    === "Linux"

        ```bash
        mkdir -p ~/miniconda3
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
        bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
        rm ~/miniconda3/miniconda.sh
        ```

    === "MacOS"

        === "Apple Silicon"

            ```bash
            mkdir -p ~/miniconda3
            curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
            bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
            rm ~/miniconda3/miniconda.sh
            ```

        === "Intel"

            ```bash
            mkdir -p ~/miniconda3
            curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
            bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
            rm ~/miniconda3/miniconda.sh
            ```

    === "Windows"

        ```powershell
        wget "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -outfile ".\miniconda.exe"
        Start-Process -FilePath ".\miniconda.exe" -ArgumentList "/S" -Wait
        del .\miniconda.exe
        ```

## Install/Setup Dependencies

=== "uv"

    ```bash
    uv sync
    ```

=== "Rye"

    ```bash
    rye sync
    ```

=== "Conda"

    ```bash
    conda create -n trending_ai python=3.10 -y
    conda activate trending_ai
    conda install uv
    uv pip sync pyproject.toml
    ```

- Once you have done the above steps, you can run the following commands to start the application.
- If your environment is messed up, you can run `uv sync` again to fix it.
