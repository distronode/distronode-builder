docker image rm exec-env-svn -f
rm -rf examples/bc
distronode-builder build -f examples/subversion/execution-environment.yml --container-runtime=docker -c examples/bc --tag exec-env-svn
distronode-runner --playbook svn.yml run examples/subversion
