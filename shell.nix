{ pkgs ? import <nixpkgs> {} }:
let
  diffusion-python = (pkgs.python3.withPackages (ps: with ps; [
    pip
    build
    twine
    numpy
    matplotlib
  ]));
in pkgs.mkShell {
  buildInputs = with pkgs; [
    diffusion-python
    autoPatchelfHook
    zlib
    gcc-unwrapped.lib
  ];

  shellHook = ''
    export PYTHON_PATH="$(pwd)/.python"
    export PIP_PREFIX="$PYTHON_PATH/pip_packages"
    mkdir -pv "$PIP_PREFIX"

    export PYTHONPATH="$PYTHON_PATH/pip_packages/lib/python3.8/site-packages:$PYTHONPATH"
    export PATH="$PATH:$PIP_PREFIX/bin"

    # pip install numpy
    # pip install matplotlib
    # autoPatchelf $PYTHON_PATH

    exec zsh
  '';
}
