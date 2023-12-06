docker image rm exec-env-blank -f
rm -rf examples/bc
distronode-builder build -f examples/blank/execution-environment.yml --container-runtime=docker -c examples/bc --tag exec-env-blank
distronode-runner --playbook debug.yml run examples/blank
