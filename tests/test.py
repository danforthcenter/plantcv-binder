import os
import shutil
import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

TEST_TMPDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".cache")


# ##########################
# Tests setup function
# ##########################
def setup_function():
    if not os.path.exists(TEST_TMPDIR):
        os.mkdir(TEST_TMPDIR)


# ##########################
# Tests executing the notebook
# ##########################
@pytest.mark.parametrize('notebook', ['index.ipynb'])
def test_notebook(notebook, tmpdir):
    tmp = tmpdir.mkdir('sub')
    # Open the notebook
    with open(notebook, "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Process the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": TEST_TMPDIR}})

    # Save the executed notebook
    out_nb = os.path.join(tmp, "executed_notebook.ipynb")
    with open(out_nb, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    assert os.path.exists(out_nb)


# ##############################
# Clean up test files
# ##############################
def teardown_function():
    shutil.rmtree(TEST_TMPDIR)