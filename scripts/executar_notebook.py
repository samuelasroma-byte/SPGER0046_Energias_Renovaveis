"""Execute real notebook cells with IPython, preserving rich outputs.

This runner does not need a listening Jupyter socket, so it also works in
restricted execution hosts. An ordinary Jupyter/Colab kernel remains supported.
"""
from pathlib import Path
from contextlib import redirect_stdout, redirect_stderr
import os
import sys
import io
import nbformat
from IPython.core.interactiveshell import InteractiveShell


class NotebookStream:
    def __init__(self, outputs, name):
        self.outputs, self.name = outputs, name
    def write(self, value):
        if not value:
            return 0
        if self.outputs and self.outputs[-1].output_type == 'stream' and self.outputs[-1].name == self.name:
            self.outputs[-1].text += value
        else:
            self.outputs.append(nbformat.v4.new_output('stream', name=self.name, text=value))
        return len(value)
    def flush(self):
        pass
    def isatty(self):
        return False


def main():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--notebook',type=Path)
    args=parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    target = args.notebook.resolve() if args.notebook else root / 'notebooks/01_Projeto_FV_Quatro_Secoes.ipynb'
    nb = nbformat.read(target, as_version=4)
    shell = InteractiveShell.instance()
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from IPython.display import display, Image
    def inline_show(*args, **kwargs):
        for number in plt.get_fignums():
            fig = plt.figure(number)
            buffer = io.BytesIO()
            fig.savefig(buffer, format='png', dpi=120, bbox_inches='tight')
            display(Image(data=buffer.getvalue()))
            plt.close(fig)
    plt.show = inline_show
    real_stdout = sys.stdout
    os.chdir(root)
    count = 0
    for index, cell in enumerate(nb.cells):
        if cell.cell_type != 'code':
            continue
        count += 1
        outputs = []
        def publish(data, metadata=None, **kwargs):
            outputs.append(nbformat.v4.new_output('display_data', data=data, metadata=metadata or {}))
        def execute_result(data, metadata=None):
            outputs.append(nbformat.v4.new_output('execute_result', data=data, metadata=metadata or {}, execution_count=count))
        shell.display_pub.publish = publish
        shell.displayhook.write_output_prompt = lambda: None
        shell.displayhook.write_format_data = execute_result
        with redirect_stdout(NotebookStream(outputs, 'stdout')), redirect_stderr(NotebookStream(outputs, 'stderr')):
            result = shell.run_cell(cell.source, store_history=True)
        cell.execution_count = count
        cell.outputs = outputs
        if result.error_before_exec or result.error_in_exec:
            raise RuntimeError(f'Notebook cell {index} failed') from (result.error_before_exec or result.error_in_exec)
        print(f'Executed code cell {count}: {cell.source.splitlines()[0][:65]}', file=real_stdout, flush=True)
    nb.metadata['execution'] = {'runner': 'IPython InteractiveShell; sequential real cell execution with rich output capture', 'python': sys.version.split()[0], 'all_code_cells_succeeded': True}
    nbformat.validate(nb)
    nbformat.write(nb, target)
    print(f'Saved executed notebook: {target.name}; {count} code cells; {target.stat().st_size} bytes', file=real_stdout)


if __name__ == '__main__':
    main()
