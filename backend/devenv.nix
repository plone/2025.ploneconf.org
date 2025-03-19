{
  pkgs,
  inputs,
  ...
}:
let
  python = pkgs.python311;
  workspace = inputs.uv2nix.lib.workspace.loadWorkspace {
    workspaceRoot = ./.;
  };
  overlay = workspace.mkPyprojectOverlay {
    sourcePreference = "wheel";
  };
  pythonSet =
    (pkgs.callPackage inputs.pyproject-nix.build.packages {
      inherit python;
    }).overrideScope
      (
        pkgs.lib.composeManyExtensions [
          inputs.pyproject-build-systems.overlays.default
          overlay
          (import ./overrides.nix { inherit pkgs; })
        ]
      );
  editableOverlay = workspace.mkEditablePyprojectOverlay {
    root = "$REPO_ROOT";
  };
  editablePythonSet = pythonSet.overrideScope editableOverlay;
  pyprojectName = (builtins.fromTOML (builtins.readFile (./pyproject.toml))).project.name;
  virtualenv =
    (editablePythonSet.mkVirtualEnv "${pyprojectName}-dev-env" workspace.deps.all).overrideAttrs
      (old: {
        venvIgnoreCollisions = [ "*" ];
      });
in
{
  packages = [
    virtualenv
  ];
}
