# execute this file to generate html file
# html file will be created in DIR_BENCH

from pathlib import Path
from benchopt.plotting.generate_html import plot_benchmark_html


DIR_BENCH = "data_lasso"
OUTPUT_FILE = "benchmark_lasso_benchopt_run_preprint22.csv"


class PseudoBenchmark:

    def __init__(self):
        self.name = 'generated'

    def get_output_folder(self):
        return Path(DIR_BENCH)


plot_benchmark_html(
    fnames=Path(f'{DIR_BENCH}/{OUTPUT_FILE}'),
    benchmark=PseudoBenchmark(),
    kinds={'name': "setting_name", 'config_file': 'config_file',
           'benchmark_name': 'benchmark_name'}
)
