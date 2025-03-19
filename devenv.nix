{ pkgs, config, ... }:
{
  packages = [
    pkgs.gnumake
    pkgs.nixfmt-rfc-style
    pkgs.treefmt
  ];
  tasks = {
    "bash:backend:install" = {
      exec = ''
        if [ ! -e instance ]; then
          ${
            pkgs.python311.withPackages (ps: [ ps.cookiecutter ])
          }/bin/cookiecutter -f --no-input --config-file backend/instance.yaml gh:plone/cookiecutter-zope-instance
          PYTHONPATH=$(pwd)/backend/src zconsole run instance/etc/zope.conf backend/scripts/create_site.py
        fi
      '';
      before = [
        "devenv:enterShell"
      ];
    };
    "bash:frontend:install" = {
      exec = ''
        if [ ! -e frontend/node_modules ]; then
          make -C frontend install
        fi
      '';
      before = [
        "devenv:enterShell"
      ];
    };
  };

  dotenv.enable = true;

  services.caddy.enable = true;
  services.caddy.config = ''
{
  admin off
}
:8000 {
  reverse_proxy /ws* localhost:3001
  handle_path "/++razzle++*" {
    rewrite * /++razzle++{uri}
    reverse_proxy localhost:3001
  }
  handle_path "/++api++*" {                                                           
    rewrite * /VirtualHostBase/https/${config.env.CODESPACE_NAME}-8000.${config.env.GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}:443/Plone/++api++/VirtualHostRoot{uri}
    reverse_proxy localhost:8080
  }
  handle_path "/api*" {
    rewrite * /VirtualHostBase/https/${config.env.CODESPACE_NAME}-8000.${config.env.GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}:443/Plone/VirtualHostRoot/_vh_api{uri}
    reverse_proxy localhost:8080
  }
  reverse_proxy http://localhost:3000
}
  '';

  processes = {
    backend.exec = "runwsgi -v instance/etc/zope.ini";
    frontend.exec = "make -C frontend start";
  };
  process.managers.process-compose.settings.environment = [
    "RAZZLE_INTERNAL_API_PATH=http://localhost:8080/VirtualHostBase/https/${config.env.CODESPACE_NAME}-8000.${config.env.GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}:443/Plone/VirtualHostRoot"
    "RAZZLE_API_PATH=https://${config.env.CODESPACE_NAME}-8000.${config.env.GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
    "CLIENT_PUBLIC_PATH=https://${config.env.CODESPACE_NAME}-8000.${config.env.GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}/++razzle++"
  ];

  enterShell = ''
    unset PYTHONPATH
    export UV=${pkgs.uv}
    export UV_NO_SYNC=1
    export UV_PYTHON_DOWNLOADS=never
    export UV_PYTHON_PREFERENCE=system
    export REPO_ROOT=$(git rev-parse --show-toplevel)/backend
  '';

  enterTest = ''
    echo ok
  '';

  cachix.pull = [ "datakurre" ];
}
