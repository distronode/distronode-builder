docker image rm exec-env-at -f
rm -rf examples/bc
distronode-builder build -f examples/distronode.posix.at/execution-environment.yml --container-runtime=docker -c examples/bc --tag exec-env-at
distronode-runner --playbook at.yml run examples/distronode.posix.at -vvv
