import os
import shutil
import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

project_root = os.getcwd()
inputs_list = [
    [project_root, 'index.ipynb'],
    [os.path.join(project_root, 'notebooks/color_correction_tutorial'), 'color_correct_tutorial.ipynb'],
    [os.path.join(project_root, 'notebooks/hyperspectral_tutorial'), 'hyperspectral_tutorial.ipynb'],
    [os.path.join(project_root, 'notebooks/input_output_tutorial'), 'input_output.ipynb'],
    [os.path.join(project_root, 'notebooks/morphology_tutorial'), 'morphology_tutorial.ipynb'],
    [os.path.join(project_root, 'notebooks/multi_plant_tutorial'), 'multi_plant_tutorial.ipynb'],
    [os.path.join(project_root, 'notebooks/naive_bayes_tutorial'), 'machine_learning.ipynb'],
    [os.path.join(project_root, 'notebooks/nir_tutorial'), 'nir_tutorial.ipynb'],
    [os.path.join(project_root, 'notebooks/photosynthesis_tutorial'), 'psII_tutorial.ipynb'],
    [os.path.join(project_root, 'notebooks/roi_tutorial'), 'roi_package.ipynb'],
    [os.path.join(project_root, 'notebooks/thermal_tutorial'), 'thermal.ipynb'],
    [os.path.join(project_root, 'notebooks/threshold_tutorial'), 'threshold.ipynb'],
    [os.path.join(project_root, 'notebooks/vis_nir_tutorial'), 'vis_nir_tutorial.ipynb'],
    [os.path.join(project_root, 'notebooks/vis_tutorial'), 'vis_tutorial.ipynb'],
    [os.path.join(project_root, 'notebooks/watershed_segmentation_tutorial'), 'segmentation.ipynb'],
    [os.path.join(project_root, 'notebooks/new_side_view_morphology_tutorial'), 'smorphology_analysis_side_view_workflow.ipynb'],
    [os.path.join(project_root, 'notebooks/aerial_view_morphology_tutorial'), 'morphology_analysis_aerial_view_workflow.ipynb'],
    [os.path.join(project_root, 'notebooks/seed_analysis_tutorial'), 'seed-analysis-workflow.ipynb'],
    [os.path.join(project_root, 'notebooks/visualization_methods'), 'visualization_methods_workflow.ipynb']
]


# ##########################
# Tests executing the notebook
# ##########################
@pytest.mark.parametrize('dir,notebook', inputs_list)
def test_notebook(dir, notebook, tmpdir):
    tmp = tmpdir.mkdir('sub')
    # Change working directory
    os.chdir(dir)
    # Open the notebook
    with open(notebook, "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Process the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": dir}})

    # Save the executed notebook
    out_nb = os.path.join(tmp, "executed_notebook.ipynb")
    with open(out_nb, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    assert os.path.exists(out_nb)
