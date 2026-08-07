from pathlib import Path

import automation_core
import pytest

pytestmark = pytest.mark.helpers

REQUIREMENTS = Path(__file__).resolve().parents[2] / "requirements.txt"


def _pinned_core_version() -> str:
    """The automation-core tag pinned in requirements.txt, without the leading ``v``.

    Reading the pin here keeps this check honest across core version bumps
    instead of hardcoding a version that silently goes stale.
    """
    for line in REQUIREMENTS.read_text(encoding="utf-8").splitlines():
        if "automation-core" in line and "@" in line:
            tag = line.rsplit("@", 1)[-1].strip().split()[0]
            return tag.lstrip("v")
    raise AssertionError("automation-core pin not found in requirements.txt")


def test_automation_core_dependency_version():
    assert automation_core.__version__ == _pinned_core_version()
