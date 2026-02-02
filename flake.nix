{
  description = "Pigz Challenge Environment";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          python311
          python311Packages.pip
          python311Packages.virtualenv
          docker
          docker-compose
        ];
        shellHook = ''
          echo "🍕 Ambiente Pigz Backend carregado!"
          # Cria venv se não existir
          if [ ! -d ".venv" ]; then
            python -m venv .venv
          fi
          source .venv/bin/activate
        '';
      };
    };
}
