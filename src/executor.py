"""Module for executing Jupyter notebooks using papermill."""

import logging
from pathlib import Path
from typing import Any, Dict, Optional

import papermill as pm

logger = logging.getLogger(__name__)

def execute_notebook(
    input_path: str | Path,
    output_path: str | Path,
    parameters: Optional[Dict[str, Any]] = None,
    kernel_name: Optional[str] = None,
) -> None:
    """
    Execute a Jupyter notebook using papermill.

    Args:
        input_path: Path to the input notebook
        output_path: Path where the executed notebook will be saved
        parameters: Dictionary of parameters to inject into the notebook
        kernel_name: Name of the kernel to use for execution

    Raises:
        Exception: If notebook execution fails
    """
    try:
        logger.info(f"Executing notebook: {input_path}")
        pm.execute_notebook(
            input_path=str(input_path),
            output_path=str(output_path),
            parameters=parameters or {},
            kernel_name=kernel_name,
        )
        logger.info(f"Notebook execution completed. Output saved to: {output_path}")
    except Exception as e:
        logger.error(f"Failed to execute notebook: {str(e)}")
        raise 