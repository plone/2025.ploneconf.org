{ pkgs, ... }:
final: prev: {
  "collective.volto.formsupport" = prev."collective.volto.formsupport".overrideAttrs (old: {
    nativeBuildInputs =
      old.nativeBuildInputs
      ++ final.resolveBuildSystem ({
        "setuptools" = [ ];
      });
  });
  "collective-volto-otp" = prev."collective-volto-otp".overrideAttrs (old: {
    nativeBuildInputs =
      old.nativeBuildInputs
      ++ final.resolveBuildSystem ({
        "setuptools" = [ ];
      });
    postInstall = ''
      find $out -type f -name "*.po" -exec sh -c 'for f; do ${pkgs.gettext}/bin/msgfmt "$f" -o "''${f%.po}.mo"; done' _ {} +
    '';
  });
  "hatchling" = prev."hatchling".overrideAttrs (old: {
    propagatedBuildInputs = [ final."editables" ];
  });
  "pas-plugins-authomatic" = prev."pas-plugins-authomatic".overrideAttrs (old: {
    postInstall = ''
      find $out -type f -name "*.po" -exec sh -c 'for f; do ${pkgs.gettext}/bin/msgfmt "$f" -o "''${f%.po}.mo"; done' _ {} +
    '';
  });
  "products-cmfcore" = prev."products-cmfcore".overrideAttrs (old: {
    postInstall = ''
      find $out -type f -name "*.po" -exec sh -c 'for f; do ${pkgs.gettext}/bin/msgfmt "$f" -o "''${f%.po}.mo"; done' _ {} +
    '';
  });
  "repoze-xmliter" = prev."repoze-xmliter".overrideAttrs (old: {
    nativeBuildInputs =
      old.nativeBuildInputs
      ++ final.resolveBuildSystem ({
        "setuptools" = [ ];
      });
  });
  "sgmllib3k" = prev."sgmllib3k".overrideAttrs (old: {
    nativeBuildInputs =
      old.nativeBuildInputs
      ++ final.resolveBuildSystem ({
        "setuptools" = [ ];
      });
  });
  "souper-plone" = prev."souper-plone".overrideAttrs (old: {
    nativeBuildInputs =
      old.nativeBuildInputs
      ++ final.resolveBuildSystem ({
        "setuptools" = [ ];
      });
  });
  "z3c-form" = prev."z3c-form".overrideAttrs (old: {
    postInstall = ''
      find $out -type f -name "*.po" -exec sh -c 'for f; do ${pkgs.gettext}/bin/msgfmt "$f" -o "''${f%.po}.mo"; done' _ {} +
    '';
  });
  "z3c-formwidget-query" = prev."z3c-formwidget-query".overrideAttrs (old: {
    postInstall = ''
      find $out -type f -name "*.po" -exec sh -c 'for f; do ${pkgs.gettext}/bin/msgfmt "$f" -o "''${f%.po}.mo"; done' _ {} +
    '';
  });
  "zodb3" = prev."zodb3".overrideAttrs (old: {
    nativeBuildInputs =
      old.nativeBuildInputs
      ++ final.resolveBuildSystem ({
        "setuptools" = [ ];
      });
  });
}
