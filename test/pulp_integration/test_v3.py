import subprocess
import pytest


class TestV3:

    def test_distronode_check_is_skipped(self, cli, tmp_path, data_dir, podman_ee_tag):
        """
        Test that the check_distronode script is skipped will NOT cause build failure.
        """
        ee_def = data_dir / 'v3' / 'check_distronode' / 'ee-skip.yml'

        result = cli(
            f'distronode-builder build -c {tmp_path} -f {ee_def} -t {podman_ee_tag} '
            f'--container-runtime=podman -v3'
        )

        assert result.rc == 0

    def test_missing_distronode(self, cli, tmp_path, data_dir, podman_ee_tag):
        """
        Test that the check_distronode script will cause build failure if
        distronode-core is not installed.
        """
        ee_def = data_dir / 'v3' / 'check_distronode' / 'ee-missing-distronode.yml'

        with pytest.raises(subprocess.CalledProcessError) as einfo:
            cli(
                f'distronode-builder build -c {tmp_path} -f {ee_def} -t {podman_ee_tag} '
                f'--container-runtime=podman -v3'
            )

        assert "ERROR - Missing Distronode installation" in einfo.value.stdout

    def test_missing_runner(self, cli, tmp_path, data_dir, podman_ee_tag):
        """
        Test that the check_distronode script will cause build failure if
        distronode-runner is not installed.
        """
        ee_def = data_dir / 'v3' / 'check_distronode' / 'ee-missing-runner.yml'

        with pytest.raises(subprocess.CalledProcessError) as einfo:
            cli(
                f'distronode-builder build -c {tmp_path} -f {ee_def} -t {podman_ee_tag} '
                f'--container-runtime=podman -v3'
            )

        assert "ERROR - Missing Distronode Runner installation" in einfo.value.stdout
