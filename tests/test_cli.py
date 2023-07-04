#
# MIT License
#
# Copyright (c) 2023 nbiotcloud
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""Command Line."""

from pathlib import Path

from nbcpychecker.cli import main

from .util import chdir

TESTDATA = Path(__file__).parent / "testdata"


def test_noarg():
    """No Arguments."""

    with chdir(TESTDATA / "prj0"):
        assert main([]) == 2


def test_check():
    """Check."""

    with chdir(TESTDATA / "prj0"):
        assert main(["check"]) == 0


def test_check_fail(capsys):
    """Check fail."""

    with chdir(TESTDATA / "prj0-broken"):
        assert main(["check"]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert (
        captured.err
        == """\
tests/util.py:1 Copyright missing or broken.
prj0/file.py:1 Copyright missing or broken.
LICENSE:1 License missing or broken.
"""
    )
