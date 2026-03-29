"""
Example problem registry for verilog evaluation template.
For internal problems, use phinitylabs/verilog-eval-internal.
"""
import logging
from hud_controller.spec import ProblemSpec, PROBLEM_REGISTRY

logger = logging.getLogger(__name__)

# =============================================================================
# EXAMPLE PROBLEMS - For demonstration only
# =============================================================================

PROBLEM_REGISTRY.append(
    ProblemSpec(
        id="crc_stream",
        description="""Please implement a CRC stream generator according to the specifications .
        For more details, please refer to the specifications.md  at docs/specifications.md

""",
        difficulty="easy",
        base="crc_stream_baseline",
        test="crc_stream_test",
        golden="crc_stream_golden",
        test_files=["tests/test_crc_stream_hidden.py"],
    )
)
