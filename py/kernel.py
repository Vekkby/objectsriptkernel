from ipykernel.kernelbase import Kernel
import irisnative
import cgi
import json


def get_iris_object():
    # Create connection to InterSystems IRIS
    connection = irisnative.createConnection('iris', 51773, 'IRISAPP', '_SYSTEM', 'SYS')

    # Create an iris object
    return irisnative.createIris(connection)


class ObjectScriptKernel(Kernel):
    implementation = 'object_script'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '1.0'
    banner = 'An ObjectScript kernel'
    language_info = {
        'name': 'Arbitrary',
        'mimetype': 'text/plain',
        'file_extension': '.cls',
    }

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.iris = get_iris_object()

    def execute_code(self, code):
        class_name = "JupyterKernel.CodeExecutor"
        print(self.iris.classMethodValue(class_name, "CodeResult", code))
        return self.iris.classMethodValue(class_name, "CodeResult", code)

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            codelines = code.split('\n')
            for line_num, codeline in enumerate(codelines, start=1):
                execution_result = json.loads(self.execute_code(codeline))

                if execution_result['status']:
                    if execution_result['out']:
                        self.send_execution_result(execution_result['out'])
                else:
                    self.send_error_msg(line_num, codeline, execution_result['out'])
                    break
        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }

    def send_execution_result(self, msg_text):
        msg = {'name': 'stdout', 'text': f'{msg_text}\n'}
        self.send_response(self.iopub_socket, 'stream', msg)

    def send_error_msg(self, line_num, codeline, excecution_exception):
        exception_type, exception_msg = excecution_exception.split('>', 1)
        msg_html = (f'<p class="ansi-cyan-fg">Line {line_num}:</p>'
                    f'<p class="ansi-red-fg">{cgi.escape(codeline)}</p>'
                    f'<p><span class="ansi-red-fg">{cgi.escape(exception_type)}></span><span>{exception_msg}</span></p>')

        msg = {
                'source': 'kernel',
                'data': {
                    'text/html': msg_html
                },
                'metadata' : {}
            }

        self.send_response(self.iopub_socket, 'display_data', msg)


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=ObjectScriptKernel)
