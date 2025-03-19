{ pkgs, ... }:
{
  packages = [
    pkgs.lightningcss
  ];
  languages.javascript = {
    enable = true;
    pnpm = {
      enable = true;
    };
  };
}
