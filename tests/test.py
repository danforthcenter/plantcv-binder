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
inputs_list = [
    ['.', 'index.ipynb'],
    ['notebooks/color_correction_tutorial', 'color_correct_tutorial.ipynb'],
    ['notebooks/hyperspectral_tutorial', 'hyperspectral_tutorial.ipynb'],
    ['notebooks/input_output_tutorial', 'input_output.ipynb'],
    ['notebooks/morphology_tutorial', 'morphology_tutorial.ipynb'],
    ['notebooks/multi_plant_tutorial', 'multi_plant_tutorial.ipynb'],
    ['notebooks/naive_bayes_tutorial', 'machine_learning.ipynb'],
    ['notebooks/nir_tutorial', 'nir_tutorial.ipynb'],
    ['notebooks/photosynthesis_tutorial', 'psII_tutorial.ipynb'],
    ['notebooks/roi_tutorial', 'roi_package.ipynb'],
    ['notebooks/thermal_tutorial', 'thermal.ipynb'],
    ['notebooks/threshold_tutorial', 'threshold.ipynb'],
    ['notebooks/vis_nir_tutorial', 'vis_nir_tutorial.ipynb'],
    ['notebooks/vis_tutorial', 'vis_tutorial.ipynb'],
    ['notebooks/watershed_segmentation_tutorial', 'segmentation.ipynb']
]

@pytest.mark.parametrize('dir,notebook', notebook_list)
def test_notebook(notebook, tmpdir):
    tmp = tmpdir.mkdir('sub')
    # Change working directory
    os.chdir(dir)
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
