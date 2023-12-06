docker image rm exec-env-pip -f
rm -rf examples/bc
distronode-builder build -f examples/pip/execution-environment.yml --container-runtime=docker -c examples/bc --tag exec-env-pip
distronode-runner --playbook pip_bottle.yml run examples/pip -vvv
